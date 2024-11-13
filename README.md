# **Digital Casting System**

<!-- PROJECT SHIELDS -->

![GitHub - License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.10-blue)
![Conda Version](https://img.shields.io/badge/Anaconda-4.14.0-blue)

**Digital Casting System (DCS)** is a Innosuisse project as well as a new novel approach for [Smart Dynamic Casting(SDC)]().
This package works to transition automated digital casting systems from the laboratory to the industry scale by
overcoming the challenges addressed by inline mixing. DCS involves identifying optimal values for comprehensive system
parameters, including processing and material characteristics, while carefully considering specific system requirements.

This package has three parts, which contain ```PLC controller``` for control compenments, ```DCS library``` for middleware, robotic control, and data handling; lastly, ```DCS application``` uses for realtime data recoding and production simulation.


- [X] PLC controller driver package
- [ ] DCS library
- [ ] DCS application for grahic real-time data recording


## Requirements

Operating System and Software.
- [Windows 10/11] or [Ubuntu 22.04]
- [TwinCAT 3]
- [Anaconda 3]
- [Docker]

CAD/CAM software and Simulation.
- [ABB RobotStudio]
- [Rhino and Grasshopper]


<!--link:-->
[Windows 10/11]: https://www.microsoft.com/en-us/windows/
[Ubuntu 22.04]: https://ubuntu.com/download/desktop
[TwinCAT 3]: https://www.beckhoff.com/en-en/products/automation/twincat/?pk_campaign=AdWords-AdWordsSearch-TwinCAT_EN&pk_kwd=twincat&gclid=Cj0KCQjw9ZGYBhCEARIsAEUXITW5dmPmQ2629HIuFY7wfbSR70pi5uY2lkYziNmfKYczm1_YsK4hhPsaApjyEALw_wcB
[Anaconda 3]: https://www.anaconda.com/
[Docker]: https://www.docker.com/
[ABB RobotStudio]: https://new.abb.com/products/robotics/robotstudio
[Rhino and Grasshopper]: https://www.rhino3d.com/download


## Getting Started

```bash
# Clone the repository
git clone https://github.com/USI-FMAA/digital_casting_system.git
```

```bash
# Update the submoudles
git submodule init
cd external_controllers
git checkout master # checkout the lastest version
git pull

# Alneratively way
git submodule foreach git pull origin master

# Update the submoudles
git pull --recurse-submodules
```

```bash
# Setup the environment
# Create the environment and activate it
conda create --prefix ./.env python=3.10

# Install dependencies
conda activate ./.env
pip install -r requirements.txt

# Install compas framework
conda install compas
pip install git+git://github.com/WeiTing1991/compas_rrc.git@master
```

## Developer Installation

```bash
....
```

### PLC Controller

```bash
....
```

## Robot communication

### Real ABB robotic control

```bash
# docker compose up
# virtual controller
docker-compose -f .\external_controllers\robot\docker_compas_rrc\virtual_controller\docker-compose.yml up

# real controller
# clean the stopped container
docker container prune
# compose up and connect with docker container
docker-compose -f .\external_controllers\robot\docker_compas_rrc\real_controller\docker-compose.yml up
```

### Simulation with ABB robot

#### ABB RobotStudio

#### CAD/CAM software(Rhino and grasshopper)

<!-- ### Virtualenv (on MacOS\ Ubuntu 22.04) -->
<!---->
<!-- ```bash -->
<!-- # Install venv -->
<!-- sudo apt install python3-venv -y -->
<!---->
<!-- # Clone repos and create the environment -->
<!-- git clone https://github.com/USI-FMAA/digital_casting_system.git -->
<!-- git submodule update --init --recursive -->
<!---->
<!-- # Update the submoudles -->
<!-- git pull --recurse-submodules -->
<!---->
<!-- # Create the environment and activate it -->
<!-- python3.10 -m venv .env -->
<!---->
<!-- #Install dependencies -->
<!-- source ./.env/bin/activate -->
<!-- which python3 -->
<!---->
<!-- pip3 install -r requirements.txt -->
<!---->
<!-- ``` -->

## Concrete Controller

The sub-package `external_controllers` is a package that provides a set of driver to control the concrete casting machines.
More information can be found in [digital casting system controller](https://github.com/USI-FMAA/digital_casting_system_controller)


## Credits

This package was created by [WeiTing Chen](https://github.com/WeiTing1991)
at [USI-FMAA](https://github.com/USI-FMAA) and [ETHZurich DFab](https://dfab.ch/)
