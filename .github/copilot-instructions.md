# Copilot Instructions for Digital Casting System (DCS)

## Repository Overview

The **Digital Casting System (DCS)** is an Innosuisse project implementing a novel approach for Smart Dynamic Casting (SDC). This system automates digital casting processes from laboratory to industry scale, focusing on inline mixing optimization and real-time parameter control.

## Key Components

### Core Architecture
- **PLC Controller**: Component control using TwinCAT 3.4
- **DCS Library**: Middleware for robotic control and data handling
- **DCS Application**: Real-time data recording and production simulation

### Technology Stack
- **Language**: Python 3.10+
- **Package Manager**: UV (preferred) or Anaconda
- **Automation**: TwinCAT 3.4 for PLC control
- **Robotics**: ABB RobotStudio integration with COMPAS RRC
- **CAD/CAM**: Rhino 7 and Grasshopper workflows
- **Containerization**: Docker for robot controllers
- **Documentation**: MkDocs with Material theme

## Project Structure

```
src/dcs_dev/           # Main package source
external_controllers/  # Git submodule for casting machine drivers
tests/                 # Test suite
docs/                  # Documentation source
data/                  # Data files and samples
scripts/              # Utility scripts
```

## Development Guidelines

### Code Quality
- **Linting**: Use `ruff` for code formatting and style (configured for line length 120)
- **Testing**: pytest with coverage reporting
- **Documentation**: Google-style docstrings
- **Version Control**: Semantic versioning with bumpversion

### Key Dependencies
- `pyads>=3.3.9`: TwinCAT/ADS communication
- `compas_rrc`: ABB robot communication framework
- `numpy`, `pandas`, `matplotlib`: Data processing and visualization
- `pydantic`: Data validation and settings management
- `attrs`: Class definitions

### Integration Points

#### PLC Communication
- Uses `pyads` for TwinCAT integration
- Real-time parameter monitoring and control
- Component state management

#### Robot Control
- ABB robots via COMPAS RRC framework
- Docker containerized controllers (real/virtual)
- RobotStudio simulation support

#### Data Management
- Real-time data recording capabilities
- CSV/structured data export
- Material and process parameter tracking

## Common Tasks

### Environment Setup
```bash
# Preferred: UV package manager
uv venv --python 3.10
source .venv/bin/activate
uv pip install -e .[dev]

# Update submodules
git submodule update --init --recursive
```

### Development Workflow
```bash
# Linting and formatting
ruff check .
ruff format .

# Testing
pytest tests/

# Documentation
mkdocs serve
```

### Robot Integration
```bash
# Real controller
docker-compose -f ./external_controllers/robot/docker_compas_rrc/real_controller/docker-compose.yml up

# Virtual controller  
docker-compose -f ./external_controllers/robot/docker_compas_rrc/virtual_controller/docker-compose.yml up
```

## Important Considerations

### System Requirements
- **OS**: Windows 10 (for TwinCAT) or Ubuntu 22.04
- **Hardware**: PLC controllers, ABB robots
- **Software**: TwinCAT 3.4, Docker, RobotStudio, Rhino/Grasshopper

### Configuration Files
- `pyproject.toml`: Main project configuration and dependencies
- `.bumpversion.cfg`: Version management
- `pyrightconfig.json`: Type checking configuration
- Docker Compose files for robot controllers

### Workflow Integration
- Rhino/Grasshopper for design input
- RobotStudio for robot programming and simulation  
- TwinCAT for PLC programming and real-time control
- Python middleware for orchestration and data management

## Version Management

The project uses semantic versioning (currently v1.0.0) with bumpversion for automated version updates across:
- `pyproject.toml`
- `src/dcs_dev/__init__.py`
- `.bumpversion.cfg`

## Testing Strategy

- Unit tests for core functionality
- Integration tests for PLC/robot communication
- Docker-based testing for robot controllers
- Documentation tests via doctest

When contributing, ensure all tests pass and maintain code coverage standards.