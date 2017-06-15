import threading
from multiprocessing import Pool, cpu_count
from imageio import imread
import re
import os
import sys
import numpy as np

IMAGE_REGEX = re.compile("([^\\s]+(\\.(?i)(jpg|png|gif|bmp))$)")

def is_image_url(path):
    return bool(IMAGE_REGEX.match(path))

def get_images(path):
    return list(map(lambda p: os.path.abspath(os.path.join(path, p)), filter(is_image_url, os.listdir(path))))

def read_image(path):
    _id = os.path.basename(path).split('.')[0]
    print('read: ' + path)
    try:
        image = imread(path)
        image_flat = image.flatten()
        prefix = str(_id) + ',"' + str(image.shape) + '",'
        row = prefix + ','.join(np.char.mod('%d', image_flat))
        print('done: ' + path)
        return row
    except Exception as e:
        print(e)
        return e

if __name__ == "__main__": # DONOT REMOVE THIS LINE - it makes the multithreading part work.

    if len(sys.argv) != 3:
        print('Usage: python extract_image_data.py <input_folder_path> <output_csv_path>')
    else:
        _, inpath, outpath = sys.argv
        n_threads = cpu_count()
        images = get_images(inpath)

        if len(images) == 0:
            print('no images found!')
        else:
            print('found ' + str(len(images)) + ' images, running in ' + str(n_threads) + ' threads')
            image_data = Pool(n_threads).map(read_image, images)
            csv_data = '\n'.join(image_data)

            with open(outpath, 'w') as f:
                f.write(csv_data)
            