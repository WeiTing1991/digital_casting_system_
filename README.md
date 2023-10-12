# **Digital Casting System**

![GitHub - License](https://img.shields.io/badge/License-MIT-blue.svg)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/COMPAS.svg)](https://pypi.python.org/project/COMPAS)
[![PyPI - Latest Release](https://img.shields.io/pypi/v/COMPAS.svg)](https://pypi.python.org/project/COMPAS)


Digital Casting System is a Innosuisse project and a new novel approach for Smart Dynamic Casting(SDC). 



## __Requirements__
---
* Windows 10 Pro
* [TwinCAT](https://www.beckhoff.com/en-en/products/automation/twincat/?pk_campaign=AdWords-AdWordsSearch-TwinCAT_EN&pk_kwd=twincat&gclid=Cj0KCQjw9ZGYBhCEARIsAEUXITW5dmPmQ2629HIuFY7wfbSR70pi5uY2lkYziNmfKYczm1_YsK4hhPsaApjyEALw_wcB)
* [Anaconda 3](https://www.anaconda.com/)
* [Docker]()
* [ABB RobotStudio]()

## __Package Version__


## __Installation__

### Anaconda 3 option 1

First step, add the conda-forge

```bash
conda config --add channels conda-forge
```
Create the envirment and activate it 

```bash
conda create -n dcs python = 3.10
```

Install depenedencies

```bash 
conda activate dcs  
pip install -r requirements.txt 

```

### Virtualenv option 2 in Ubuntu 22.04

Install Virtualenv

```bash
sudo apt install python3-venv -y

```
Clone repos and create the envirment

```bash
mkdir myfolder 
cd myfolder

git clone https://github.com/USI-FMAA/digital_casting_system.git

python3.10 -m venv env
```

Install depenedencies

```bash 
source env/bin/activate
which python3

pip3 install -r requirements.txt 

pip3 list 
```

### Concrete Controller 

<!-- ```bash

```
- Devices
    - TBC -->


<!-- ### Arduino temperature sensor Kit 

```bash
pip install pyserial

```
- Devices
    - Sensor DS18B20
    - Arduino UNO
    - LCD DISPLAY 2X16, 1602 DRIVER, I2C
    - UBS cable  -->


## Credits
This package was created by WeiTing Chen [`@WeiTing1991`](https://github.com/WeiTing1991) at USI-FFMA and ETHZurich. 
