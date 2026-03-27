<a href="https://stsci.edu">
  <img src="docs/assets/stsci_logo.png" alt="STScI Logo" width="15%" style="margin-left: auto;"/>
  <img src="docs/assets/stsci_name.png" alt="STScI Name" width="68%"/>
</a>

# {{ cookiecutter.project_name }}

[![build]({{ cookiecutter.repository_url }}/actions/workflows/build.yml/badge.svg)]({{ cookiecutter.repository_url }}/actions/workflows/build.yml)
[![tests]({{ cookiecutter.repository_url }}/actions/workflows/tests.yml/badge.svg)]({{ cookiecutter.repository_url }}/actions/workflows/tests.yml)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Powered by STScI](https://img.shields.io/badge/powered%20by-STScI-blue.svg?colorA=707170&colorB=3e8ddd&style=flat)](https://www.stsci.edu)
{%- if cookiecutter.publish_docs_to == 'readthedocs.io' %}
[![ReadTheDocs](https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest)](https://{{ cookiecutter.package_name }}.readthedocs.io/en/latest/?badge=latest)
{%- elif cookiecutter.publish_docs_to == 'github.io' %}
[![GitHub Pages]({{ cookiecutter.repository_url }}/actions/workflows/pages-build-deployment/badge.svg)](https://spacetelescope.github.io/{{ cookiecutter.package_name }})
{%- endif %}

{{ cookiecutter.project_description }}
