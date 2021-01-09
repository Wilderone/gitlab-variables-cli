import json
import sys
import gitlab


def parse_single_variable(data):
    if not data:
        print("Error, No data in -p. Use KEY=VALUE syntax")
        sys.exit(1)
    if not "=" in data:
        print("Error, Use KEY=VALUE syntax")
        sys.exit(1)
    try:
        key, value = data.split("=")
        return [{"key": str(key), "value": str(value)}]
    except ValueError as e:
        print(e)
        sys.exit(1)


def parse_file_variable(path):
    if not path:
        print("Path to file not provided")
        sys.exit(1)

    try:
        with open(path) as file:
            try:
                variables = json.load(file)
            except json.decoder.JSONDecodeError as e:
                print(f"Invalid JSON file. Error message: \n {e.msg}")
                sys.exit(1)

            for key, value in variables.items():
                yield {"key": str(key), "value": str(value)}
    except FileNotFoundError:
        print(f"File {path} not found")
        sys.exit(1)
    except IOError as e:
        print(f"IO Error \n {e}")
        sys.exit(1)


def mask_vars(var):
    try:
        var.masked = True
        var.save()
    except gitlab.exceptions.GitlabUpdateError as e:
        print(
            f"Can't mask variable {var.key}. Ensure variable is meet regular expression requirements. Error \n {e.response_body} \n")
