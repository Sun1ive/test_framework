from time import sleep
from modules.printer_device import ZebraZD420PrinterModule
from enums import SERVICES_MAP


def fn(param):
    print(f"~~~~~~~~self params {param}")
    z.set_printer_state({
        'message': 'testing'
    })


# EXAMPLE
if __name__ == "__main__":
    try:
        print("Starting app")
        z = ZebraZD420PrinterModule(SERVICES_MAP.PRINTER_SERVICE.value)

        z.emitter.on('ep_attached', fn)

    except KeyboardInterrupt as e:
        print("Ctrl+C received! ...")
    except RuntimeError as e:
        pass
    except BaseException:
        pass
