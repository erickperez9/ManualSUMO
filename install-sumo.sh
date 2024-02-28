#!/bin/bash

# Este script sirve para instalar SUMO a partir de la construccion de archivos binarios

echo =================== ACTUALIZACION DE PAQUETES ===================
sudo apt-get update

echo ================ INSTALACION DE LIBRERIAS (1/5) =================
sudo apt-get install git cmake python3 g++ libxerces-c-dev libfox-1.6-dev libgdal-dev libproj-dev libgl2ps-dev python3-dev swig default-jdk maven libeigen3-dev

echo ================ INSTALACION DE LIBRERIAS (2/5) =================
sudo apt-get install ccache libavformat-dev libswscale-dev libopenscenegraph-dev python3-pip python3-setuptools

echo ================ INSTALACION DE LIBRERIAS (3/5) =================
sudo apt-get install libgtest-dev gettext tkdiff xvfb flake8 astyle python3-autopep8 pip3 install texttest

echo ================ INSTALACION DE LIBRERIAS (4/5) =================
sudo apt-get install python3-pandas python3-rtree python3-pyproj

echo ================ INSTALACION DE LIBRERIAS (5/5) =================
sudo apt-get install python3-pyproj python3-rtree python3-pandas python3-flake8 python3-autopep8 python3-scipy python3-pulp python3-ezdxf



echo =================================================================
echo =================================================================
echo =================================================================

echo ================ DESCARGA DESDE EL REPOSITORIO  =================
git clone --recursive https://github.com/eclipse-sumo/sumo

echo ================ CAPTURA ADICIONAL (GIT FETCH) ==================
cd sumo
git fetch origin refs/replace/*:refs/replace/*

echo ================ INSTALACION DE LIBRERIAS (1/2) =================
pip install -r tools/requirements.txt

echo ================ INSTALACION DE LIBRERIAS (2/2) =================
sudo apt-get install python3-pandas python3-rtree python3-pyproj



# El ultimo paso es exportar la variable de entorno dentro de la carpeta de descarga de sumo, esto se logra con:
# export SUMO_HOME="$PWD"


# O agregando el siguiente comando al final de los archivos: /etc/bash.bashrc y /home/<user>/.bashrc
# export SUMO_HOME="/home/<user>/sumo-<version>"
