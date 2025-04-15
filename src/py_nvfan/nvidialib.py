import pynvml

pynvml.nvmlInit()


def getTotalDevices() -> int:
    return pynvml.nvmlDeviceGetCount()


def setFanDuty(
    currentTemp: int, targetTemps: list[int], targetDuties: list[int]
) -> int:
    if not targetTemps or not targetDuties or len(targetTemps) != len(targetDuties):
        raise ValueError(
            "The targetTemps and targetDuties lists must have the same length and cannot be empty."
        )

    if currentTemp <= targetTemps[0]:
        return targetDuties[0]

    for i in range(1, len(targetTemps)):
        if targetTemps[i - 1] < currentTemp <= targetTemps[i]:
            return targetDuties[i]

    return targetDuties[-1]


if __name__ == "__main__":
    # print(getNvidiaBoardsPresent())
    # print("")
    pass
