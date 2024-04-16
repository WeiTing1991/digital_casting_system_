# **Digital Casting System**

![GitHub - License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.10-blue)
![Conda Version](https://img.shields.io/badge/Anaconda-4.14.0-blue)


**Digital Casting System (DCS)** is a Innosuisse project as well as a new novel approach for [Smart Dynamic Casting(SDC)]().
This package works to transition automated digital casting systems from the laboratory to the industry scale by
overcoming the challenges addressed by inline mixing. DCS involves identifying optimal values for comprehensive system
parameters, including processing and material characteristics, while carefully considering specific system requirements.

## __Requirements__
* [Windows 10]()
* [Debian 12]()
* [TwinCAT](https://www.beckhoff.com/en-en/products/automation/twincat/?pk_campaign=AdWords-AdWordsSearch-TwinCAT_EN&pk\
_kwd=twincat&gclid=Cj0KCQjw9ZGYBhCEARIsAEUXITW5dmPmQ2629HIuFY7wfbSR70pi5uY2lkYziNmfKYczm1_YsK4hhPsaApjyEALw_wcB)
* [Anaconda 3](https://www.anaconda.com/)
* [Docker]()
* [ABB RobotStudio]()

## __Package Version__

## __Installation__

### Anaconda 3 on Windows 11

```bash
# Create the environment and activate it
conda create -n dcs python=3.10

# Install dependencies
conda activate dcs
pip install -r requirements.txt

# Clone the repository
git clone https://github.com/USI-FMAA/digital_casting_system.git
git pull --recurse-submodules
```


<!-- ### Virtualenv option 2 on Debian 12 -->
<!---->
<!-- ```bash -->
<!-- # Install venv -->
<!-- sudo apt install python3-venv -y -->
<!---->
<!-- # Clone repos and create the environment -->
<!---->
<!-- mkdir myfolder -->
<!-- cd myfolder -->
<!---->
<!-- git clone https://github.com/USI-FMAA/digital_casting_system.git -->
<!---->
<!-- python3.10 -m venv env -->
<!---->
<!-- Install dependencies -->
<!---->
<!-- source env/bin/activate -->
<!-- which python3 -->
<!---->
<!-- pip3 install -r requirements.txt -->
<!---->

### Concrete Controller

The sub-package `external_controllers` is a package that provides a set of driver to control the concrete casting machines.
More information can be found in [digital casting system controller]()

## Credits
This package was created by [WeiTing Chen](https://github.com/WeiTing1991)
at [USI-FMAA](https://github.com/USI-FMAA) and [ETHZurich DFab](https://dfab.ch/)



