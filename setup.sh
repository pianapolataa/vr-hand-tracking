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

echo ">>> 安装 deoxys_control"
cd src/deoxys_control
pip install -e .
pip install -r requirements.txt
cd ../..   


