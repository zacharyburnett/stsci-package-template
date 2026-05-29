"""
nox session configuration
https://nox.thea.codes/en/stable/config.html

  nox --list-sessions
  nox -s format
  nox -s test
  nox -s build

You can activate any previously-created session environment with its full path.

to save environments to a place other than `.nox/`:

  nox --envdir /tmp/envs <-- 

To run selected sessions directly on the current interpreter (without creating an environment):

    nox -s test --no-venv

To run multiple pythons from the command line for a session:

    nox -s test --extra-pythons 3.11 3.12 3.13
"""

import nox

# fail if using an external program without external=True
nox.options.error_on_external_run = True


@nox.session(
    tags=["all"],
    python=["3.12", "3.13"],
    venv_backend="micromamba|mamba",
    default=False,
)
def format(session):
    session.install("-e", ".[contrib]")
    session.run("ruff", "format", ".")
    session.run("ruff", "check", ".", "--fix")
    session.run("ruff", "check", ".", "--fix", "--select", "I")

    session.run("ty", "check", ".", "--output-format=concise")


@nox.session(
    tags=["all", "test"],
    python=["3.12", "3.13"],
    venv_backend="micromamba|mamba",
    default=True,
)
def test(session):
    session.install("-e", ".[test]")


@nox.session(
    name="test-with-coverage",
    tags=["all", "coverage"],
    python=["3.12", "3.13"],
    venv_backend="micromamba|mamba",
    default=False,
)
def test_with_coverage(session):
    session.install("-e", ".[test]")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "combine")
    session.run("coverage", "report")
    session.run("coverage", "html")


@nox.session(
    tags=["all", "build"],
    python=["3.12", "3.13"],
    venv_backend="micromamba|mamba",
    default=False,
)
def build(session):
    session.run("rm", "-rf", "build")
    session.run("rm", "-rf", "dist")

    session.install("build")
    session.run("python", "-m", "build")
