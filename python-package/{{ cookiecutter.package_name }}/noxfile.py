import nox

nox.options.sessions = ["format", "test"]


@nox.session(python="3")
def format(session):
    session.install("ruff")
    session.run("ruff", "format", ".")
    session.run("ruff", "check", ".", "--fix")
    session.run("ruff", "check", ".", "--fix", "--select", "I")

    session.install("ty")
    session.run("ty", "check", ".", "--output-format=concise")


@nox.session
def test(session):
    session.install("pytest")
    session.run("pytest")


@nox.session
def test_with_coverage(session):
    session.install("pytest", "coverage")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "combine")
    session.run("coverage", "report")
    session.run("coverage", "html")


@nox.session(python="3")
def build(session):
    session.run("rm", "-rf", "build")
    session.run("rm", "-rf", "dist")

    session.install("build")
    session.run("python", "-m", "build")
