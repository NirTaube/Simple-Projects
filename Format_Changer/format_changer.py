import nbformat as nbf

def py_to_ipynb(py_file, ipynb_file):
    with open(py_file, 'r') as f:
        code = f.read()

    # Create a new notebook
    nb = nbf.v4.new_notebook()

    # Split the code by sections (assuming two consecutive newlines as a delimiter) and add them to the notebook cells
    for section in code.split('\n\n'):
        nb['cells'].append(nbf.v4.new_code_cell(section))

    # Write the notebook to a file
    with open(ipynb_file, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

if __name__ == "__main__":
    source_py_file = input("Enter the path to the .py file if you are running this outside of the folder that contains the file needing to be converted.: ") 
    target_ipynb_file = input("Enter the desired name/path for the .ipynb file") 

    py_to_ipynb(source_py_file, target_ipynb_file)
    print(f"Converted {source_py_file} to {target_ipynb_file} successfully!")
