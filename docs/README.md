# Auto PyPi Uploader

## Table of Contents

- [Introduction](#introduction)
- [Uses](#uses)
    - [Running from Command Line](#running-from-command-line)
    - [Running with Command Line Arguments](#running-with-command-line-arguments)
    - [Importing as a Module](#importing-as-a-module)
        - [Installing with pip](#installing-with-pip)
        - [`create_setup()`](#create_setup-takes-in)
        - [`set_login()`](#set_login-takes-in)
        - [`pypi_upload()`](#pypi_upload-takes-in)
- [Running](#running)
    - [Dependencies](#dependencies)
    - [Setting Up .env File](#setting-up-env-file)
    - [Running](#running-1)
- [Quality Assurance](#quality-assurance)
- [Suggestions](#suggestions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

While working on my previous project: [text-excuse-generator](https://github.com/Huckdirks/text-excuse-generator), I just published my first package to [PyPi](https://pypi.org/project/text-excuse-generator/). I quickly realized that I wasn't going to be able to remember the command line arguments to pass into the required fields, and that I was bound to forget to change the version manually in the `setup.py` file every time I updated the package. So I decided to make a program that would automatically update the version number in the `setup.py` file and export a project to [PyPi](https://pypi.org/). I also added another script that would automatically create a `setup.py` file for me with the required fields.

## Uses

There are three main ways to interact with the program: by [running it in the command line](#running-from-command-line), by [running it with command line arguments](#running-with-command-line-arguments), or by [importing as a module](#importing-as-a-module) into another python file.

In order for this program to run, your project's directory must be set up as such:

**Any files and directories in [ ]'s are optional, but highly recommended!!!**
```
project_root_dir/

    pypi_uploader.py (can be downloaded from auto_pypi_uploader/ or substituted with a program that imports the module)
    setup.py (can be created with pypi_uploader.py or setup_file_creator.py)
    [README.md] (can also be in docs/)
    [LICENSE]

    main_module_name/
            __init__.py
            (other python files...)

    [docs/]
            [README.md]
```


You can also have multiple modules in the same directory, or even multiple modules within a module, but you will need to add the `__init__.py` file to each directory that contains a module. e.g.:
```
project_root_dir/

    pypi_uploader.py (can be downloaded from auto_pypi_uploader/ or substituted with a program that imports the module)
    setup.py (can be created with pypi_uploader.py or setup_file_creator.py)
    [README.md] (can also be in docs/)
    [LICENSE]

    main_module_name/
            __init__.py
            (other python files...)
            main_submodule_name/
                    __init__.py
                    (other python files...)

    secondary_module_name/
            __init__.py
            (other python files...)

    [docs/]
            [README.md]
```

### Running from Command Line

I'd recommend downloading [pypi_uploader.py](../include/pypi_uploader.py) from [include](../include/pypi_uploader.py) into a project's [root directory](../) if you want the functionality of the whole module, or just [`setup_file_creator.py`](../auto_pypi_uploader/setup_file_creator.py) if you only want to make a `setup.py` file. You can run the program by typing:
```bash
python3 pypi_uploader.py
```

When you run the program normally, it will first check if a `setup.py` file exists in the current directory. If it doesn't, it will then run [`setup_file_creator`](../auto_pypi_uploader/setup_file_creator.py)`.create_setup()`, which will ask you for:
- The Project's Name
- The Project's Version
- The Project's Author
- The Project's Description

And ask you if you want to add these optional fields:
- The Project's License
- The Project's Long Description Type (From [README.md](README.md))
- The Project's URL
- The Required Packages
- Keywords
- Classifiers
- Minimum Python Version

*If you just want to create a `setup.py` file, run:*
```bash
python3 setup_file_creator.py
```


If a `setup.py` file already exists, [`pypi_uploader.py`](../auto_pypi_uploader/pypi_uploader.py) will then ask you for a new version number, and update it in `setup.py`. It will then upload the package to [PyPi](https://pypi.org/). If you haven't already set up your login credentials, it will then ask you for your username and password & save it, and then proceed to upload the package. It then automatically updates/installs the package with `pip3 install --upgrade {project_name}`.

The program runs: `python3 setup.py sdist bdist_wheel` and `python3 twine upload dist/* -u "{USERNAME}" -p "{PASSWORD}"` to upload the package to [PyPi](https://pypi.org/).

### Running with Command Line Arguments

You can also run the program with command line arguments. All command line arguments longer than a single word need to be in parentheses. I'd recommend downloading [`pypi_uploader.py`](../auto_pypi_uploader/pypi_uploader.py) into a project's [root directory](../) if you want all the functionality, or just [`setup_file_creator.py`](../auto_pypi_uploader/setup_file_creator.py) if you only want to make a `setup.py` file, and running them from the command line. Please also include the [LICENSE](../LICENSE) file in the same directory as any files you add from [this project](https://github.com/Huckdirks/auto-pypi-uploader).

#### **Creating a `setup.py` File**

If you want to create a `setup.py` file, run:
```bash
python3 setup_file_creator.py --name PROJECT_NAME --version VERSION --author AUTHOR --description DESCRIPTION [--license LICENSE] [--long_description_content_type LONG_DESCRIPTION_TYPE] [--url URL] [--install_requires "INSTALL_REQUIRES"] [--keywords "KEYWORDS"] [--classifiers "CLASSIFIERS"] [--python_requires PYTHON_REQUIRES]
```
Any parameters in [ ]'s are optional, and all parameters in " "'s can be a comma separated list: e.g.
```bash
python3 setup_file_creator.py -n auto_pypi_uploader -v "1.0.0" -a "Huck Dirksmeier" -d "A program to automate the creation of the 'setup.py' file, changing a pip package's version, & publishing it to PyPi." -l MIT -ld text/markdown -u https://github.com/Huckdirks/auto-pypi-uploader -i "twine, python-dotenv" -k "PyPi, Pip, setup, setup.py, automation" -c "Programming Language :: Python, License :: OSI Approved :: MIT License, Operating System :: OS Independent" -p ">=3.8"
```

#### **Uploading [PyPi](https://pypi.org/) Package & Adding Login Information**
If you want to upload a package to [PyPi](https://pypi.org/), run:
```bash
python3 pypi_uploader.py VERSION [--user USERNAME PASSWORD]
```
e.g.
```bash
python3 pypi_uploader.py "1.0.0" -u Huckdirks PASSWORD
```
This assumes that you've already made a `setup.py` file. If you just want to update the version number, run `python3 pypi_uploader.py VERSION`. This assumes that you've already set up your login credentials. To just add login credentials, run `python3 pypi_uploader.py --user USERNAME PASSWORD`. This will add your username and password to a `.env` file in the current directory. If you decide to update the version & login information in a single call, **make sure the version is the first argument!** **YOU ONLY NEED TO ADD YOUR LOGIN INFORMATION ONCE, OTHERWISE IT WILL OVERRIDE THE PREVIOUS LOGIN INFORMATION!!!**

### Importing as a Module

You can also import the program as a module into another python file.

#### Installing with pip

Simply run:
```bash
pip install auto-pypi-uploader
```
 The `auto_pypi_uploader` module has  two sub-modules:
- `setup_file_creator` has one function: [`create_setup()`](#create_setup-takes-in)
- `pypi_uploader` has two functions: [`pypi_upload()`](#pypi_upload-takes-in) and [`set_login()`](#set_login-takes-in)

To import the modules into your python file, put this at the top of your file:
```python
from auto_pypi_uploader.pypi_uploader import *
from auto_pypi_uploader.setup_file_creator import *
```
Or you can import the individual functions.

#### `create_setup()` takes in:
```python
create_setup(NAME: str, VERSION: str, AUTHOR: str, DESCRIPTION: str, help: bool, license: str, long_description_content_type: str, url: str, install_requires: list[str], keywords: list[str], classifiers: list[str], python_requires: str) -> bool
```
`create_setup()` returns True if able to generate `setup.py` and False if not. **All uppercase parameters are required if parameters are passed in, and each parameter must be defined in the function call. You can also omit all parameters, and the function will prompt you for each one manually.**

If you want to create a `setup.py` file, call the function like this:
```python
create_setup(name = "auto_pypi_uploader", version = "1.0.0", author = "Huck Dirksmeier", description = "A program to automate the creation of the 'setup.py' file, changing a pip package's version, & publishing it to PyPi.", license = "MIT", long_description_content_type = "text/markdown", url = "https://github.com/Huckdirks/auto-pypi-uploader", install_requires = ["twine", "python-dotenv"], keywords = ["PyPi", "Pip", "setup", "setup.py", "automation"], classifiers = ["Programming Language :: Python", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"], python_requires = ">=3.8")
```
Make sure to put the fields before the variables when calling the function.

#### `set_login()` takes in:
```python
set_login(USERNAME: str, PASSWORD: str) -> None
```
If you want to set up your .env file, call `set_login()` like this:
```python
set_login("USERNAME", "PASSWORD")
```
If you want user input, just call [`pypi_upload()`](#pypi_upload-takes-in).

#### `pypi_upload()` takes in:
```python
pypi_upload(VERSION: str, username: str, password: str) -> bool
```
`pypi_upload()` returns True if the package was successfully uploaded, and False if it wasn't. **All uppercase parameters are required if parameters are passed in, and each parameter must be defined in the function call. You can also omit all parameters, and the function will prompt you for the version, and the login info if not previously saved.**
If you want to upload a package & login to [PyPi](https://pypi.org/), call `pypi_upload()` like this:
```python
pypi_upload(version = "0.0.0", username = "USERNAME", password = "PASSWORD")
```

## Running

### Dependencies

#### Accounts

You'll need to create a [PyPi](https://pypi.org/account/register/) account. Once you get your account set up, you'll need to [set up the `.env` file](#setting-up-env-file) with this information:
- Username
- Password

#### Install Dependencies

Double click [`dependencies`](../dependencies), or run `bash `[`dependencies`](../dependencies) or `./`[`dependencies`](../dependencies) in the command line in the root directory to install the python dependencies. You must have [pip](https://pip.pypa.io/en/stable/installation/) installed to download the new dependencies. Also, you'll need to install [python](https://www.python.org/downloads/) yourself if you haven't already.

**[List of Dependencies](DEPENDENCIES.md)**

### Setting Up .env File

Either run the program without any arguments to manually input the information for the .env file, run with [command line arguments](#setting-up-env-file) to automatically input the information for the .env file, or pass in the correct parameters to the [`set_login()`](#set_login-takes-in) or [`pypi_upload()`](#pypi_upload-takes-in) function.

### Running

**YOU HAVE TO INSTALL THE DEPENDENCIES & SETUP THE `.env` FILE BEFORE TRYING TO RUN THE PROGRAM!!!**
If installed with pip, all dependencies should be installed automatically!

Run [`python3 pypi_uploader.py`](#running-from-command-line) or [`python3 pypi_uploader.py VERSION [--user USERNAME PASSWORD]`](#running-with-command-line-arguments) in the command line in the source directory.

More detailed instructions are in the [Uses](#uses) section.

## Quality Assurance
All variable, function, class, module, & file names are written in [snake_case](https://en.wikipedia.org/wiki/Snake_case) to make sure everything is consistent, and all `const` variables are written in ALL-CAPS. The code is also quite commented and the variable names are quite verbose, so it should be easy enough to understand what's going on.

If there are any other/better ways to check for quality assurance, please let me know in the [suggestions](https://github.com/Huckdirks/auto-pip-exporter/discussions/new?category=suggestions)!

## Suggestions

If you have any suggestions about anything, please create a [new discussion in suggestions](https://github.com/Huckdirks/auto-pip-exporter/discussions/new?category=suggestions).

## Contributing

Contributions are always welcomed! Look at [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License

The project is available under the [MIT](https://opensource.org/licenses/MIT) license.
