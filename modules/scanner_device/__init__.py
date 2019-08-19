#!/usr/bin/env python3

from extension import ServiceEndpoint


class QrDatalogicModule(ServiceEndpoint):
    __instance = None

    @classmethod
    def get_instance(cls):
        if QrDatalogicModule.__instance is None:
            raise Exception("Not created!")
        return QrDatalogicModule.__instance

    @classmethod
    def create(cls, serviceName: str):
        if QrDatalogicModule.__instance is None:
            QrDatalogicModule(serviceName)
        else:
            raise Exception("Already exists!")

    def __init__(self, serviceName: str):
        if QrDatalogicModule.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ServiceEndpoint.__init__(self, serviceName)
            QrDatalogicModule.__instance = self

    def close_connection(self):
        QrDatalogicModule.__instance = None
        print('Close connection called.')
