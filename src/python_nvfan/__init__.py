from .nvidialib import getTotalDevices
from .config import printAsciiArt
from rich.console import Console

cl = Console()


def main() -> None:
    printAsciiArt()
    # totalDevices = getTotalDevices()
    # for i in range(totalDevices):
    #     cl.print(f"Device {i}:")
