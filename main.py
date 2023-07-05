import yaml
import argparse
import subprocess
import getpass
import glob
import os

def load_config(script_name):
    with open(f"{script_name}.yaml", 'r') as file:
        configs = list(yaml.safe_load_all(file))
    return configs

def fill_params(config):
    filled_params = {}
    for key, value in config["params"].items():
        if value.get("value") == "PROMPT":
            if value.get("secret"):
                filled_value = getpass.getpass(f"Enter value for {key}: ")
            else:
                filled_value = input(f"Enter value for {key}: ")
        elif "value" in value:
            filled_value = value["value"]
        else:
            filled_value = value.get("default")
        filled_params[key] = filled_value
    return filled_params

def create_command(script_name, params):
    command_template = config["command_template"]
    filled_command = command_template.format(**params)
    return filled_command

def run_script(command):
    process = subprocess.Popen(command, shell=True)
    process.communicate()

def list_scripts():
    files = glob.glob('*.yaml')
    for file in files:
        print(f"Script: {os.path.splitext(file)[0]}")
        configs = load_config(os.path.splitext(file)[0])
        for config in configs:
            print(f"\tCommand: {config['name']}")
            for param, details in config['params'].items():
                print(f"\t\tParameter: {param}")
                print(f"\t\t\tValue: {details.get('value', 'Not specified')}")
                print(f"\t\t\tHelp: {details.get('help', 'No help available')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run command-line scripts with YAML configuration.")
    parser.add_argument("script_name", nargs='?', help="The name of the script (without .yaml)")
    parser.add_argument("--list", action="store_true", help="List all scripts and parameters")
    args = parser.parse_args()

    if args.list:
        list_scripts()
    elif args.script_name:
        configs = load_config(args.script_name)
        for config in configs:
            params = fill_params(config)
            command = create_command(args.script_name, params)
            run_script(command)
    else:
        parser.print_help()
