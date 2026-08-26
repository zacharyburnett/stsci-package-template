======================
STScI Package Template
======================

This `Cookiecutter template <https://github.com/cookiecutter/cookiecutter>`_
defines best practices and boilerplate for STScI packages::

	cookiecutter https://github.com/spacetelescope/stsci-package-template.git

To keep your package updated with changes to this template,
use `Cruft <https://cruft.github.io/cruft>`_ instead of Cookiecutter::

	cruft create https://github.com/spacetelescope/stsci-package-template.git

This template `includes a GitHub Actions workflow <https://github.com/spacetelescope/stsci-package-template/blob/main/templates/.github/workflows/update.yml>`_ that
`runs Cruft to automatically check for updates <https://cruft.github.io/cruft/#updating-a-project>`_.
You can also do this manually with ``cruft update``.

.. toctree::

	options.rst
	github.rst

============
Contributing
============

``stsci-package-template`` is an open source package written in Python.
The source code is `available on GitHub <https://github.com/spacetelescope/stsci-package-template>`_.
New contributions and contributors are very welcome!

We strive to provide a welcoming community by abiding with our `CODE_OF_CONDUCT.md <https://github.com/spacetelescope/stsci-package-template/blob/main/CODE_OF_CONDUCT.md>`_.
