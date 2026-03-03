import numpy as np
from setuptools import Extension, setup
from pathlib import Path

# Setup C module include directories
include_dirs = [np.get_include()]

# Setup C module macros
define_macros = [("NUMPY", "1")]

setup(
    ext_modules=[
        Extension(
            "{{ cookiecutter.package_name }}.replace_with_c_module_name",
            Path.glob("src/**/*.c"),
            include_dirs=include_dirs,
            define_macros=define_macros,
        ),
    ],
)

