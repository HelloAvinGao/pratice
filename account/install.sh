#!/usr/bin/env bash
sudo apt install -y python37
sudo apt install -y python3-pip
sudo yum install -y python37
sudo yum install -y python3-pip
curl -LO https://files.pythonhosted.org/packages/e9/0f/b1aaf961980d5ea94243f28f91d3f6fc6f3b7e5047a9b8dc037541c2cc11/numpy-1.18.0-cp37-cp37m-win_amd64.whl
pip3.7 install numpy-1.15.0rc1+mkl-cp37-cp37m-win_amd64.whl