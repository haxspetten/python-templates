# python-templates
Templates for python projects intended as an introduction for begginer python programmers

# Installing a development environment
For the suggested development environment the following tools are going to be used:
 - [WSL](https://docs.microsoft.com/en-us/windows/wsl/) (Windows Subsystem for Linux)
 - [Python3](https://python.land/)
 - [Visual Studio Code](https://code.visualstudio.com/) ([IDE](https://en.wikipedia.org/wiki/Integrated_development_environment))
 - [Git](https://git-scm.com/) ([version control](https://en.wikipedia.org/wiki/Version_control))

To start, it is recommended to install WSL since the installation of some of the other tools, if one chooses, can be done through WSL. It is not strictly required to install WSL, it is possible to use Windows Powershell, but it is recommended since Linux is great!
Since everything in this template project is written in it, python is needed. Specifically python3 is used (as opposed to python2, which is soon&trade; no longer maintained).  
For the integrated development environment (IDE), Visual Studio Code is recommended. There are many options for IDEs, but VScode is free, modern, widely used and just excellent.
Finally the version control of the project (and github) is managed with Git which is the industri standard.

## Install Windows Subsystem for Linux
The Windows Subsystem for Linux (WSL) lets developers run a GNU/Linux environment -- including most command-line tools, utilities, and applications -- directly on Windows.  
Install either WSL1 or WSL2 (or both), for enabling working in a Linux environment both will suit fine.  
WSL2 will increase file system performance and and system call compatibility but may force you to enable additional virtualization features in your bios, i.e. it may be a bit more complicated to install.
However you choose, [follow the installation instructions here](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Install Python3
Follow the instructions for installing the latest version of python [found here](https://python.land/installing-python).

### Installing virtualenv
virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. It is not preinstalled so it has to be manually installed. Open a terminal windows and run:

```bash
python3 -m pip install --user virtualenv
```
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

## Install Visual Studio Code
Follow the instructions on the [official download site](https://code.visualstudio.com/download).
### Suggested VS Code extensions

- [Remote WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) lets you use VS Code in WSL just as you would from Windows.
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) provides a feature rich environment for Python.

## Install Git
Follow the instructions on the official [getting started with Git site](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Note that the Linux commands for installing Git can be performed in WSL.

### Configuring Git
If you want to collaborate using Git some configurations are needed for you to be able to, for example, push to a remote repo. 
This is a first time setup but it can be re-configured at any time.   
Open a terminal and run the following and replace the content with the "<>" as appropriate:
```bash
git config --global user.name "<my-name-or-alias>"
git config --global user.email <johndoe@example.com>
```

An additional option if you want to use Visual Studio Code as your default Git editor (if you did not do so during installation):
```bash
git config --global core.editor "code --wait"
```
To check your configuration either run:
```bash
git config --list
```
or read the global Git configuration file directly. First find out where it is located
```bash
git config --list --show-origi
```
and then simply open it.