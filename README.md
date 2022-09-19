# Giang Project

## Command

Required Anaconda or Miniconda installed.

Create a new virtual environment and install packages

```python
conda env create -f environment.yml
```

Update environment

```python
conda env update -f environment.yml --prune
```

To run

```python
python main.py -f [input.json] -o [output filename]
```

Add `--write-html` to write html file
