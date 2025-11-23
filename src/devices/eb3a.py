from ..base_devices import BaseDeviceV1
from ..fields import FieldName, SwitchField


class EB3A(BaseDeviceV1):
    def __init__(self):
        super().__init__(
            [
                SwitchField(FieldName.CTRL_AC, 3007),
                SwitchField(FieldName.CTRL_DC, 3008),
            ],
        )
