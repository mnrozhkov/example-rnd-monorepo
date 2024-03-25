# Example for R&D repository structure

## Installation

```bash
python -m venv .venv
echo "PYTHONPATH=$PWD" > .venv/bin/activate
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

To run the pipeline, execute the following command:

```bash
dvc exp run
```

Run a separate stage with `-s` flag:

```bash
dvc exp run -s train_randomforest
```
