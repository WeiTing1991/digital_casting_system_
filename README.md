# **Digital Casting System**

<!-- PROJECT SHIELDS -->

![GitHub - License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.10-blue)
![Conda Version](https://img.shields.io/badge/Anaconda-4.14.0-blue)

**Digital Casting System (DCS)** is a Innosuisse project as well as a new novel approach for [Smart Dynamic Casting(SDC)]().
This package works to transition automated digital casting systems from the laboratory to the industry scale by
overcoming the challenges addressed by inline mixing. DCS involves identifying optimal values for comprehensive system
parameters, including processing and material characteristics, while carefully considering specific system requirements.

## Requirements

-   [Windows 10]()
-   [Debian 12]()
-   [TwinCAT](https://www.beckhoff.com/en-en/products/automation/twincat/?pk_campaign=AdWords-AdWordsSearch-TwinCAT_EN&pk_kwd=twincat&gclid=Cj0KCQjw9ZGYBhCEARIsAEUXITW5dmPmQ2629HIuFY7wfbSR70pi5uY2lkYziNmfKYczm1_YsK4hhPsaApjyEALw_wcB)
-   [Anaconda 3](https://www.anaconda.com/)
-   [Docker]()
-   [ABB RobotStudio]()

## Getting Started

```bash

```

## Developer Installation

### Anaconda 3 (on Windows 10)

```bash
# Clone the repository
git clone https://github.com/USI-FMAA/digital_casting_system.git
git pull --recurse-submodules

# Create the environment and activate it
conda create --prefix ./.env python=3.10

# Install dependencies
conda activate ./.env
pip install -r requirements.txt

# Install compas framework
conda install compas
pip install git+git://github.com/WeiTing1991/compas_rrc.git@master

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


## License

## Credits

This package was created by [WeiTing Chen](https://github.com/WeiTing1991)
at [USI-FMAA](https://github.com/USI-FMAA) and [ETHZurich DFab](https://dfab.ch/)
