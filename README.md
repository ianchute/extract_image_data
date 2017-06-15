# extract_image_data
Multi-threaded script for converting images to CSV data

```
Usage: python extract_image_data.py <input_folder_path> <output_csv_path>
```

```
Example: python extract_image_data.py images data.csv
```

Converts all images within **input_folder_path** into a CSV file located in **output_csv_path**.

- The filename of the image is stored in the **id** column (without the extension).

- There will be **N feature columns** (feature_0, feature_1, ... feature_N) depending on the image size and color (RGB).

- Also there will be a **shape column** that describes the original shape of the image data.

For black and white images, rank = 2.

For colored ones, rank = 3 where the data is a matrix of RGB lists.
