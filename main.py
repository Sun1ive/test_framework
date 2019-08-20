#!/usr/bin/env python3

from time import sleep
from modules.printer_device import ZebraZD420PrinterModule
from modules.labeller_api import LabellerApi
from enums import SERVICES_MAP


def fn(param):
    print(f"~~~~~~~~self params {param}")
    # z.set_printer_state({
    #     'message': 'testing'
    # })

    api.set_order()


# EXAMPLE
if __name__ == "__main__":
    try:
        print("Starting app")
        # z = ZebraZD420PrinterModule(SERVICES_MAP.PRINTER_SERVICE.value)

        # z.emitter.on('ep_attached', fn)

        api = LabellerApi('order.service')
        api.emitter.on('ep_attached', fn)

    except KeyboardInterrupt as e:
        print("Ctrl+C received! ...")
    except RuntimeError as e:
        pass
    except BaseException:
        pass
