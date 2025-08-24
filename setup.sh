#!/bin/bash

# Do all the installation including for Franka-Teach in this repo

# Deoxys
git clone https://github.com/NYU-robot-learning/deoxys_control.git src/deoxys_control
cd src/deoxys_control/deoxys
./InstallPackage  # enter 0.13.3 for the frankalib version when prompted
make -j build_deoxys=1
python -m pip install -e .
python -m pip install -U -r requirements.txt
cd ../../..

# ReSkin
python -m pip install reskin_sensor

# Franka-Env
cd franka-env
python -m pip install -e .
cd ..

git submodule update --init --recursive

# Franka-Teach
cd Franka-Teach
pip install -e .
pip install -r requirements.txt


# RUKA (under Franka-Teach directory)
git clone --recurse-submodules https://github.com/joliachen/RUKA.git
cd RUKA
pip install -r requirements.txt
pip install -e .
cd ..

