import os
import shutil
 
REMOVE_PATHS = [
    "{% if not cookiecutter.manage_changelog_with_towncrier %}changes/{% endif %}",
    "{% if not cookiecutter.manage_changelog_with_towncrier %}.github/workflows/changelog.yml{% endif %}",
    "{% if not cookiecutter.manage_changelog_with_towncrier %}towncrier.toml{% endif %}",
    "{% if not cookiecutter.manage_changelog_with_towncrier %}.github/release.yml{% endif %}",
    '{% if cookiecutter.publish_docs_to != "readthedocs.io" %}.readthedocs.yaml{% endif %}',
    '{% if cookiecutter.task_runner != "nox" %}noxfile.py{% endif %}',
    "{% if not cookiecutter.python_c_extensions %}setup.py{% endif %}",
]
 
for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else shutil.rmtree(path)
