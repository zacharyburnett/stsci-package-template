import re
import sys

MODULE_REGEX = r"^([_a-zA-Z]+[_a-zA-Z\d]+)$"

PACKAGE_NAME = "{{ cookiecutter.package_name }}"

if not re.match(MODULE_REGEX, PACKAGE_NAME):
    print(
        f"WARNING: `{PACKAGE_NAME}` may not be importable as a module name in Python",
        file=sys.stderr,
    )
