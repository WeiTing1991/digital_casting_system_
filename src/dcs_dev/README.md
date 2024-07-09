# Digital casting system package

TODO make the doc for usage

    ───dcs_dev
        ├───abb_rob

        ├───data_processing
            │  data_processing.py
            │  data_struct.py

        ├───gui

        ├───hal
            │ device.py
            │ interface.py
            │ plc.py

        ├───utilities

        ├───visualization

        ├───_config
            │  abb_irb4600.json
            │  beckhoff_controller.json

│ └  data_processing.py
|  visualization
│ │  DataVisualization.py
│ │  DataVisualizationNew.py
│ │  test.py
│ └  visualization.py

dcs -- hal
data processing
interface
utilities

<!-- NOTE: -->

data processing
covert the processing data into system
some kits to covert plc data into research data

hal
interface: interface to covernt config into python object
plc interface api to connect plc
device :
maybe a main deviec class or extend from plc

robot package
how to define robot package
for rhino user and gh user

config --
abb_irb4600.json
beckhoff_controller.json

app gui user interface MOVE to cpp part
thinking how to read py lib into c++ a wrapper.
