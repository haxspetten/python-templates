# Project template number 1
The overview file structure of this project looks like the following:
```
.
├── package
│   ├── __init__.py
│   └── module1.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_package.py
```

The project template consist of a python package with one module.  
The module of the package is tested in the test located in tests.  
The requirements.txt file lists any packages not available in the default python installation but are required for the project. It is used to set up the projects virtual working environment.

## Prerequisites before working
Before starting work with this template, the virtual python environment needs to be activated.

Run all these command from the top-level of the project-template directory, i.e. /python-templates/project-template-1.  
Create the virtual environment:
```bash
python3 -m venv venv
```

Activate the virtual environment:
```bash
source venv/bin/activate
```

Install the required packages for the project:
```bash
pip install -r requirements.txt
```

To deactivate the virtual environment, simply run:
```bash
deactivate
```

## Running the tests
To run the tests, navigate to the project-template-1 directory and run:
```bash
python -m unittest discover tests/
```