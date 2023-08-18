# Simple-Projects

[Project 1 : Python to Jupyter Notebook Converter](Format_Changer)
[Project 2 : Picture Combiner](picture_combiner)

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
