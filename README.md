# py-nvfan

py-nvfan is a Python application designed to monitor and control NVIDIA GPU fan speeds on Linux systems. It provides a command-line interface to adjust fan profiles, monitor GPU temperatures, and automate cooling based on user-defined thresholds.

## Features
- Monitor NVIDIA GPU temperatures and fan speeds
- Set custom fan speed profiles
- Automatic fan control based on temperature
- Command-line interface for easy usage
- Logging and status reporting

## Requirements
- Python 3.13+
- NVIDIA GPU with supported drivers
- Linux x86_64 operating system
- [nvidia-smi](https://developer.nvidia.com/nvidia-system-management-interface) installed and available in PATH
- [UV](https://github.com/astral-sh/uv) for project management

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/py-nvfan.git
   cd py-nvfan
   ```
2. Install dependencies using UV:
   ```bash
   uv sync
   ```


## Usage
Run the application from the command line:
```bash
uv venv python main.py [options]
```

Example:
```bash
uv venv python main.py --auto
```

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
Use this tool at your own risk. Improper fan control may cause hardware damage. Always monitor your GPU temperatures and ensure adequate cooling.
