#!/bin/bash

echo "Setting up dependencies from boostrap.sh"
sudo apt-get -y update

# My tools for editing and playing with code
sudo apt-get install -y IPython
sudo apt-get install -y vim

# Install other package managers
sudo apt-get install -y python-pip

# Installing sklearn is a chore! This is all for stack finding
sudo apt-get install -y python-dev  # necessary for compiling against Python.h
sudo apt-get install -y python-numpy  # for stack finding
sudo apt-get install -y python-scipy # for stack finding
sudo apt-get install -y python-sklearn

echo 'Done installing packages!'
