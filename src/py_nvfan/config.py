import os
from typing import Any
from confz import BaseConfig, FileSource
from rich.console import Console


# SeuUsuario ALL=(ALL) NOPASSWD: /usr/bin/nvidia-settings

# APP_NAME
APP_NAME = "py-nvfan"
# APP_VERSION
VERSION = "0.1.6"

cl = Console()


def pc(message: str, variable: Any) -> None:
    cl.print(f"[bold yellow]{message}[/bold yellow]: {variable}")


def printAsciiArt() -> None:
    asciiArt = r"""
                               __             
 _ __  _   _       _ ____   __/ _| __ _ _ __  
| '_ \| | | |_____| '_ \ \ / / |_ / _` | '_ \ 
| |_) | |_| |_____| | | \ V /|  _| (_| | | | |
| .__/ \__, |     |_| |_|\_/ |_|  \__,_|_| |_|
|_|    |___/                
    """
    print(asciiArt)


class AppConfig(BaseConfig):
    CONFIG_SOURCES = FileSource(
        file=os.path.join(
            os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "config.yaml"
        )
    )

    temps: list[int]
    fanSpeeds: list[int]
