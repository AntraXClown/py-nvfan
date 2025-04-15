from pynvml_utils import nvidia_smi

nvsmi = nvidia_smi.getInstance()


def getNvidiaBoardsPresent():
    return nvsmi.DeviceQuery(filter="--list-gpus")


if __name__ == "__main__":
    print(getNvidiaBoardsPresent())
