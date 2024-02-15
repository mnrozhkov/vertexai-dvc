# DVC Project Design Patterns (WIP)

## Introduction

Welcome to the "DVC Project Design Patterns" community project! This initiative is dedicated to exploring, documenting, and sharing best practices and design patterns for using [Data Version Control (DVC)](https://dvc.org/doc), an open-source tool for managing and versioning data and machine learning models.

### What You Will Find Here

- Design Pattern Catalogue: A collection of design patterns for common scenarios encountered in machine learning projects, such as handling large datasets, managing experiments, and parallel processing.
- Best Practices: Tips and tricks for optimizing DVC workflows, managing dependencies, and ensuring reproducibility.
- Real-World Examples: Practical implementations of these patterns in real-world projects, demonstrating their application and benefits.

### Who Should Participate

- Data Scientists & ML Engineers: Improve your workflow with efficient DVC practices.
- Team Leads & Managers: Understand how to structure ML projects for better manageability and collaboration.
- Open Source Enthusiasts: Contribute by sharing your own experiences, patterns, and best practices.

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
dvc repro -s train_rf & dvc repro -s train_lr   # Train models in parallel
dvc repro -s train_lr -f                        # Train only Linear Regression
dvc repro evaluate                              # Run downstream stages
```

