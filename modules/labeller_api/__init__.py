from extension import ServiceEndpoint
from enums import EVENTS_MAP
from utils import getId
from typing import Optional


class LabellerApi(ServiceEndpoint):
    service: Optional[str] = None

    def __init__(self, serviceName: str) -> None:
        super().__init__(serviceName)
        self.service = serviceName
        print("consturctor")

    def set_order(self):
        self.socket.emit(EVENTS_MAP.SERVICE_EVENT.value, {
            'service': self.service,
            'id': None,
            'params': [{}, ['order']],
            'name': 'PropertiesChanged'
        })
