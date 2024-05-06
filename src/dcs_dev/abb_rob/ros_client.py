import compas_rrc as rrc


class DcsRosClient:
    def __init__(self):
        self._ros = None
        self._abb = None

    def _init_ros_client(self) -> None:
        self.ros = rrc.RosClient()
        self.ros.run()
        self.abb = rrc.AbbClient(self.ros, "/rob1")

        print("Connected:", self.ros.is_connected)
        self.abb.send_and_wait(rrc.PrintText("Wellcome to digital casting sytsem"))

    def _close_ros_client(self) -> None:
        self.ros.close()
        self.ros.terminate()

        print("Connected:", self.ros.is_connected)
        self.abb.send_and_wait(rrc.PrintText("Disconected to ROS"))

    # IO functions
    def _set_digital_output(self, io_name: str, value: int) -> None:
        set_do = self.abb.send_and_wait(rrc.SetDigital(io_name, value))
        print(f"{io_name} is set to {value}")

    def _get_digital_input(self, io_name: str) -> None:
        get_di = self.abb.send_and_wait(rrc.ReadDigital(io_name))
        print(f"{io_name} is {get_di}")

    def _set_group_output(self, io_name: str, value: int) -> None:
        get_go = self.abb.send_and_wait(rrc.SetGroup(io_name, value))
        print(f"{io_name} is {value}")

    def _get_group_input(self, io_name: str) -> None:
        get_gi = self.abb.send_and_wait(rrc.SetGroup(io_name))
        print(f"{io_name} is {get_gi}")


    def _set_tool(self):
        pass

    def _get_tool(self):
        pass

    def _set_workobject(self):
        pass

    def _get_workobject(self):
        pass

