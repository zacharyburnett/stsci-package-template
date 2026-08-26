from pathlib import Path

import numpy
from setuptools import Extension, setup

# Setup C module include directories
include_dirs = [numpy.get_include()]

# Setup C module macros
define_macros = [
    ("NUMPY", "1"),
    ("Py_LIMITED_API", 0x030B0000),  # PY_VERSION_HEX for 3.11
]

setup(
    ext_modules=[
        Extension(
            "{{ cookiecutter.package_name }}.replace_with_c_module_name",
            Path(__file__).parent.glob("src/**/*.c"),
            include_dirs=include_dirs,
            define_macros=define_macros,
        ),
    ],
    options={"bdist_wheel": {"py_limited_api": "cp311"}},
)
