import helper
import support
import inputs
import authorization
import functions
import namespace_definer

import sys


arguments = ["-p", "-g", "-l", "-la", "-a",
             "-f", "-m", "-rm", "-rmf", "-cv", "--help"]

check_provided = [x for x in sys.argv +
                  arguments if x in sys.argv and x in arguments]
if len(check_provided) == 0:
    print("provide some arguments. Use --help")
    sys.exit(1)
