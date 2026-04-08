import re
import sys

MODULE_REGEX = r"^([_a-zA-Z]+[_a-zA-Z\d]+)$"

PACKAGE_NAME = "{{ cookiecutter.package_name }}"

PYTHON_BUILD_BACKEND = "{{ cookiecutter.python_build_backend }}"
PYTHON_C_EXTENSIONS = "{{ cookiecutter.python_c_extensions }}" == "True"

if not re.match(MODULE_REGEX, PACKAGE_NAME):
    print(
        f"WARNING: `{PACKAGE_NAME}` may not be importable as a module name in Python",
        file=sys.stderr,
    )

if PYTHON_BUILD_BACKEND == "hatchling" and PYTHON_C_EXTENSIONS:
    raise NotImplementedError(
        "building Python C extensions with Hatch is not yet implemented"
    )
