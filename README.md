<a href="https://stsci.edu">
  <img src="docs/_static/stsci_pri_combo_mark_horizonal_white_bkgd.png" alt="Space Telescope Science Institute" width="83%" style="margin-left: auto;"/>
</a>

# STScI Package Template

This [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template defines best practices and boilerplate for STScI packages.

To initialize a new package from this template, run [`cruft create`](https://cruft.github.io/cruft):

```shell
cruft create https://github.com/spacetelescope/stsci-package-template.git --directory python-package
```

You can then use [`cruft update`](https://cruft.github.io/cruft/#updating-a-project)
to keep your package up to date with changes to this template:

```shell
cruft update
```

See [the `cruft` documentation](https://cruft.github.io/cruft)
for more information on installing and using `cruft`.

### Included Features

- `.gitignore` that covers editor files and Python objects
- scheduled GitHub Actions workflow that checks for changes to the upstream template (this repository) and makes a pull request to apply updates
- GitHub Dependabot config for grouped monthly dependency updates
- GitHub pull request template
- GitHub Actions workflow that automatically adds labels to pull requests
- `.pre-commit-config.yaml` configuration with checks and formatting

### Optional Features

- option to set up a Python package
- option to manage changelog with [`towncrier`](https://github.com/twisted/towncrier)
- option to publish documentation to ReadTheDocs
- option to use a task runner (`nox` or `tox`)

## Acknowledgements

Adapted from [Cookiecutter PyPackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
