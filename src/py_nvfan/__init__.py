from .nvidialib import *
from .config import VERSION, printAsciiArt, AppConfig, cl, pc
from confz import FileSource
import argparse
import os
import sys
import time


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

    # print(args.config)
    if not os.path.exists(args.config):
        cl.print("[bold red]Config file not found[/bold red]")
        sys.exit(1)
    else:
        appConfig = AppConfig()
        pc(message="using config file", variable=args.config)
        pc(message="Temperatures", variable=appConfig.temps)
        pc(message="FanSpeeds", variable=appConfig.fanSpeeds)
        totalDevices = getTotalDevices()
        pc(message="Total devices", variable=totalDevices)
        while True:
            with cl.status("Running...") as status:
                try:
                    for i in range(totalDevices):
                        cl.print("-" * 40)
                        cl.print(
                            f"[bold yellow]Device[/bold yellow]\t\t: [{i}] - {getDeviceName(gpu_index=i)}"
                        )
                        currentTemp: int = getGpuTemperature(gpu_index=i)
                        pc(message="Temperature\t", variable=f"{currentTemp}°C")
                        newfanSpeed = getFanDuty(
                            currentTemp=currentTemp,
                            targetTemps=appConfig.temps,
                            targetDuties=appConfig.fanSpeeds,
                        )
                        fanCount = getFanCount(gpu_index=i)
                        pc(message="Fan Count\t", variable=fanCount)
                        currentFanSpeed: int = getFanSpeed(gpu_index=i)
                        pc(
                            message="Fan Speed\t",
                            variable=f"{currentFanSpeed}%",
                        )

                        cl.print(
                            f"currentFanSpeed: {currentFanSpeed} newfanSpeed: {newfanSpeed}"
                        )
                        if currentFanSpeed != newfanSpeed:
                            pc(message="Setting new fan speed...", variable=newfanSpeed)
                            setFanSpeed(gpu_index=i, fan_speed=newfanSpeed)
                            pc(
                                message="New Fan Speed\t",
                                variable=f"{newfanSpeed}%",
                            )

                    time.sleep(1)

                except KeyboardInterrupt:
                    cl.print("[bold red]Exiting...[/bold red]")
                    break


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
