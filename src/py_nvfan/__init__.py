from .nvidialib import getTotalDevices, setFanDuty
from .config import VERSION, printAsciiArt, AppConfig
from confz import FileSource
from rich.console import Console
import argparse
import os
import sys

cl = Console()


def passArgs() -> None:
    printAsciiArt()
    # Configuração do parser
    parser = argparse.ArgumentParser(
        description=f"py-nvfan v{VERSION}: Monitor NVIDIA GPU fans and temperatures.",
    )

    # Argumentos
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default=AppConfig.CONFIG_SOURCES.file,  # type: ignore
        required=False,
        help="Path to the config file (config.yaml)",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"Version {VERSION}",
        help="Show the version and exit",
    )

    # Processamento dos argumentos
    args: argparse.Namespace = parser.parse_args()

    AppConfig.CONFIG_SOURCES = FileSource(file=args.config)

    print(args.config)
    if not os.path.exists(args.config):
        cl.print("[bold red]Config file not found[/bold red]")
        sys.exit(1)
    else:
        appConfig = AppConfig()
        print(appConfig.targetTemps)
        print(appConfig.targetDuties)


def main() -> None:
    passArgs()
    # currentTemp = 70
    # appConfig = AppConfig()
    # print(f"currentTemp: {currentTemp}")
    # print(f"targetTemps: {appConfig.targetTemps}")
    # print(f"targetDuties: {appConfig.targetDuties}")
    # fanDuty = setFanDuty(
    #     currentTemp=currentTemp,
    #     targetTemps=appConfig.targetTemps,
    #     targetDuties=appConfig.targetDuties,
    # )
    # print(f"fanDuty: {fanDuty}")

    # totalDevices = getTotalDevices()
    # for i in range(totalDevices):
    #     cl.print(f"Device {i}:")
