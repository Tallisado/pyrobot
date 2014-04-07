#!/bin/sh

cwd=$(pwd)

echo "Pyrobot"
git add -A; git commit -am 'automatically publishing and installing (Pyrobot)'
git push

echo "PyroLibrary"
cd ../pyrolibrary
pip uninstall git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary
git add -A
git commit -am 'automatically publishing and installing (PyroLibrary)'
git push
pip install git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary

echo "PyroFactory"
cd ../pyrofactory
pip uninstall git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory
git add -A
git commit -am 'automatically publishing and installing (PyroFactory)'
git push
pip install git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory

cd cwd