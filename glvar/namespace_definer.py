import requests
import json
import os
import gitlab
import sys

from authorization import gl

namespace = {}


def check_exist(list_available, name):
    if len(list_available) == 0:
        print(f"no group or project available for {name} name")
        sys.exit(1)


def get_project(name):
    projects_available = gl.projects.list(owned=True, search=name)
    check_exist(projects_available, name)
    return projects_available[0]


def get_group(name):
    group_available = gl.groups.list(search=sys.argv[sys.argv.index('-g') + 1])
    check_exist(group_available, sys.argv[sys.argv.index('-g') + 1])
    return group_available[0]


if "-p" in sys.argv:
    namespace["project"] = get_project(sys.argv[sys.argv.index('-p') + 1])


elif "-g" in sys.argv:
    namespace["group"] = get_group(sys.argv[sys.argv.index('-g') + 1])

elif os.environ.get('CLI_GITLAB_PROJECT'):
    namespace['project'] = get_project(os.environ.get('CLI_GITLAB_PROJECT'))

elif os.environ.get('CLI_GITLAB_GROUP'):
    namespace['group'] = get_project(os.environ.get('CLI_GITLAB_GROUP'))


if not namespace:
    print("Missing project or group name (use -p PROJECT_NAME or -g GROUP_NAME or environement variables (see --help))")
    sys.exit(1)

if len(namespace) > 1:
    print("You provide too much objects (for example multiple projects or both group and project). Check your environment variables. Pass one project or one group")
    for i in namespace.values():
        print(f"{i.name} provided")
    sys.exit(1)
