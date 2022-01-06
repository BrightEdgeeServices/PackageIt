"""Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
"""
import datetime
from pathlib import Path
import pytest

# import sys
from tempfile import mkdtemp
from beetools import get_os, rm_tree
import configparserext

# from github import Github, GithubException as gh_exc

_DESC = __doc__.split("\n")[0]
_PATH = Path(__file__)


_CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "Topic :: Software Development",
    "Topic :: System :: Systems Administration",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]
_INDEX_RST_BADGE_CODECOV = """.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/{0}
    :alt: CodeCov
    :target: https://app.codecov.io/gh/hendrikdutoit/{0}

"""
_INDEX_RST_BADGE_GITHUB_CI = """.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/{0}/CI
    :alt: GitHub Actions - CI
    :target: https://github.com/hendrikdutoit/{0}/actions/workflows/ci.yaml

"""
_INDEX_RST_BADGE_GITHUB_HITS = """.. image:: https://img.shields.io/github/search/hendrikdutoit/{}/GitHub
    :alt: GitHub Searches

"""
_INDEX_RST_BADGE_GITHUB_LICENSE = """.. image:: https://img.shields.io/github/license/hendrikdutoit/{}
    :alt: License

"""
_INDEX_RST_BADGE_GITHUB_ISSUES = """.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/{}
    :alt: GitHub issues

"""
_INDEX_RST_BADGE_GITHUB_PRE_COMMIT = """.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/{0}/Pre-Commit
    :alt: GitHub Actions - Pre-Commit
    :target: https://github.com/hendrikdutoit/{0}/actions/workflows/pre-commit.yaml

"""
_INDEX_RST_BADGE_GITHUB_RELEASE = """.. image:: https://img.shields.io/github/v/release/hendrikdutoit/{}
    :alt: GitHub release (latest by date)

"""
_INDEX_RST_BADGE_PYPI_VERSION = """.. image:: https://img.shields.io/testpypi/v/{}
    :alt: PyPi

"""
_INDEX_RST_BADGE_PYPI_DL = """.. image:: https://img.shields.io/pypi/dm/{}
    :alt: PyPI - Downloads

"""
_INDEX_RST_BADGE_PYPI_STATUS = """.. image:: https://img.shields.io/pypi/status/{}
    :alt: PyPI - Status

"""
_INDEX_RST_BADGE_PYPI_WHEEL = """.. image:: https://img.shields.io/pypi/wheel/{}
    :alt: PyPI - Wheel

"""
_INDEX_RST_BADGE_PYVERSIONS = """.. image:: https://img.shields.io/pypi/pyversions/{}
    :alt: PyPI - Python Version

"""
_INDEX_RST_CONTENTS = """.. ======================================================
.. This file is auto generated by PackageIt. Any changes
.. to it will be over written
.. ======================================================

===============================
{0}
===============================

.. image:: https://img.shields.io/pypi/status/{0}
    :alt: PyPI - Status

.. image:: https://img.shields.io/pypi/wheel/{0}
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/{0}
    :alt: PyPI - Python Version

.. image:: https://img.shields.io/github/v/release/hendrikdutoit/{0}
    :alt: GitHub release (latest by date)

.. image:: https://img.shields.io/github/license/hendrikdutoit/{0}
    :alt: License

.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/{0}
    :alt: GitHub issues

.. image:: https://img.shields.io/pypi/dm/{0}
    :alt: PyPI - Downloads

.. image:: https://img.shields.io/github/search/hendrikdutoit/{0}/GitHub
    :alt: GitHub Searches

.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/{0}
    :alt: CodeCov
    :target: https://app.codecov.io/gh/hendrikdutoit/{0}

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/{0}/Pre-Commit
    :alt: GitHub Actions - Pre-Commit
    :target: https://github.com/hendrikdutoit/{0}/actions/workflows/pre-commit.yaml

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/{0}/CI
    :alt: GitHub Actions - CI
    :target: https://github.com/hendrikdutoit/{0}/actions/workflows/ci.yaml

.. image:: https://img.shields.io/testpypi/v/{0}
    :alt: PyPi

Project Header Description (default ini)

    Project long description goes in here (default ini)

------------
Installation
------------

.. code-block:: bash

    $ pip install .

-----
Usage
-----

.. code-block:: bash

    Insert text in Usage.rst

-------
Support
-------

.. code-block:: bash

    Insert text in Support.rst

.. toctree::
    :maxdepth: 2
    :caption: Contents
    :numbered:

    conventions
    api
    donotexist

"""
_PROJECT_CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Topic :: Software Development",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.10",
]
_PROJECT_NAME = "PackageItTest"
_RELEASE_YAML_PROD = """name: Build distribution

on: [push, pull_request]

jobs:
  ReleaseToPyPi:
    runs-on: "ubuntu-latest"

    steps:
      - name: Checkout source
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        uses: actions/setup-python@v1
        with:
          python-version: 3.9

      - name: Install build dependencies
        run: python -m pip install build wheel

      - name: Build distributions
        shell: bash -l {0}
        run: python -m build

      - name: Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: __token__
          password: ${{ secrets.PYPI_API_TOKEN }}
          repository_url: https://upload.pypi.org/legacy/
          verbose: true
"""
_RELEASE_YAML_TEST = """name: Build distribution

on: [push, pull_request]

jobs:
  ReleaseToPyPi:
    runs-on: "ubuntu-latest"

    steps:
      - name: Checkout source
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        uses: actions/setup-python@v1
        with:
          python-version: 3.9

      - name: Install build dependencies
        run: python -m pip install build wheel

      - name: Build distributions
        shell: bash -l {0}
        run: python -m build

      - name: Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: __token__
          password: ${{ secrets.TEST_PYPI_API_TOKEN }}
          repository_url: https://test.pypi.org/legacy/
          verbose: true
"""
_CONFIG_CFG_CONTENTS = """
[metadata]
version = 1.1.1

[tool:pytest]
addopts = --ignore-glob=*/VersionArchive --ignore-glob=*/Archive  --cov-report=html

[flake8]
exclude = __init__.py, VersionArchive/, Archive/
max-line-length = 120
"""


class WorkingDir:
    def __init__(self):
        self.dir = Path(mkdtemp(prefix="packageit_"))


class EnvSetUp:
    def __init__(self, p_make_project_ini=False, p_static_name=False):
        self.project_name = self.make_project_name(p_static_name)
        self.anchor_dir = WorkingDir().dir
        self.classifiers = _CLASSIFIERS
        self.external_arc_dir = self.anchor_dir / "external_archive"
        self.external_arc_dir.mkdir(parents=True)
        self.index_rst_badge_codecov = _INDEX_RST_BADGE_CODECOV.format(
            self.project_name
        )
        self.index_rst_badge_github_ci = _INDEX_RST_BADGE_GITHUB_CI.format(
            self.project_name
        )
        self.index_rst_badge_github_license = _INDEX_RST_BADGE_GITHUB_LICENSE.format(
            self.project_name
        )
        self.index_rst_badge_github_hits = _INDEX_RST_BADGE_GITHUB_HITS.format(
            self.project_name
        )
        self.index_rst_badge_github_issues = _INDEX_RST_BADGE_GITHUB_ISSUES.format(
            self.project_name
        )
        self.index_rst_badge_github_pre_commit = (
            _INDEX_RST_BADGE_GITHUB_PRE_COMMIT.format(self.project_name)
        )
        self.index_rst_badge_github_release = _INDEX_RST_BADGE_GITHUB_RELEASE.format(
            self.project_name
        )
        self.index_rst_badge_pypi_version = _INDEX_RST_BADGE_PYPI_VERSION.format(
            self.project_name
        )
        self.index_rst_badge_pypi_dl = _INDEX_RST_BADGE_PYPI_DL.format(
            self.project_name
        )
        self.index_rst_badge_pypi_status = _INDEX_RST_BADGE_PYPI_STATUS.format(
            self.project_name
        )
        self.index_rst_badge_pypi_wheel = _INDEX_RST_BADGE_PYPI_WHEEL.format(
            self.project_name
        )
        self.index_rst_badge_pyversions = _INDEX_RST_BADGE_PYVERSIONS.format(
            self.project_name
        )
        self.index_rst_contents = _INDEX_RST_CONTENTS.format(self.project_name)
        self.project_classifiers = _PROJECT_CLASSIFIERS
        self.packageit_ini_pth = self.make_packageit_ini()
        self.project_ini_pth = None
        self.release_yaml_prod = _RELEASE_YAML_PROD
        self.release_yaml_test = _RELEASE_YAML_TEST
        self.token_dir = Path("d:\\", "dropbox", "lib", "SSHKeys")
        self.token_gh_pth = self.token_dir / "github_token.txt"
        self.token_pypi_pth = self.token_dir / "PYPI_API_TOKEN.txt"
        self.token_testpypi_pth = self.token_dir / "TEST_PYPI_API_TOKEN.txt"
        self.token_rtd_pth = self.token_dir / "readthedocs_token.txt"

        if p_make_project_ini:
            self.project_ini_pth = self.make_project_ini()

    def create_mock_files(self):
        project_root_dir = self.anchor_dir / self.project_name
        src_dir = project_root_dir / "src" / self.project_name.lower()
        if not src_dir.exists():
            src_dir.mkdir(parents=True)
        (src_dir / "{}.py".format(self.project_name.lower())).write_text(
            "Test file\nThis file is included"
        )
        (src_dir / "{}.pyc".format(self.project_name.lower())).write_text(
            "Test file\nThis file is excluded"
        )
        (src_dir / "{}.ini".format(self.project_name.lower())).write_text("[Folders]\n")
        (project_root_dir / "setup.cfg").write_text(_CONFIG_CFG_CONTENTS)
        pass

    def make_packageit_ini(self):
        """Make INI file for testing"""
        packageit_ini_pth = self.anchor_dir / "pimt.ini"
        ini = configparserext.ConfigParserExt()
        ini["Classifiers"] = {
            "DevStatus": "Development Status :: 1 - Planning",
            "IntendedAudience002": "Intended Audience :: Developers",
            "IntendedAudience013": "Intended Audience :: System Administrators",
            "Topic013": "Topic :: Software Development",
            "Topic027": "Topic :: System :: Systems Administration",
            "License": "License :: OSI Approved :: MIT License",
            "ProgrammingLanguage001": "Programming Language :: Python :: 3.0",
            "ProgrammingLanguage010": "Programming Language :: Python :: 3.9",
            "ProgrammingLanguage011": "Programming Language :: Python :: 3.10",
        }
        ini["Coverage"] = {"Omit010": "setup.py"}
        ini["Detail"] = {
            "Author": "Ann Other",
            "AuthorEmail": "ann.other@testmodule.com",
            "HeaderDescription": "Project Header Description (default ini)",
            "LongDescription": "Project long description goes in here (default ini)",
            "{}ProjectAnchorDir".format(get_os()): self.anchor_dir,
            "{}ProjectIniDir".format(get_os()): Path(self.anchor_dir, "ini"),
            "PythonRequires": ">=3.6",
            "Url": "www.{}.com".format(self.project_name.lower()),
            "Type": "Module",
        }

        ini["flake8"] = {
            "exclude": "__init__.py, VersionArchive /, Archive /",
            "max-line-length": "120",
        }
        ini["General"] = {"Verbose": "Yes"}
        ini["Git"] = {
            "Enable": "Yes",
            #     'Include' : '*.py;*.ini;*.bat;*.sh',
            #     'Ignore'  : '/VersionArchive;.workspace/;__pycache__/;*.komodoproject;*.log'
        }
        ini["GitHub"] = {
            "BugTemplate": "templ_github_bug.md",
            "ConfigTemplate": "templ_github_config.yaml",
            "Enable": "Yes",
            "FeatureTemplate": "templ_github_feature.md",
            "TokenFileName": "github_token.txt",
            "UserName": "hendrikdutoit",
            "Url": "https: // github.com",
        }
        ini["Import"] = {
            "ReWrite": "Yes",
            "Prod001": "pypi;termcolor",
            "Test010": "pypi;pip",
            "Test020": "pypi;wheel",
            "Test030": "pypi;pre-commit",
            "Test040": "pypi;pytest",
            "Test050": "pypi;beetools",
            "Test060": "pypi;pytest-cov",
            "Test070": "pypi;sphinx",
            "Test080": "pypi;sphinx-autobuild",
            "Test090": "pypi;sphinx-rtd-theme",
            "Test100": "pypi;black",
            "Test110": "pypi;build",
            "Test120": "pypi;configparserext",
            "Test130": "pypi;pygithub",
        }
        ini["Install Apps"] = {"App01": "pre-commit install"}
        ini["LogLevels"] = {"Default": 0, "Console": 0, "File": 0}
        ini["PyPi"] = {
            "Publishing": "GitHub",  # No | GitHub| Twine
            "Repository": "testpypi",
            "TokenFileNamePyPi": "PYPI_API_TOKEN.txt",
            "TokenFileNameTestPyPi": "TEST_PYPI_API_TOKEN.txt",
        }
        ini["ReadMe"] = {
            "EnableTesting": "Yes",
            "EnableDeveloping": "Yes",
            "EnableReleasing": "Yes",
        }
        ini["ReadTheDocs"] = {
            "Enable": "Yes",
            "ConfigTemplate": "readthedocs_def_.readthedocs_template.yaml",
            "NewProjectTemplate": "readthedocs_def_newproject_template.json",
            "TokenFileName": "readthedocs_token.txt",
        }
        ini["Sphinx"] = {
            "Enable": "Yes",
            "ConfPyInstr001": "extensions = ['sphinx.ext.autodoc']",
            "ConfPyInstr010": "templates_path = ['_templates']",
            "ConfPyInstr020": "language = 'en'",
            "ConfPyInstr030": "exclude_patterns = []",
            "ConfPyInstr040": "html_theme = 'sphinx_rtd_theme'",
            "ConfPyInstr050": "html_static_path = ['_static']",
            "AddSection001": "Installation",
            "AddSection010": "Usage",
            "AddSection020": "Support",
            "AddContent001": "conventions",
            "AddContent010": "api",
            "AddContent020": "donotexist",
        }
        ini["tool:pytest"] = {
            "addopts": """--ignore-glob=*/VersionArchive --ignore-glob=*/Archive  --cov-report=html"""
        }
        ini["VEnv"] = {
            "Enable": "Yes",
            "Upgrade": "Yes",
            "ReinstallVEnv": "No",
            "{}VEnvBaseFolder".format(get_os()): self.anchor_dir,
            "{}VEnvAnchorDir".format(get_os()): self.anchor_dir / "venv",
        }
        with open(packageit_ini_pth, "w") as ini_file:
            ini.write(ini_file)
        return packageit_ini_pth

    def make_project_ini(self):
        """Make a project specific ini file"""
        project_ini_pth = Path(
            self.packageit_ini_pth.parents[0],
            self.project_name,
            ".packageit",
            "packageit.ini",
        )
        if not project_ini_pth.parents[0].exists():
            project_ini_pth.parents[0].mkdir(parents=True)
        ini = configparserext.ConfigParserExt(inline_comment_prefixes="#")
        ini["Classifiers"] = {
            "DevStatus": "Development Status :: 1 - Planning",
            "IntendedAudience002": "Intended Audience :: Developers",
            "IntendedAudience003": "Intended Audience :: System Administrators",
            "Topic013": "Topic :: Software Development",
            "License": "License :: OSI Approved :: MIT License",
            "ProgrammingLanguage001": "Programming Language :: Python :: 3.0",
            "ProgrammingLanguage011": "Programming Language :: Python :: 3.10",
        }
        ini["Coverage"] = {}
        ini["Detail"] = {
            "Author": "Hendrik du Toit",
            "AuthorEmail": "hendrik@brightedge.co.za",
            "HeaderDescription": "Project Header Description (project ini)",
            "Import01": "import sys",
            "LongDescription": "Project long description goes in here (project ini)",
            "Url": "www.brightedge.co.za",
        }
        ini["flake8"] = {
            "exclude": "__init__.py, VersionArchive /, Archive /",
            "max-line-length": "120",
        }
        ini["General"] = {"Verbose": "Yes"}
        ini["Git"] = {}
        ini["GitHub"] = {"UserName": "hendrikdutoit", "Url": "https: // github.com"}
        ini["Import"] = {}
        ini["Install Apps"] = {}
        ini["LogLevels"] = {}
        ini["ReadMe"] = {
            "EnableTesting": "Yes",
            "EnableDeveloping": "Yes",
            "EnableReleasing": "Yes",
        }
        ini["PyPi"] = {}
        ini["Sphinx"] = {}
        ini["tool:pytest"] = {
            "addopts": """--ignore-glob = */VersionArchive --ignore-glob = */Archive --cov-report = html"""
        }
        ini["VEnv"] = {}
        with open(project_ini_pth, "w") as project_ini_file:
            ini.write(project_ini_file)
        return project_ini_pth

    def make_project_name(self, p_static_name):
        if not p_static_name:
            return "{}{}".format(
                _PROJECT_NAME, datetime.datetime.now().strftime("%y%m%d%H%M%S%f")
            )
        else:
            return _PROJECT_NAME

    def reduce_import_list(self):
        ini = configparserext.ConfigParserExt(inline_comment_prefixes="#")
        ini.read([self.packageit_ini_pth])
        ini.remove_section("Import")
        ini.add_section("Import")
        ini.set("Import", "ReWrite", "Yes")
        ini.set("Import", "Test01", "pypi;pre-commit")
        with open(self.packageit_ini_pth, "w") as project_ini_file:
            ini.write(project_ini_file)
        pass


@pytest.fixture
def setup_env_self_destruct():
    """Set up the environment base structure"""
    setup_env = EnvSetUp()
    yield setup_env
    rm_tree(setup_env.anchor_dir, p_crash=False)


@pytest.fixture
def setup_env_self_destruct_with_static_name():
    """Set up the environment base structure"""
    setup_env = EnvSetUp(p_static_name=True)
    yield setup_env
    rm_tree(setup_env.anchor_dir, p_crash=False)


@pytest.fixture
def setup_env_with_project_ini_self_destruct():
    """Set up the environment base structure"""
    setup_env = EnvSetUp(p_make_project_ini=True)
    yield setup_env
    rm_tree(setup_env.anchor_dir, p_crash=False)


@pytest.fixture
def working_dir_self_destruct():
    """Set up the environment base structure"""
    working_dir = WorkingDir()
    yield working_dir
    rm_tree(working_dir.dir, p_crash=False)
