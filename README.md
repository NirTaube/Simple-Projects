# Simple-Projects

- [Project 1 : Python to Jupyter Notebook Converter](Format_Changer)
- [Project 2 : Image Combination Scripts](Image_combination)

---

  ## Python to Jupyter Notebook Converter
  
  This utility allows you to convert Python `.py` scripts into Jupyter Notebook `.ipynb` files. It's particularly useful if you have Python code that you'd like to present or share in a more interactive format, like Jupyter Notebooks.
  
### Requirements
- Python
- `nbformat` package. You can install it using pip:
  ```bash
  pip install nbformat
  ```

### Usage
  Run
  ```python
   format_changer.py
  ```
- You'll be prompted to provide the path to the .py file. If you're running this script outside of the folder containing the file you want to convert, provide the full path. Otherwise, just the filename will suffice.

- Next, you'll be prompted to provide a name or path for the resulting .ipynb file.

- The script will notify you once the conversion is successful.

### <span style="color:orange">**How It Works**</span>
The script reads the provided .py file and divides it into sections based on two consecutive newlines. Each of these sections becomes a separate cell in the Jupyter Notebook.

### Caution
Ensure that the source .py file exists in the specified path to avoid any FileNotFoundError.
This script assumes two consecutive newlines as a delimiter for separate cells in the Jupyter Notebook. Adjust the content of your .py file accordingly if needed.

Contributing
Feel free to report any issues or submit pull requests. Contributions are welcome!
---

# Image Combination Scripts
A collection of scripts that allow you to combine two images. These scripts support SVG, JPEG, and PNG formats.

### Table of Contents
- [SVG Combiner](SVG Combiner)
- [JPEG Combiner](JPEG Combiner)
- [PNG Combiner](PNG Combiner)

### Usage

## SVG Combiner
The SVG combiner takes two SVG files and merges their content into a single SVG file.

## JPEG Combiner
The JPEG combiner allows you to combine two JPEG images either horizontally (side-by-side) or vertically (stacked one on top of the other).

## PNG Combiner
The PNG combiner works similarly to the JPEG combiner, with the added support for PNG's transparency features.


### SVG
```python
python svg_combiner.py
```
It will prompt you for the paths to the two SVG files you want to combine.

### JPEG
```python
python jpeg_combiner.py
```

It will prompt you for:
- The path to the first JPEG file.
- The path to the second JPEG file.
- The desired orientation: 'horizontal' for side-by-side or 'vertical' for one on top of the other.
- The path where the combined JPEG should be saved or if you are running this in the same folder you can just write the name and '.jpeg' .

### PNG
```python
python png_combiner.py
```

It will prompt you for:
- The path to the first PNG file.
- The path to the second PNG file.
- The desired orientation: 'horizontal' for side-by-side or 'vertical' for one on top of the other.
- The path where the combined PNG should be saved or if you are running this in the same folder you can just write the name and '.png'.
