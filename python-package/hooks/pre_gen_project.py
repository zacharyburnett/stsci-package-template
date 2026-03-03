import re

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

PACKAGE_NAME = "{{ cookiecutter.package_name }}"

if not re.match(MODULE_REGEX, PACKAGE_NAME):
    raise SyntaxError(
        f"`{PACKAGE_NAME}` is not a valid Python module name; please use `_` instead of `-`",
    )
