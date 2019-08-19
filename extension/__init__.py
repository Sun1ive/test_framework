#!/usr/bin/env python3

import socketio
import uuid

from emitter import Emitter
from typing import Optional, Any
from enums import EVENTS_MAP, SERVICES_MAP


def getId() -> str:
    return str(uuid.uuid4())


HOST = '127.0.0.1'
PORT = "3000"


class ServiceEndpoint():
    service: Optional[str] = None
    socket: socketio.client = None
    emitter: Optional[Emitter] = None

    def __init__(self, serviceName: str):
        self.emitter = Emitter()
        print(f"CONSTRUCTOR OF SE {self.emitter}")
        self.service = serviceName
        self.socket = socketio.Client(logger=True)
        self.socket.connect(
            f'http://{HOST}:{PORT}',
            {'socketio_path': '/'},
            'websocket'
        )

        self.socket.on(EVENTS_MAP.CONNECT.value, self.subscribe_to_service)
        self.socket.on(EVENTS_MAP.SERVICE_RESPONSE.value,
                       self.service_response)

    def close_connection(self) -> None:
        self.socket.disconnect()

    def get_socket(self) -> socketio.client:
        return self.socket

    def subscribe_to_service(self) -> None:
        self.socket.emit(EVENTS_MAP.SERVICE_ATTACH.value, self.service)
        self.socket.on(EVENTS_MAP.SERVICE_ATTACH.value, self.service_attach)
        print("Subscribe to service")

    def service_response(self, value: Any) -> Any:
        print(f"value incoming {value}")
        return value

    def get_properties(self, service: str) -> None:
        id: str = str(uuid.uuid4())

        print(f"id = {id}, service = {service}")

        self.socket.emit(EVENTS_MAP.SERVICE_REQUEST.value, {
            'id': id,
            'method': '<get>',
            'params': {},
            'service': service
        })

    def service_request(self, value: str) -> None:
        print(f"Hello world {value}")

    def service_event(self, value: Any) -> None:
        print(f"Service event handler {value}")

    def service_attach(self, service: str) -> None:
        self.socket.on(EVENTS_MAP.SERVICE_REQUEST.value, self.service_request)
        self.socket.on(EVENTS_MAP.SERVICE_EVENT.value, self.service_event)

        print('service attached ', service)

        if service == SERVICES_MAP.PRINTER_SERVICE.value:
            self.socket.emit(
                EVENTS_MAP.SERVICE_SUBSCRIBE.value,
                self.service
            )
            self.emitter.emit("ep_attached", True)

        # elif service == SERVICES_MAP.ORDER_SERVICE.value:
        #     self.socket.emit(
        #         EVENTS_MAP.SERVICE_SUBSCRIBE.value,
        #         SERVICES_MAP.ORDER_SERVICE.value
        #     )

    def set_printer_state(self, data: dict) -> None:
        print(f"Emit event from set_printer_state {data}")
        # self.set_printer_state({'message': 'hello world'})
        self.socket.emit(EVENTS_MAP.SERVICE_EVENT.value, {
            'service': SERVICES_MAP.PRINTER_SERVICE.value,
            'id': None,
            'params': [{'printerErrorState': data}, []],
            'name': 'PropertiesChanged'
        })
