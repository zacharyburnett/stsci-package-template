import os
import shutil
 
REMOVE_PATHS = [
    "{% if not cookiecutter.python_c_extensions %}setup.py{% endif %}",
]
 
for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else shutil.rmtree(path)
