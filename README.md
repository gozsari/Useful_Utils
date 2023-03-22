# Useful_Utils
![Linux](https://svgshare.com/i/Zhy.svg)
![version](https://img.shields.io/badge/version-1.0-blue)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Python](https://img.shields.io/badge/python-v3.10-red)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Tools facilitate your work
### 1- Extracting the table from the PDF files:
- You can extract the table from the PDF files using the `extract_pdf_tables.py` file.
- Input files should be located in the **input** directory.
- Usage: `python extract_pdf_tables.py --pdf_file <input_file> --page_no <page_number_in_pdf> --table_no <table_number_in_page>`
- Example: `python extract_pdf_tables.py --pdf_file "test.pdf" --page_no 1 --table_no 1`
- Output: `table1.csv` and `table1.xlsx` files will be created in the **output** directory.


