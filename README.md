# **Digital Casting System**

<!------link:---------->
[Windows 10]: https://www.microsoft.com/en-us/windows/
[Ubuntu 22.04]: https://ubuntu.com/download/desktop
[TwinCAT 3]: https://www.beckhoff.com/en-en/products/automation/twincat/?pk_campaign=AdWords-AdWordsSearch-TwinCAT_EN&pk_kwd=twincat&gclid=Cj0KCQjw9ZGYBhCEARIsAEUXITW5dmPmQ2629HIuFY7wfbSR70pi5uY2lkYziNmfKYczm1_YsK4hhPsaApjyEALw_wcB
[Anaconda 3]: https://www.anaconda.com/
[Docker]: https://www.docker.com/
[ABB RobotStudio]: https://new.abb.com/products/robotics/robotstudio
[Rhino and Grasshopper]: https://www.rhino3d.com/download


<!-- PROJECT SHIELDS -->

![GitHub - License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.10-blue)
![Conda Version](https://img.shields.io/badge/Anaconda-4.14.0-blue)
![UV Version](https://img.shields.io/badge/UV-0.6.0-blue)
![ABB Version](https://img.shields.io/badge/RobotStudio-2023/2024-blue)
![TwinCAT Version](https://img.shields.io/badge/TwinCAT-3.4-blue)
![Docker Version](https://img.shields.io/badge/Docker-23.0.3-blue)

<!-- PROJECT DESCRIPTION -->

**Digital Casting System (DCS)** is a Innosuisse project as well as a new novel approach for [Smart Dynamic Casting(SDC)]().
This package works to transition automated digital casting systems from the laboratory to the industry scale by
overcoming the challenges addressed by inline mixing. DCS involves identifying optimal values for comprehensive system
parameters, including processing and material characteristics, while carefully considering specific system requirements.

This package has three parts, which contain ```PLC controller``` for control components, ```DCS library``` for middleware, robotic control, and data handling; lastly, ```DCS application``` uses for real-time data recording and production simulation.


<!-- PROJECT REQUIREMENTS -->

## Requirements

Operating System and Software.

- [Windows 10]* or [Ubuntu 22.04]*
- [TwinCAT 3] -- version 3.4
- [Docker]  -- version
- [Anaconda 3] # change to uv soon.

CAD/CAM software and simulation.

- [ABB RobotStudio] -- version 2023/2024
- [Rhino and Grasshopper] -- version 7


<!-- PROJECT Getting Started -->

## Getting Started
Data visualization and real-time monitoring app
Please find the app [here](https://github.com/USI-FMAA/digital_casting_system_app)


<!-- PROJECT USAGE -->
## Usage

> [!NOTE]
> Don`t have to run the programming only for data recording.

### Real-time monitoring and data recording

``` bash
# sync the library
uv sync

# run the script
uv run scripts/dcs.py
```

### PLC Controller

Please find more information [here](https://github.com/USI-FMAA/digital_casting_system_controller.git) under **Connect with TwinCAT** section.

### Robot communication
>[!NOTE]
> Only if we want to run with the robot script

#### Real ABB robotic control
TODO: TEST

```sh
docker
# real controller
# clean the stopped container
docker container prune
# compose up and connect with docker container

# Linux/WSL
docker-compose -f ./external_controllers/robot/docker_compas_rrc/real_controller/docker-compose.yml up
```

```sh
docker
# real controller
# clean the stopped container
docker container prune
# compose up and connect with docker container

# Linux/WSL
docker-compose -f ./external_controllers/robot/docker_compas_rrc/real_controller/docker-compose.yml up
```

```pwsh
# windows
docker-compose -f .\external_controllers\robot\docker_compas_rrc\real_controller\docker-compose.yml up
```

```pwsh
# windows
uv run scripts/main_run_robot.py
```

### Simulation with ABB robot

```sh
docker
# clean the stopped container
docker container prune
# docker compose up

# virtual controller
# Linux/WSL
docker-compose -f ./external_controllers/robot/docker_compas_rrc/real_controller/docker-compose.yml up
```

```pwsh
# windows
docker-compose -f .\external_controllers\robot\docker_compas_rrc\virtual_controller\docker-compose.yml up
```

#### ABB RobotStudio

Please find more information [here]()

#### CAD/CAM software(Rhino and grasshopper)

Please find more information [here]()

#### Concrete Controller

The sub-package `external_controllers` is a package that provides a set of driver to control the concrete casting machines.
More information can be found in [digital casting system controller](https://github.com/USI-FMAA/digital_casting_system_controller)


<!-- PROJECT DEVELOPMENT -->

## Development

### Clone the repository
```bash
git clone https://github.com/USI-FMAA/digital_casting_system.git
# Alternately
git clone --recurse-submodules https://github.com/USI-FMAA/digital_casting_system.git
```

```bash
# if the repository is already cloned
cd digital_casting_system
git submodule update --init --recursive
```


### Update the submodules

```bash
# Update the submoudles
git submodule update --remote --merge
git pull --recurse-submodules


# Alternately
git submodule init
cd external_controllers
git checkout master # checkout the lastest version
git pull

# Alternately way
git submodule foreach git pull origin master

```

### Setup the environment

With `UV` package manger (super fast package management build by rust)

#### Install UV
```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv --version
```

#### Create virtual environment

UV

``` bash
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e .

# optional
uv pip install '.[dev]' # install the development dependencies
uv pip install '.[docs]' # install the documentation dependencies

```

Alternately with Anaconda package manager

```sh
# Create the environment and activate it
conda create --prefix ./.env python=3.10

# Install dependencies
conda activate ./.env
pip install -r requirements.txt

# Install Compas framework
pip install compas
pip install git+git://github.com/WeiTing1991/compas_rrc.git@main
```

<!-- Misc -->

## Credits
Author: [Wei-Ting Chen](https://github.com/WeiTing1991)

This package created by [WeiTing Chen](https://github.com/WeiTing1991)
at [USI-FMAA](https://github.com/USI-FMAA) and [ETHZurich DFab](https://dfab.ch/)

## Features

- [X] PLC controller driver package
- [X] DCS library with real-time data recording
- [ ] DCS application for graphic real-time data recording application
