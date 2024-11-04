# **Digital casting system package**
## WIP

TODO make the doc for software architecture


    ───dcs_dev
        ├───abb_rob
        ├───data_processing
        │         │  data_processing.py
        │         │  data_struct.py
        ├───gui
        ├───hal
        │    │ device.py
        │    │ interface.py
        │    │ plc.py
        ├
        ├───utilities
        ├───visualization
        ├───config
            │  beckhoff_controller.json
            │  abb_irb4600.json

<!-- NOTE: -->
- data processing
    passing the processing data into system
    to covert plc raw data into research data

- hal: interface to convert config into python object
- plc interface API to connect PLC
- device :class or extend from plc
        app gui user interface MOVE to cpp part
        thinking how to read py lib into c++ a wrapper.

- config
    abb_irb4600.json
    beckhoff_controller.json

TODO robot package
    - how to define robot package
    - for rhino user and gh user
