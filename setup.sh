#!/bin/bash
set -e   

git submodule update --init --recursive


cd Franka-Teach
pip install -e .
pip install -r requirements.txt


cd RUKA
pip install -e .
pip install -r requirements.txt
cd ../..   

cd src/deoxys_control
pip install -e .
pip install -r requirements.txt
cd ../..   


