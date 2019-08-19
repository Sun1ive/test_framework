from extension import ServiceEndpoint
from typing import Optional, Any
from enums import EVENTS_MAP, SERVICES_MAP


def f():
    print("something")


class ZebraZD420PrinterModule(ServiceEndpoint):
    __instance: Optional[Any] = None
    attached: bool = False

    def __init__(self, service: str) -> None:
        super().__init__(service)
        self.emitter.once("ep_attached", self.is_attached)

    def is_attached(self, param) -> None:
        print(f"is_attached {param}")
        self.attached = param

    def close_connection(self) -> None:
        ZebraZD420PrinterModule.__instance = None
        print('Close connection called.')

    def set_printer_state(self, data: dict) -> None:
        super().set_printer_state(data)


# # EXAMPLE
# if __name__ == "__main__":

#     # printer_instance: ZebraZD420PrinterModule = ZebraZD420PrinterModule.get_instance()

#     try:
#         ZebraZD420PrinterModule.create(SERVICES_MAP.PRINTER_SERVICE.value)
#         print("Starting app")
#     except KeyboardInterrupt as e:
#         print("Ctrl+C received! ...")
# #     except RuntimeError as e:
#         pass
#     except BaseException:
#         pass
