# Command Runner

Command Runner is a command-line tool to manage and run multiple scripts with parameters. The parameters for each script are configured using YAML files.

## Requirements

- Python 3.8 or above
- PyYAML library

## Installation

1. Clone this repository:

```bash
git clone https://github.com/leighshepperson/command_runner.git
```

2. Install the PyYAML library:

```bash
pip install pyyaml
```

## Usage

Each script that you want to run should have an associated YAML configuration file with the same name. The YAML file should define the command template and the parameters required for the command. 

For example, if you have a script called `deploy.py`, you would create a YAML file called `deploy.yaml` with the following structure:

```yaml
---
name: Deploy
command_template: "python3 {script_path} --build_dir {build_dir} --server {server} --credentials {credentials}"
params:
  script_path: { value: "/path/to/deploy.py" }
  build_dir: { value: "PROMPT" }
  server: { value: "192.168.0.1:8000", help: "The IP address and port of the server." }
  credentials: { value: "PROMPT", secret: true, help: "The login credentials for the server." }
```

In this YAML file, `name` is the name of the command, `command_template` is the template for the command to run, and `params` is a dictionary of parameters required by the command. Each parameter is a dictionary that can have the following keys:

- `value`: The value for the parameter. If this is set to "PROMPT", the application will prompt the user for the value.
- `secret`: If this is set to true, the application will hide the user's input when prompting for the value. This is useful for passwords or other sensitive information.
- `help`: A help message for the parameter.

To run a script, pass the name of the script (without the `.yaml` or `.py` extension) as an argument to `command_runner`:

```bash
./command_runner deploy
```

This will prompt the user to input the parameters marked as "PROMPT" in the `deploy.yaml` file, and then run the `deploy.py` script with the given parameters.

You can also list all scripts and their parameters with the `--list` flag:

```bash
./command_runner --list
```

This will print all the YAML files in the current directory, their commands, parameters, and help messages.

---

This README assumes that the name of the application is `command_runner`. Replace this with the actual name of your application as needed.
