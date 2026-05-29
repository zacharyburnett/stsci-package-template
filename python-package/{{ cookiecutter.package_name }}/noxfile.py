"""
 execute this file by running nox --noxfile <noxfile.py>

 Nox stores virtualenvs in .nox/, but that can be overridden with
 nox --envdir /tmp/envs
 
 micromamba is set as the default backend, you can activate any env that was created
 by using the full path to the environment

 each session is configured like an app.route, and a new virtualenv is created for each
 and contains an environment and a set of commands

 use default=False in the session decorator to not run that session by default
 
 >nox --list-sessions
 >nox -s test
 >nox --session simple-nox-test
 >nox --envdir /tmp/envs <-- to save environments to a place other that .nox/

 there are some situations where it is advantageous to reuse the 
 virtualenvs between runs. Use -r or --reuse-existing-virtualenvs 
 or for fine-grained control use --reuse-venv=yes|no|always|never

 --no-venv Runs the selected sessions directly on the current interpreter, without creating a venv. 
 This is an alias for '--force-venv-backend none'.
 
 --extra-pythons 3.11 3.12 3.13   <- to run multiple pythons from the command line for a session

NOTE: If you have just created a new package template, 
make sure that you have initialized this package with git before running tests: git init

"""
import nox

#make Nox fail the session if it uses any external program
#without explicitly passing external=True into session.run:
nox.options.error_on_external_run = True


# a list of python versions will create an env for each
# and run all the tests
@nox.session(name="format",
             tags=["all"],
             python=["3.12", "3.13"],
             venv_backend='micromamba|mamba',
             default=False)
def format(session):
    session.install("-e", ".[contrib]")
    session.run("ruff", "format", ".")
    session.run("ruff", "check", ".", "--fix")
    session.run("ruff", "check", ".", "--fix", "--select", "I")

    session.run("ty", "check", ".", "--output-format=concise")


@nox.session(name="test",
             tags=["all", "test"],
             python=["3.12","3.13"],
             venv_backend='micromamba|mamba',
             default=True)
def test(session):
    session.install("-e", ".[test]")


@nox.session(name="test-with-coverage",
             tags=["all", "coverage"],
             python=["3.12","3.13"],
             venv_backend='micromamba|mamba',
             default=False)
def test_coverage(session):
    session.install("-e", ".[test]")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "combine")
    session.run("coverage", "report")
    session.run("coverage", "html")


@nox.session(name="build",
             tags=["all", "build"],
             python=["3.12","3.13"],
             venv_backend='micromamba|mamba',
             default=False)
def build(session):
    session.run("rm", "-rf", "build")
    session.run("rm", "-rf", "dist")

    session.install("build")
    session.run("python", "-m", "build")
