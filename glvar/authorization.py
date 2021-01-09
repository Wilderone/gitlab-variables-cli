import requests
import os
import gitlab
import sys
import configparser

gitlab_url = None
gitlab_private_token = None
gitlab_file = os.environ.get('GITLAB_CREDENTIALS', None)

if gitlab_file:
    config = configparser.ConfigParser()
    try:
        config.read(gitlab_file)
        gitlab_url = config["GITLAB"]["GITLAB_URL"]
        gitlab_private_token = config["GITLAB"]["GITLAB_PRIVATE_TOKEN"]
    except configparser.MissingSectionHeaderError as e:
        print(
            f"invalid config file. Use [HEADER] and key=value \n {e.message}")
    except configparser.ParsingError as e:
        print(f"invalid config file. Use key=value notation \n {e.message}")

    except KeyError as e:
        print(
            f"config file exception \n {e} not provided. Trying to read from environment..")


if not gitlab_url:
    gitlab_url = os.environ.get('GITLAB_URL')

if not gitlab_private_token:
    gitlab_private_token = os.environ.get('GITLAB_PRIVATE_TOKEN')

if not gitlab_url:

    print("missing GITLAB_URL. Use GITLAB_URL environment variable")
    sys.exit(1)

if not gitlab_private_token:
    print("missing GITLAB_PRIVATE_TOKEN. Use GITLAB_PRIVATE_TOKEN environment variable")
    sys.exit(1)


gl = gitlab.Gitlab(gitlab_url, private_token=gitlab_private_token)
gl.auth()
