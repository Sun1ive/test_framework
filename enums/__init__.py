#!/usr/bin/env python3

from enum import Enum


class EVENTS_MAP(Enum):
    CONNECT = 'connect'
    SERVICE_ATTACH = 'service_attach'
    SERVICE_RESPONSE = 'service_response'
    SERVICE_REQUEST = 'service_request'
    SERVICE_EVENT = 'service_event'
    SERVICE_SUBSCRIBE = 'service_subscribe'


class SERVICES_MAP(Enum):
    PRINTER_SERVICE = 'printer.device.service'
    ORDER_SERVICE = 'order.service'
    QR_SERVICE = 'qr.device.service'
