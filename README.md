# Dartboard
CS Project from university 2021 to develop a dartboard game with proper scoring mechanics.

# Getting Started

For Specific notes on individual features, see the `docs/` directory. For instructions on
how to begin development, see below!

## Tools

- [Python &gt;3.7](https://www.python.org/downloads/)
- [Pycharm IDE](https://www.jetbrains.com/pycharm-edu/)

## Setup

Once you have the project cloned to your computer and have downloaded both of the tools mentioned above, complete the
following steps.

- Configure a virtual environment for your work.
  - Open Pycharm
  - Type `ctrl + alt + s` then select your project and then Python Interpreter
  - Click the settings gear and select "Add"
  - Check that everything makes sense on this page. The default settings should work. Pay careful attention to the
    python path.
  - Select Ok. If you have any open terminals inside PyCharm, you will need to restart these for them to take effect
- Right click on the `dartboard` directory, then select `Mark Directory as` and then select `Sources Root`
  - Note, if the folder is blue, this has already been done for you automatically
- Install required packages. use the following command in the top level directory of this project to do this:
  - `python -m pip install -r requirements.txt`

## Running the project

The whole program should be kicked off from `dartboard/dartboard_main.py`. You can run the program by directly calling
that file with python, or by calling `run.bat` or `run.sh` (depending on your Operating System). The Database should
be automatically generated and updated for you, and the application window(s) will open. (Note:
these scripts should be called from inside your virtual environment)
