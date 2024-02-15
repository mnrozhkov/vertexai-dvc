# Vertex AI + DVC Example

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$PWD
```

## Run

```bash
dvc repro data                                  # Prepare features
dvc repro -s train_lr                           # Train only
dvc repro evaluate                              # Run downstream stages
```
