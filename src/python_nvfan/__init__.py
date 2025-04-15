from pynvml_utils import nvidia_smi


def main() -> None:
    nvsmi = nvidia_smi.getInstance()
    temp = nvsmi.DeviceQuery(filter="temperature.gpu")
    print(temp["gpu"][0])
