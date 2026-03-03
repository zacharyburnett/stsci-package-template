<a href="https://stsci.edu">
  <img src="docs/assets/stsci_logo.png" alt="STScI Logo" width="15%" style="margin-left: auto;"/>
  <img src="docs/assets/stsci_name.png" alt="STScI Name" width="68%"/>
</a>

# STScI Package Template

This [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template defines best practices and boilerplate for STScI packages.

To initialize a new package from this template, run [`cruft create`](https://cruft.github.io/cruft):
```shell
cruft create https://github.com/spacetelescope/stsci-package-template.git
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

### Optional Features

- option to set up a Python package
- option to manage changelog with [`towncrier`](https://github.com/twisted/towncrier)

## Acknowledgements

Adapted from [Cookiecutter PyPackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
