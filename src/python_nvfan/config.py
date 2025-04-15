from confz import BaseConfig, FileSource
import os


APP_NAME = "docker-whatch"
VERSION = "0.1.0"


def printAsciiArt() -> None:
    asciiArt = r"""
     _            _                          _           _       _
  __| | ___   ___| | _____ _ __    __      _| |__   __ _| |_ ___| |__
 / _` |/ _ \ / __| |/ / _ \ '__|___\ \ /\ / / '_ \ / _` | __/ __| '_ \
| (_| | (_) | (__|   <  __/ | |_____\ V  V /| | | | (_| | || (__| | | |
 \__,_|\___/ \___|_|\_\___|_|        \_/\_/ |_| |_|\__,_|\__\___|_| |_|
    """
    print(asciiArt)


class AppConfig(BaseConfig):
    CONFIG_SOURCES = FileSource(
        file=os.path.join(
            os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "config.yaml"
        )
    )
