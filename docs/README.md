# Writing and maintaining documentation

Documentation for `stsci-package-template` is written in [Sphinx reStructuredText (`.rst`)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
in this `docs/` directory, and is hosted online at https://spacetelescope.github.io/stsci-package-template

### Building documentation locally

```shell
cd docs/
pip install -r requirements.txt
make clean
make html
```

The docs will build to `docs/_build/html/`.
Open `docs/_build/html/index.html` to view the pages in your browser.
