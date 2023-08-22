# Image Combination Scripts
A collection of scripts that allow you to combine two images. These scripts support SVG, JPEG, and PNG formats.

## Product (Python + Jupyter logos)
![Combined SVG](https://raw.githubusercontent.com/NirTaube/Simple-Projects/2539f278d9c025bdc99cad270d80d771ecb20db9/Image_combination/combined2.svg)


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
