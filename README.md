# extract_image_data (Images2CSV)
Multi-threaded script for converting a large number of images to CSV data

## Usage

```bash
$ python extract_image_data.py <input_folder_path> <output_csv_path>
```

## Requirements

Install the requirements by calling `pip` on the `requirements.txt` file

```bash
$ pip install -r requirements.txt
```

## Example

```bash
$ python extract_image_data.py images data.csv
```

## How it works

Converts all images within **input_folder_path** into a CSV file located in **output_csv_path**.

- The **filename of the image** (without the extension) is stored in the first column.

- The **shape of the image data** is stored in the second column.

  - For black and white images, `rank = 2`.
  
  - For colored ones, `rank = 3` where the data is a matrix of RGB lists.

- Subsequent columns are the **feature columns** that encode color of each pixel.

## Multithreading

There will be `n_cores` number of threads, where `n_cores` is the number of cores in the CPU where the script is being run.
