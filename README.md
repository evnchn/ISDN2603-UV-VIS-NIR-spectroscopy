# ISDN2603-IR-spectroscopy
IR spectroscopy CSV parsing and display

## Usage

1. Simply run the Python script and drop the files over to the command window.

Powered by [LinkStart.py](https://github.com/evnchn/linkstart.py), a lightweight dependency auto-installer. 

_You may use command-line parameter for easier specification of the file name, especially when the file is in the same directory of the script._

## Example

_First copy TPU.csv from RAMAN_DATA/Group1 folder to same directory of reader.py_

`py reader.py TPU.csv`

<img width="482" alt="image" src="https://github.com/evnchn/ISDN2603-Raman-spectroscopy/assets/37951241/ade23269-8cef-4f61-a216-cc785275a431">

## Converter usage

_Note: Not intended for end users._

1. Install `xlrd`, `openpyxl` and `pandas`

For converter_xls_RAMAN:

2. Put the `converter.py` in same directory as all the .xls files
3. Run `converter.py`

For converter_xlsx_FTIR:

2. Ensure run `xlsx_to_csv("[name].xlsx")` for the xlsx files for conversion in `converter_xlsx.py`
3. Run `converter_xlsx.py`
