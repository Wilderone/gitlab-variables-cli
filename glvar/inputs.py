import sys
import gitlab

from functions import show_vars, show_vars_for_all, add_variable, change_variable, delete_variable
from support import parse_file_variable, parse_single_variable
from namespace_definer import namespace

if "-a" in sys.argv:
    masked = False
    if "-m" in sys.argv:
        masked = True
    add_variable(data=parse_single_variable(
        sys.argv[sys.argv.index('-a')+1]), masked=masked, namespace=namespace)

if "-f" in sys.argv:
    add_variable(data=parse_file_variable(
        sys.argv[sys.argv.index('-f')+1]), namespace=namespace)

if "-l" in sys.argv:
    show_vars(namespace)

if "-la" in sys.argv:
    show_vars_for_all(namespace)

if "-rm" in sys.argv:
    data = str(sys.argv[sys.argv.index('-rm')+1]).split(",")
# Iterate through argument, get list no matter if we get one ore multiple variables
    for arg in data:
        try:
            delete_variable(data=arg, namespace=namespace)
        except gitlab.exceptions.GitlabDeleteError as e:
            print(
                f" ===== no such variable {arg} =====")
            continue

if "-rmf" in sys.argv:
    data = sys.argv[sys.argv.index('-rmf') + 1]
    delete_variable(data=parse_file_variable(data),
                    namespace=namespace, fromfile=True)


if "-cv" in sys.argv:
    data = str(sys.argv[sys.argv.index('-cv')+1]).split(",")
    # Iterate through argument, get list no matter if we get one ore multiple variables (same as -rm)
    for arg in data:
        try:
            change_variable(data=parse_single_variable(arg),
                            namespace=namespace)
        except gitlab.exceptions.GitlabDeleteError as e:
            print(
                f" ===== no such variable {arg} =====")
            continue
