# dec-pyc

A Python utility for decompiling Python bytecode (`.pyc`) files back to readable Python source code (`.py`).

It recursively searches through directories to find compiled Python files (`.pyc`) and decompiles them using the `uncompyle6` library. It preserves the original directory structure of the source folder in the destination folder.


## Prerequisites

You need to have `uncompyle6` installed

```
pip install uncompyle6
```

## Usage
Clone this repo or download the dec_py.py file

In dec_pyc.py, add this after the function definition:
```python
decompile_pyc_files('source-path', 'output-path')
```

## To-do 
Make this a script