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

@dataclass
class MixerStructOutput:
    pass
