import tkinter as tk

from data_processing.data_processing import DataHandler
from hal.device import InlineMixer
from hal.plc import PLC


if __name__ == "__main__":
    window = tk.Tk()
    window.minsize(800, 600)
    tk.Button(window, text="Hello World", command=window.quit).pack()

    machine_data = DataHandler()
    print(machine_data.__str__())

    # set the path to the PLC config file
    # machine_data._set_plc_config()

    machine_data._set_robot_mode_config()
    data = machine_data._load_json_to_instance()


    inline_mixer = InlineMixer(
        machine_data.machine["inline_mixer"].machine_id,
        machine_data.machine["inline_mixer"].machine_input,
        machine_data.machine["inline_mixer"].machine_output,
    )

    # print(str(inline_mixer))

    # print(inline_mixer.input_list())
    for input in inline_mixer.get_input_var_name():
        tk.Button(window, text=input, command=window.quit).pack()
    for output in inline_mixer.get_output_var_name():
        print(output)


    # inline_mixer.get_output_var_name()j
    for input in inline_mixer.set_input_dict():
        print(input)

    #while True:
    #    plc = PLC(netid="5.57.158.168.1.1", ip="")
    #    plc.connect()
    #    plc.set_plc_vars_input_list(inline_mixer.input_list())
    #    plc.get_variable("mixer_is_run")

    # plc.connect()

    # print(path.machine["inline_mixer"].machine_output)

    window.mainloop()
