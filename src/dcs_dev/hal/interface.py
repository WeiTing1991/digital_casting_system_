from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field


@dataclass(slots=True)
class DeviceStruct:
    """define the paramters info from json."""

    id: str = ""
    var_name: str = ""
    var_name_IN: str = ""
    type: str = ""
    active: bool = False

    def _to_dict(self) -> dict:
        return dict(asdict(self).items())


class DeviceStructInput:
    pass


class DeviceStructOutput:
    # getter
    # setter
    pass


@dataclass
class MixerStructOutput:

    get_speed_M1: DeviceStruct = field(default_factory=DeviceStruct)

    def __post_init__(self):
        self.get_speed_M1 = DeviceStruct()._to_dict()

    # get_speed_M2:dict = DeviceStructOutput()._to_dict()
    # get_torque_M1:dict= DeviceStructOutput()._to_dict()
    # get_torque_M2:dict = DeviceStructOutput()._to_dict(),
    # get_temperature_M1:dict = DeviceStructOutput()._to_dict(),
    # get_temperature_M2:dict = DeviceStructOutput()._to_dict(),
    # get_temperature_funnel:dict = DeviceStructOutput()._to_dict(),
    # get_temperature_funnel_outlet:dict = DeviceStructOutp out()._to_dict(),
    # get_temperature_funnel_plate:dict = DeviceStructOutput()._to_dict(),
    # get_pressure:dict = DeviceStructOutput()._to_dict()

    # output_params = [get_speed_M1, get_speed_M2]

    # def __init__(self): o
    #     self.output_params = self.__dict__
    #     print(self.output_params)

if __name__ == "__main__":

