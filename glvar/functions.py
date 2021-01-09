import requests
import json
import os
import gitlab
import sys
from namespace_definer import namespace
from support import parse_file_variable, parse_file_variable, mask_vars
from authorization import gitlab_private_token, gitlab_url


def show_vars(namespace):
    if isinstance(namespace[next(iter(namespace))], gitlab.v4.objects.Project):
        # if single project passed
        project = (namespace[next(iter(namespace))])
        print(f"\n===== Project {project.name} had this variables ====\n")
        for variable in project.variables.list():
            print(f"{variable.key}={variable.value}")

    elif isinstance(namespace[next(iter(namespace))], gitlab.v4.objects.Group):
        # if group passed
        group = namespace[next(iter(namespace))]
        print(f"\n===== Group {group.name} had this variables ====\n")
        for variable in group.variables.list():
            print(f"{variable.key}={variable.value}")

    else:
        print(
            f"There is no {namespace[next(iter(namespace))]} name of group or project")


def show_vars_for_all(namespace):
    # function will show all variables in every project of a group
    # using requests because gitlab lib do it tooo long
    if not isinstance(namespace[next(iter(namespace))], gitlab.v4.objects.Group):
        return f"{namespace[next(iter(namespace))].name} is not a group name"
        # list of all projects as GroupObject, this object does not have
        # .variables method so we need it only to find projects in group
        # TODO imporve that
    group_objects = [x for x in namespace[next(
        iter(namespace))].projects.list()]
    projects = []
    header = {"PRIVATE-TOKEN": gitlab_private_token}
    for i in group_objects:
        r = requests.get(
            url=f"{gitlab_url}/api/v4/projects/{i.id}/variables", headers=header)
        print(
            f"\n=============== VARIABLES FOR PROJECT {i.name} ================== \n")
        for var in r.json():
            print(f"{var['key']}={var['value']}")


def add_variable(data, masked=False, namespace=namespace):
    if not data:
        print("no data to manipulate")
        sys.exit(1)

    for var in data:
        try:
            new_var = namespace[next(iter(namespace))].variables.create(var)
            if masked:
                mask_vars(new_var)
            print(
                f"===== Variable {var} added to {namespace[next(iter(namespace))].name} =====")
        except gitlab.exceptions.GitlabCreateError as e:
            print(f"for variable {var} error ocured: \n {e.response_body}")
            continue


def change_variable(data, namespace=namespace):
    if not data:
        print("no data to manipulate")
        sys.exit(1)

    for var in data:
        variable = namespace[next(iter(namespace))].variables.get(var['key'])
        variable.value = var['value']
        variable.save()
        print(
            f" ======= Project {namespace[next(iter(namespace))].name}, new value for {var['key']} is {var['value']} ===============")


def delete_variable(data, namespace=namespace, fromfile=False):
    if not data:
        print("no data to manipulate")
        sys.exit(1)

    if fromfile:
        for var in data:
            try:
                namespace[next(iter(namespace))].variables.delete(var['key'])
                print(
                    f" ===== variable {var['key']} removed from {namespace[next(iter(namespace))].name} =====")
            except gitlab.exceptions.GitlabDeleteError as e:
                print(f" ===== no such variable {var} =====")
                continue
    else:
        try:
            namespace[next(iter(namespace))].variables.delete(str(data))
            print(
                f"===== variable {data} removed from {namespace[next(iter(namespace))].name} =====")
        except gitlab.exceptions.GitlabDeleteError as e:
            print(f" ===== no such variable {arg} =====")
