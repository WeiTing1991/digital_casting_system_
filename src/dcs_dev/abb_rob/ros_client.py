""" This module is a ROS client for ABB robot controller via compas_rrc."""

import compas_rrc as rrc

class DcsRosClient:
"""This class is a ROS client for ABB robot controller via compas_rrc."""
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
        get_gi = self.abb.send_and_wait(rrc.ReadGroup(io_name))
        print(f"{io_name} is {get_gi}")

    def _get_analog_output(self, io_name: str, value: int) -> None:
        get_ao = self.abb.send_and_wait(rrc.SetAnalog(io_name, value))
        print(f"{io_name} is {get_ao}")

    def _get_analog_input(self, io_name: str) -> None:
        get_ai = self.abb.send_and_wait(rrc.ReadAnalog(io_name))
        print(f"{io_name} is {get_ai}")

    # movement functions
    def _move_to_frame(self, frame, speed: int, zone: int) -> None:
        move_to_frame = self.abb.send(rrc.MoveToFrame(frame, speed, zone, rrc.Motion.LINEAR))
        print(f"Robot is moving to {frame}")

    def _move_to_robotarget(self):
        raise NotImplementedError

    def _move_to_joints(self, joints: list, external_axes, speed: int, zone: int) -> None:
        move_to_joints = self.abb.send(rrc.MoveToJoints(joints, external_axes, speed, zone))
        print(f"Robot is moving to {joints}")

    def _wait(self, time:int) -> None:
        self.abb.send(rrc.WaitTime(time))

    # Robot config

    def _set_move_zone(self, zone: int) -> None:
        raise NotImplementedError

    def _set_acceleration(self, acc: int, ramp: int) -> None:
        set_acceleration = self.abb.send(rrc.SetAcceleration(acc, ramp))

    def _set_max_speed(self, overide: int, max_tcp: int) -> None:
        """
        override: Unit [%]
        max_tcp: Unit [mm/s]
        """
        set_max_speed = self.abb.send(rrc.SetMaxSpeed(overide, max_tcp))

    def _set_tool(self, tool_name: str) -> None:
        self.abb.send(rrc.SetTool(tool_name))
        print(f"Tool is set to {tool_name}")

    def _get_tool(self):
        raise NotImplementedError

    def _set_workobject(self, workobject: str) ->None:
        self.abb.send(rrc.SetWorkObject(workobject))
        print(f"Workobject is set to {workobject}")

    def _get_workobject(self):
        raise NotImplementedError

    def _get_robotarget(self) -> tuple:
        frame, external_axes = self.abb.send_and_wait(rrc.GetRobtarget())
        return frame, external_axes

    def _print_text(self, text: str) -> None:
        self.abb.send(rrc.PrintText(text))
        print(text)
