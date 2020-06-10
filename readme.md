# Simple FastAPI calculator

Testing assignment for PulsuPro

## Getting Started

To use FastAPI calculator you need to provide several commands

* /add/3.3/2.1 will result addition
* /sub/5/2 will result subtraction
* /div/4/2 will result division
* /mult/2/2 will result multiplication

### Prerequisites

This program was written with Python, FastAPI and MongoDB on Ubuntu 18.04

Full list of extensions used and their versions you can find in the requirements.txt

### Installing

The best way to repeat installation process is to install Conda or MiniConda. Then you can recreate environment with provided requirements.txt

Create environment
```
conda create --name <environment-name> python=3.8 pip
```
Activate environment
```
conda activate <environment-name>
```
Install requirements
```
pip install -r requirements.txt
```
To properly install MongoDB on your system see their official site instructions.
* [MongoDB](http://mongodb.com/) - MongoDB is the noSQL database

## Running the tests

Tests are running with installed and activated MongoDB

