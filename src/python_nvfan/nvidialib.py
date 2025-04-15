import pynvml

pynvml.nvmlInit()


def getTotalDevices() -> int:
    return pynvml.nvmlDeviceGetCount()


if __name__ == "__main__":
    # print(getNvidiaBoardsPresent())
    print("")
