#!/bin/sh

cwd=$(pwd)

if [ "$1" = "all" ]
then
    echo "ALL"
	echo "Pyrobot"
	git add -A
	git commit -am 'automatically publishing and installing (Pyrobot)'
	git push

	echo "PyroLibrary"
	cd ../pyrolibrary
	/usr/bin/yes | pip uninstall git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary
	git add -A;	git commit -am 'automatically publishing and installing (PyroLibrary)';	git push
	pip install git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary

	echo "PyroFactory"
	cd ../pyrofactory
	/usr/bin/yes | pip uninstall git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory
	git add -A; git commit -am 'automatically publishing and installing (PyroFactory)'; git push
	pip install git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory	

elif [ "$1" = "library" ]
then
	echo "PyroLibrary"
	cd ../pyrolibrary
	/usr/bin/yes | pip uninstall git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary
	git add -A; git commit -am 'automatically publishing and installing (PyroLibrary)'; git push
	pip install git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary

elif [ "$1" = "factory" ]
then
	echo "PyroFactory"
	cd ../pyrofactory
	/usr/bin/yes | pip uninstall git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory
	git add -A; git commit -am 'automatically publishing and installing (PyroFactory)'; git push
	pip install git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory	

elif [ "$1" = "bot" ]
then
	echo "Pyrobot"
	git add -A; git commit -am 'automatically publishing and installing (Pyrobot)'
	git push
	
elif [ "$1" = "pip" ]
then	
	echo "PIP ONLY"
	/usr/bin/yes | pip uninstall git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary
	pip install git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary
	/usr/bin/yes | pip uninstall git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory
	pip install git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory
else
	echo "USAGE: "
	echo "#pyrobot> ./publish_and_install_assets.sh [all|pip|bot|library|factory]"
fi