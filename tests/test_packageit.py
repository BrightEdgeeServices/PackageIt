"""Testing packageit__init__()

Testing
1. The following packageit methods use a virtual environment.  Tests containing
one of these methods must create a virtual environment.
- create_sphinx_docs
- do_pytest
- format_code
- git_commit
- install_editable_package
- install_prereq_apps_in_venv
- install_prereq_modules_in_venv
- make_wheels
- setup_sphinx

"""


from pathlib import Path
import requests
import time
from beetools import Archiver, get_os
import configparserext

# from git import Repo, exc as git_exc
# from github import Github, GithubException as GH_Exc
from packageit import packageit

_DESC = __doc__.split("\n")[0]
_PATH = Path(__file__)
_NAME = _PATH.stem


def change_ini(p_ini_pth, p_section, p_option, p_value):
    """Change settings in INI file"""
    ini = configparserext.ConfigParserExt()
    ini.read([p_ini_pth])
    if not ini.has_section(p_section):
        ini[p_section] = {}
    ini[p_section][p_option] = str(p_value)
    with open(p_ini_pth, "w") as ini_file:
        ini.write(ini_file)
    return p_ini_pth


def read_project_ini(p_ini_pth):
    """Read project specific ini file"""
    ini = configparserext.ConfigParserExt(inline_comment_prefixes="#")
    ini.read([p_ini_pth])
    return ini


def del_gh_repo(p_repo):
    time.sleep(1)
    p_repo.init_github_repo()


b_tls = Archiver(_DESC, _PATH)


class TestPackageIt:
    def test__init__(self, setup_env_self_destruct):
        """Testing packageit__init__()"""
        env_setup = setup_env_self_destruct

        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )

        assert p_it.success
        assert p_it.arc_extern_dir == env_setup.external_arc_dir
        assert p_it.gh_user is None
        assert p_it.github is None
        assert p_it.project_gh_token == env_setup.token_gh_pth.read_text().strip()
        assert p_it.ini_spec_pth is None
        assert p_it.logger_name is None
        assert p_it.origin is None
        assert p_it.packageit_ini_pth == env_setup.packageit_ini_pth

        assert p_it.project_anchor_dir == env_setup.anchor_dir

        assert p_it.project_author == "Ann Other"
        assert p_it.project_author_email == "ann.other@testmodule.com"

        assert p_it.project_classifiers == env_setup.classifiers
        assert p_it.project_code is None
        assert p_it.project_dir is None
        assert p_it.project_git_enable is True
        assert p_it.project_gh_enable is True
        assert (
            p_it.project_header_description
            == "Project Header Description (default ini)"
        )

        assert p_it.project_import_prod == [["pypi", "termcolor"]]
        assert p_it.project_import_rewrite is True
        assert p_it.project_import_test == [
            ["pypi", "pip"],
            ["pypi", "wheel"],
            ["pypi", "pre-commit"],
            ["pypi", "pytest"],
            ["pypi", "beetools"],
            ["pypi", "pytest-cov"],
            ["pypi", "sphinx"],
            ["pypi", "sphinx-autobuild"],
            ['pypi', 'sphinx-rtd-theme'],
            ["pypi", "black"],
            ["pypi", "build"],
            ["pypi", "configparserext"],
            ["pypi", "pygithub"],
        ]

        assert p_it.project_packageit_ini_pth == Path(
            env_setup.anchor_dir, env_setup.project_name, ".packageit", "packageit.ini"
        )
        assert p_it.project_install_apps == ["pre-commit install"]
        assert (
            p_it.project_long_description
            == "Project long description goes in here (default ini)"
        )
        assert p_it.project_name == env_setup.project_name
        assert p_it.project_python_requires == ">=3.6"

        assert p_it.project_readme_rst is None
        assert p_it.project_readme_developing_enable
        assert p_it.project_readme_releasing_enable
        assert p_it.project_readme_testing_enable

        assert p_it.project_readthedocs_enable

        assert p_it.project_root_dir == Path(
            env_setup.anchor_dir, env_setup.project_name
        )

        assert (
            p_it.project_readthedocs_config_template
            == "readthedocs_def_.readthedocs_template.yaml"
        )
        assert (
            p_it.project_readthedocs_newproject_template
            == "readthedocs_def_newproject_template.json"
        )

        assert p_it.project_tests_dir == Path(
            env_setup.anchor_dir, env_setup.project_name, "tests"
        )

        assert p_it.project_version.version == "0.0.0"

        assert p_it.project_versionarchive_dir == Path(
            env_setup.anchor_dir, env_setup.project_name, "VersionArchive"
        )

        assert p_it.project_pypi_publishing == "GitHub"
        assert p_it.project_pypi_repository == "testpypi"

        assert p_it.project_sphinx_enable is True
        assert p_it.project_sphinx_conf_py_inst == [
            "extensions = ['sphinx.ext.autodoc']",
            "templates_path = ['_templates']",
            "language = 'en'",
            "exclude_patterns = []",
            "html_theme = 'sphinx_rtd_theme'",
            "html_static_path = ['_static']",
        ]

        assert p_it.project_type == "Module"

        assert p_it.project_url == "www.{}.com".format(p_it.project_name.lower())

        assert p_it.project_venv_dir is None
        assert p_it.project_venv_enable is True
        assert p_it.project_venv_name == env_setup.project_name
        assert p_it.project_venv_root_dir == env_setup.anchor_dir / "venv"
        assert p_it.project_venv_upgrade is True

        assert p_it.project_wheels is None

        assert p_it.pypi_curr_token_name == "TEST_PYPI_API_TOKEN"
        assert p_it.pypi_prod_token_name == "PYPI_API_TOKEN"
        assert p_it.pypi_test_token_name == "TEST_PYPI_API_TOKEN"

        assert (
            p_it.pyproject_toml_pth
            == env_setup.anchor_dir / env_setup.project_name / "pyproject.toml"
        )
        assert p_it.git_repo is None
        assert p_it.templ_dir == p_it.packageit_dir / "templates"
        assert p_it.verbose
        pass

    def test_add_forced_repo_files(self, setup_env_with_project_ini_self_destruct):
        """Testing packageit_add__forced_repo_files()"""
        env_setup = setup_env_with_project_ini_self_destruct
        # env_setup.del_github_repo()

        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )

        assert p_it
        p_it_dup = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it_dup.create_scaffolding()
        p_it_dup.create_git_ignore()
        env_setup.create_mock_files()

        # assert p_it.add_forced_repo_files() == [
        #     str(Path(env_setup.anchor_dir, env_setup.project_name, ".gitignore"))
        # ]
        assert p_it.add_forced_repo_files() == []
        pass

    def test_add_repo_files(self, setup_env_with_project_ini_self_destruct):
        """Testing packageit_add_repo_files()"""
        env_setup = setup_env_with_project_ini_self_destruct
        # env_setup.del_github_repo()

        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_git()
        env_setup.create_mock_files()

        assert p_it.add_repo_files() == [
            '.gitignore',
            ".packageit/packageit.ini",
            "setup.cfg",
            f"src/{env_setup.project_name.lower()}/{env_setup.project_name.lower()}.ini",
            f"src/{env_setup.project_name.lower()}/{env_setup.project_name.lower()}.py",
        ]
        pass

    def test_add_sphinx_index_contents(self, setup_env_self_destruct):
        """Testing packageit_add_sphinx_index_contents()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )

        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.project_readme_rst = packageit.RSTBuilder(_NAME, p_it.project_readme_pth)
        p_it.project_sphinx_index_rst = packageit.RSTBuilder(
            _NAME, p_it.project_sphinx_index_rst_pth
        )
        (p_it.project_sphinx_source_dir / "conventions.rst").write_text(
            "===========\nConventions\n===========\n\n1. Convention 1\n2. Next convention\n\n"
        )
        p_it.add_sphinx_index_contents()

        assert p_it.project_sphinx_index_rst.elements == {
            0: {
                "Type": "TocTree",
                "Text": ".. toctree::\n    :maxdepth: 2\n    :caption: Contents\n"
                "    :numbered:\n\n    conventions\n    api\n    donotexist\n\n",
                "Items": ["conventions", "api", "donotexist"],
            }
        }
        pass

    def test_add_sphinx_index_sections(self, setup_env_self_destruct):
        """Testing packageit_add_sphinx_index_sections()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )

        p_it.create_scaffolding()
        p_it.project_readme_rst = packageit.RSTBuilder(_NAME, p_it.project_readme_pth)
        p_it.project_sphinx_index_rst = packageit.RSTBuilder(
            _NAME, p_it.project_sphinx_index_rst_pth
        )
        (p_it.project_sphinx_source_dir / "Usage.rst").write_text(
            ">>> This is how you use {}".format(p_it.project_name)
        )
        p_it.add_sphinx_index_sections()

        assert p_it.project_sphinx_index_rst.elements == {
            0: {
                "Type": "SecondLevelTitle",
                "Text": "------------\nInstallation\n------------\n\n",
            },
            1: {
                "Type": "CodeBlock",
                "Text": ".. code-block:: bash\n\n    $ pip install .\n\n",
            },
            2: {"Type": "SecondLevelTitle", "Text": "-----\nUsage\n-----\n\n"},
            3: {
                "Type": "CodeBlock",
                "Text": ".. code-block:: bash\n\n    >>> This is how you use {}\n\n".format(
                    env_setup.project_name
                ),
            },
            4: {"Type": "SecondLevelTitle", "Text": "-------\nSupport\n-------\n\n"},
            5: {
                "Type": "CodeBlock",
                "Text": ".. code-block:: bash\n\n    Insert text in Support.rst\n\n",
            },
        }
        pass

    def test_create_conftest_py(self, setup_env_self_destruct):
        """Testing packageit_create_coveragerc()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert p_it.create_conftest_py()
        pass

    def test_create_coveragerc(self, setup_env_self_destruct):
        """Testing packageit_create_coveragerc()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert p_it.create_coveragerc().exists()
        pass

    def test_create_git_ignore(self, setup_env_with_project_ini_self_destruct):
        """Testing create_git_ignore()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()

        assert Path(p_it.project_src_dir / ".gitignore")
        pass

    def test_create_github_bug_templ(self, setup_env_self_destruct):
        """Testing packageit_create_github_bug_templ()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert p_it.create_github_bug_templ().exists()
        pass

    def test_create_github_ci_yaml(self, setup_env_self_destruct):
        """Testing packageit_create_github_ci_yaml()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert p_it.create_github_ci_yaml().exists()
        pass

    def test_create_github_config_templ(self, setup_env_self_destruct):
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert p_it.create_github_config_templ().exists()
        pass

    def test_create_github_feature_templ(self, setup_env_self_destruct):
        """Testing packageit_create_github_feature_templ()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert p_it.create_github_feature_templ().exists()
        pass

    def test_create_github_release_yml_prod(self, setup_env_self_destruct):
        """Testing packageit_create_github_release_yml()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.get_project_details()
        p_it.create_scaffolding()
        p_it.create_github_release_yml()

        change_ini(p_it.project_packageit_ini_pth, "PyPi", "Repository", "pypi")
        p_it.read_project_detail_specific()
        dest_pth = p_it.create_github_release_yml()
        contents = dest_pth.read_text()

        assert dest_pth.exists()
        assert contents == env_setup.release_yaml_prod
        p_it.project_pypi_publishing = 'No'
        dest_pth = p_it.create_github_release_yml()
        assert not dest_pth
        pass

    def test_create_github_release_yml_test(self, setup_env_self_destruct):
        """Testing packageit_create_github_release_yml()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        dest_pth = p_it.create_github_release_yml()
        contents = dest_pth.read_text()

        assert dest_pth.exists()
        assert contents == env_setup.release_yaml_test
        p_it.project_pypi_publishing = 'No'
        dest_pth = p_it.create_github_release_yml()
        assert not dest_pth
        pass

    def test_create_license(self, setup_env_self_destruct):
        """Testing packageit_create_license()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert p_it.create_license().exists()
        pass

    def test_create_readme(self, setup_env_self_destruct):
        """Testing packageit_create_readme()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_source_code_py()

        assert (
            p_it.create_readme()
            == env_setup.anchor_dir / env_setup.project_name / "README.rst"
        )
        assert p_it.project_readme_rst.contents == ""
        assert p_it.project_readme_rst.element_cntr == 14
        assert p_it.project_readme_rst.elements == {
            0: {
                "Type": "Paragraph",
                "Text": "Project Header Description (default ini)\n\n",
            },
            1: {
                "Type": "Paragraph",
                "Text": "    Project long description goes in here (default ini)\n\n",
            },
            2: {"Type": "FirstLevelTitle", "Text": "=======\nTesting\n=======\n\n"},
            3: {
                "Type": "Paragraph",
                "Text": "This project uses ``pytest`` to run tests and also to test docstring examples.\n\n",
            },
            4: {"Type": "Paragraph", "Text": "Install the test dependencies.\n\n"},
            5: {
                "Type": "CodeBlock",
                "Text": ".. code-block:: bash\n\n    $ pip install -r requirements_test.txt\n\n",
            },
            6: {"Type": "Paragraph", "Text": "Run the tests.\n\n"},
            7: {
                "Type": "CodeBlock",
                "Text": ".. code-block:: bash\n\n    $ pytest tests\n    === XXX passed in SSS seconds ===\n\n",
            },
            8: {
                "Type": "FirstLevelTitle",
                "Text": "==========\nDeveloping\n==========\n\n",
            },
            9: {
                "Type": "Paragraph",
                "Text": "This project uses ``black`` to format code and ``flake8`` for linting. We also support "
                + "``pre-commit`` to ensure these have been run. To configure your local environment please "
                + "install these development dependencies and set up the commit hooks.\n\n",
            },
            10: {
                "Type": "CodeBlock",
                "Text": ".. code-block:: bash\n\n    $ pip install black flake8 pre-commit\n"
                + "    $ pre-commit install\n\n",
            },
            11: {
                "Type": "FirstLevelTitle",
                "Text": "=========\nReleasing\n=========\n\n",
            },
            12: {
                "Type": "Paragraph",
                "Text": "Releases are published automatically when a tag is pushed to GitHub.\n\n",
            },
            13: {
                "Type": "CodeBlock",
                "Text": '''.. code-block:: bash\n\n    # Set next version number\n    export RELEASE = x.x.x\n    \n'''
                + '''    # Create tags\n    git commit --allow -empty -m "Release $RELEASE"\n'''
                + '''    git tag -a $RELEASE -m "Version $RELEASE"\n    \n    # Push\n'''
                + '''    git push upstream --tags\n\n''',
            },
        }
        pass

    def test_create_readthedocs_project_new(self, setup_env_self_destruct):
        """Testing packageit_upload_to_enabled()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_venv()
        p_it.create_git_ignore()
        # p_it.init_github()
        # p_it.init_github_repo()
        # p_it.init_github_master_branch()
        # p_it.init_git()
        # p_it.marry_git_github()
        p_it.install_prereq_apps_in_venv()
        p_it.setup_sphinx()

        p_it.create_release()
        # p_it.github_format_titles()
        # p_it.github_sync_release_notes()
        p_it.create_sphinx_conf_py()
        p_it.create_source_code_py()
        p_it.create__init__()
        p_it.create_source_code_ini()
        p_it.create_license()
        p_it.create_test_code()
        # p_it.create_conftest_py()
        p_it.create_pyproject_toml()
        # p_it.create_github_ci_yaml()
        # p_it.create_github_bug_templ()
        # p_it.create_github_config_templ()
        # p_it.create_github_feature_templ()
        p_it.create_setup_cfg()
        p_it.create_readme()
        p_it.create_manifest()
        # p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        # p_it.create_requirements("requirements_test.txt", p_it.project_import_test)
        p_it.create_coveragerc()
        # p_it.add_badges()
        p_it.project_readme_rst.write_text()
        p_it.create_sphinx_index_rst()
        p_it.project_sphinx_index_rst.write_text()
        p_it.create_sphinx_docs()
        p_it.format_code()
        # p_it.create_github_release_yml()
        # p_it.create_git_pre_commit_config_yaml()
        # p_it.create_github_pre_commit_yaml()
        p_it.create_readthedocs_yaml()
        # p_it.update_to_latest_version()
        p_it.cleanup()
        # p_it.install_editable_package()
        # p_it.do_pytest()
        # p_it.git_commit()
        # p_it.git_push()
        p_it.make_wheels()
        # p_it.upload_to_pypi()
        # p_it.git_repo.close()
        p_it.create_readthedocs_project()
        # p_it.zip_project()  # Zip after changes

        url = "https://readthedocs.org/api/v3/projects/{}/".format(
            p_it.project_name.lower()
        )
        # url = 'https://readthedocs.org/api/v3/projects/'
        headers = {"Authorization": f"token {p_it.rtd_token}"}
        response = requests.get(url, headers=headers).json()
        assert len(response)

        # p_it.gh_repo.delete()
        pass

    def test_create_readthedocs_project_existing(
        self, setup_env_self_destruct_with_static_name
    ):
        """Testing packageit_upload_to_enabled()
        This test has to be improved because currently it does not really
        test if an existing entry has been updated."""
        env_setup = setup_env_self_destruct_with_static_name
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.run()

        url = "https://readthedocs.org/api/v3/projects/{}/".format(
            p_it.project_name.lower()
        )
        # url = 'https://readthedocs.org/api/v3/projects/'
        headers = {"Authorization": f"token {p_it.rtd_token}"}
        response = requests.get(url, headers=headers).json()
        assert len(response)

        pass

    def test_create_readthedocs_yaml(self, setup_env_self_destruct):
        """Testing packageit_create_readthedocs_yaml()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert p_it.create_readthedocs_yaml().exists()
        assert (p_it.project_sphinx_docs_dir / "requirements_docs.txt").exists()
        p_it.project_readthedocs_enable = False
        assert not p_it.create_readthedocs_yaml()
        pass

    def test_create_release(self, setup_env_with_project_ini_self_destruct):
        """Testing create_scaffolding_package()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "Detail", "Type", "Package")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_release()
        assert p_it.project_release.rel_notes == {
            "0": {
                "0": {
                    "0": {
                        "Title": "Version 0.0.0",
                        "Description": [
                            "Creation of the project",
                            "List all the changes to the project here.",
                            "Changes listed here will be in the release notes under the above heading.",
                        ],
                    }
                }
            }
        }
        assert p_it.project_release.src_pth.exists()
        pass

    def test_create_requirements(self, setup_env_self_destruct):
        """Testing create_requirements()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        req_pth = p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        assert req_pth.exists()
        pass

    def test_create_scaffolding_module(self, setup_env_with_project_ini_self_destruct):
        """Testing create_scaffolding_module()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert (
            p_it.project_dir
            == env_setup.anchor_dir
            / env_setup.project_name
            / "src"
            / env_setup.project_name.lower()
        )
        assert p_it.project_dir.exists()
        assert p_it.project_packageit_ini_pth == Path(
            env_setup.anchor_dir, env_setup.project_name, ".packageit", "packageit.ini"
        )
        assert p_it.project_packageit_ini_pth.exists()
        assert (
            p_it.project_src_dir
            == env_setup.anchor_dir / env_setup.project_name.lower() / "src"
        )
        assert p_it.project_src_dir.exists()
        assert (
            p_it.project_tests_dir
            == env_setup.anchor_dir / env_setup.project_name / "tests"
        )
        assert p_it.project_tests_dir.exists()
        assert (
            p_it.project_versionarchive_dir
            == env_setup.anchor_dir / env_setup.project_name / "VersionArchive"
        )
        assert p_it.project_versionarchive_dir.exists()
        pass

    def test_create_scaffolding_package(self, setup_env_with_project_ini_self_destruct):
        """Testing create_scaffolding_package()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "Detail", "Type", "Package")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert (
            p_it.project_dir
            == env_setup.anchor_dir
            / env_setup.project_name
            / env_setup.project_name.lower()
        )
        assert p_it.project_dir.exists()
        assert p_it.project_packageit_ini_pth == Path(
            env_setup.anchor_dir, env_setup.project_name, ".packageit", "packageit.ini"
        )
        assert p_it.project_packageit_ini_pth.exists()
        assert (
            p_it.project_src_dir
            == env_setup.anchor_dir
            / env_setup.project_name
            / env_setup.project_name.lower()
        )
        assert p_it.project_src_dir.exists()
        assert (
            p_it.project_tests_dir
            == env_setup.anchor_dir / env_setup.project_name / "tests"
        )
        assert p_it.project_tests_dir.exists()
        assert (
            p_it.project_versionarchive_dir
            == env_setup.anchor_dir / env_setup.project_name / "VersionArchive"
        )
        assert p_it.project_versionarchive_dir.exists()

    def test_create_setup_cfg_module(self, setup_env_self_destruct):
        """Testing packageit_create_setup_py()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_setup_cfg().exists()

        assert p_it.project_setup_cfg.options('options') == [
            'install_requires',
            'setup_requires',
            'tests_require',
            'package_dir',
            'packages',
        ]
        pass

    def test_create_setup_cfg_package(self, setup_env_self_destruct):
        """Testing packageit_create_setup_py()"""
        env_setup = setup_env_self_destruct
        change_ini(env_setup.packageit_ini_pth, "Detail", "Type", "Package")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()

        assert p_it.create_setup_cfg().exists()
        pass

    def test_create_source_code_ini_module(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing create_source_code_py_module()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_source_code_ini()

        assert not Path(
            p_it.project_src_dir / "{}.ini".format(env_setup.project_name.lower())
        ).exists()
        pass

    def test_create_source_code_ini_package(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing create_source_code_ini_package()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "Detail", "Type", "Package")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_source_code_ini()

        assert Path(
            p_it.project_src_dir / "{}.ini".format(env_setup.project_name.lower())
        ).exists()
        pass

    def test_create_source_code_py_module(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing create_source_code_py_module()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_source_code_py()

        assert Path(
            p_it.project_src_dir
            / "{}".format(env_setup.project_name.lower())
            / "{}.py".format(env_setup.project_name.lower())
        ).exists()
        pass

    def test_create_source_code_py_package(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing create_source_code_py_package()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "Detail", "Type", "Package")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_source_code_py()

        assert Path(
            p_it.project_src_dir / "{}.py".format(env_setup.project_name.lower())
        ).exists()
        pass

    def test_create_sphinx_conf_py(self, setup_env_self_destruct):
        """Testing packageit_create_sphinx_conf_py()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        # p_it.create_venv()
        # p_it.create_setup_py()
        p_it.create_pyproject_toml()
        p_it.create_source_code_py()
        p_it.create_readme()
        p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        p_it.create_requirements("requirements_test.txt", p_it.project_import_test)
        p_it.project_readme_rst.write_text()
        p_it.install_prereq_modules_in_venv()
        p_it.setup_sphinx()

        assert p_it.create_sphinx_conf_py()
        pass

    def test_create_sphinx_docs(self, setup_env_self_destruct):
        """Testing packageit_create_sphinx_docs()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        # p_it.create_venv()
        p_it.create_git_ignore()
        p_it.init_git()
        # p_it.create_setup_py()
        p_it.create_pyproject_toml()
        p_it.create_source_code_py()
        p_it.create_readme()
        p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        p_it.create_requirements("requirements_test.txt", p_it.project_import_test)
        p_it.project_readme_rst.write_text()
        p_it.install_prereq_modules_in_venv()
        p_it.install_prereq_apps_in_venv()
        p_it.setup_sphinx()
        p_it.create_sphinx_conf_py()
        p_it.add_badges()
        p_it.create_sphinx_index_rst()
        p_it.create_sphinx_index_rst().write_text()
        p_it.create_sphinx_docs()

        assert (
            p_it.project_root_dir / "docs" / "build" / "html" / "index.html"
        ).exists()
        pass

    def test_create_sphinx_index_rst(self, setup_env_self_destruct):
        """Testing packageit_create_sphinx_index_rst()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_source_code_py()
        p_it.create_readme()
        p_it.add_badges()
        p_it.create_sphinx_index_rst()
        p_it.create_sphinx_index_rst().write_text()

        assert p_it.project_sphinx_index_rst.elements == {
            0: {
                "Type": "Comment",
                "Text": ".. ======================================================\n",
            },
            1: {
                "Type": "Comment",
                "Text": ".. This file is auto generated by PackageIt. Any changes\n",
            },
            2: {"Type": "Comment", "Text": ".. to it will be over written\n"},
            3: {
                "Type": "Comment",
                "Text": ".. ======================================================\n\n",
            },
            4: {
                "Text": "===============================\n{}\n===============================\n\n".format(
                    env_setup.project_name
                ),
                "Type": "FirstLevelTitle",
            },
            5: {
                "Text": env_setup.index_rst_badge_pypi_status,
                "Type": "DirectiveImage",
            },
            6: {"Text": env_setup.index_rst_badge_pypi_wheel, "Type": "DirectiveImage"},
            7: {"Text": env_setup.index_rst_badge_pyversions, "Type": "DirectiveImage"},
            8: {
                "Text": env_setup.index_rst_badge_github_release,
                "Type": "DirectiveImage",
            },
            9: {
                "Text": env_setup.index_rst_badge_github_license,
                "Type": "DirectiveImage",
            },
            10: {
                "Text": env_setup.index_rst_badge_github_issues,
                "Type": "DirectiveImage",
            },
            11: {"Text": env_setup.index_rst_badge_pypi_dl, "Type": "DirectiveImage"},
            12: {
                "Text": env_setup.index_rst_badge_github_hits,
                "Type": "DirectiveImage",
            },
            13: {"Text": env_setup.index_rst_badge_codecov, "Type": "DirectiveImage"},
            14: {
                "Text": env_setup.index_rst_badge_github_pre_commit,
                "Type": "DirectiveImage",
            },
            15: {"Text": env_setup.index_rst_badge_github_ci, "Type": "DirectiveImage"},
            16: {
                "Text": env_setup.index_rst_badge_pypi_version,
                "Type": "DirectiveImage",
            },
            17: {
                "Text": "Project Header Description (default ini)\n\n",
                "Type": "Paragraph",
            },
            18: {
                "Text": "    Project long description goes in here (default ini)\n\n",
                "Type": "Paragraph",
            },
            19: {
                "Text": "------------\nInstallation\n------------\n\n",
                "Type": "SecondLevelTitle",
            },
            20: {
                "Text": ".. code-block:: bash\n\n    $ pip install .\n\n",
                "Type": "CodeBlock",
            },
            21: {"Text": "-----\nUsage\n-----\n\n", "Type": "SecondLevelTitle"},
            22: {
                "Text": ".. code-block:: bash\n\n    Insert text in Usage.rst\n\n",
                "Type": "CodeBlock",
            },
            23: {"Text": "-------\nSupport\n-------\n\n", "Type": "SecondLevelTitle"},
            24: {
                "Text": ".. code-block:: bash\n\n    Insert text in Support.rst\n\n",
                "Type": "CodeBlock",
            },
            25: {
                "Items": ["conventions", "api", "donotexist"],
                "Text": ".. toctree::\n    :maxdepth: 2\n    :caption: Contents\n    :numbered:\n\n    conventions\n"
                + "    api\n    donotexist\n\n",
                "Type": "TocTree",
            },
        }
        assert p_it.project_sphinx_index_rst.contents == env_setup.index_rst_contents
        assert p_it.project_sphinx_index_rst_pth.exists()
        pass

    def test_create_venv_not_exist_and_reinstall_no(self, setup_env_self_destruct):
        """Testing packageit_do_install_venv_not_exist_and_reinstall_no()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_venv()

        assert p_it.project_venv_dir == env_setup.anchor_dir / "venv" / "{}_env".format(
            env_setup.project_name
        )
        assert (p_it.project_venv_dir / "pyvenv.cfg").exists()
        pass

    def test_create_venv_not_exist_and_reinstall_yes(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing packageit_do_install_venv_not_exist_and_reinstall_yes()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        change_ini(env_setup.packageit_ini_pth, "VEnv", "ReinstallVEnv", "Yes")
        p_it.create_scaffolding()
        p_it.create_venv()

        assert p_it.project_venv_dir == env_setup.anchor_dir / "venv" / "{}_env".format(
            env_setup.project_name
        )
        assert (p_it.project_venv_dir / "pyvenv.cfg").exists()
        pass

    def test_create_venv_yes(self, setup_env_self_destruct):
        """Testing packageit_do_install_venv_simple()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_venv()

        assert p_it.project_venv_dir == env_setup.anchor_dir / "venv" / "{}_env".format(
            env_setup.project_name
        )
        assert (p_it.project_venv_dir / "pyvenv.cfg").exists()
        pass

    def test_do_pytest(self, setup_env_self_destruct):
        """Testing packageit_make_wheel()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_venv()
        p_it.install_prereq_modules_in_venv()
        p_it.create_git_ignore()
        p_it.init_git()
        p_it.install_prereq_apps_in_venv()
        p_it.create_source_code_py()
        p_it.create__init__()
        p_it.create_source_code_ini()
        # p_it.create_setup_py()
        p_it.create_setup_cfg()
        p_it.create_license()
        p_it.create_test_code()
        p_it.create_conftest_py()
        p_it.create_pyproject_toml()
        p_it.create_readme()
        p_it.create_manifest()
        p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        p_it.create_requirements("requirements_test.txt", p_it.project_import_test)
        p_it.project_readme_rst.write_text()
        p_it.install_editable_package()
        p_it.format_code()

        assert p_it.do_pytest() == 0
        pass

    def test_format_code(self, setup_env_self_destruct):
        """Testing packageit_format_code()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.create_venv()
        p_it.create_scaffolding()
        p_it.create_source_code_py()
        # p_it.create_setup_py()
        p_it.create_pyproject_toml()

        assert p_it.format_code() == 0
        pass

    def test_get_github_release_titles(self, setup_env_with_project_ini_self_destruct):
        """Testing init_github_all_enable()"""
        env_setup = setup_env_with_project_ini_self_destruct
        release_details = [
            ["0.0.0", "Version 0.0.0", "This is a test release for 0.0.0"],
            ["0.0.1", "Version 0.0.1", "This is a test release for 0.0.1"],
        ]
        release_titles = [s[0] for s in release_details]
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.gh_repo.delete()
        p_it.init_github()
        p_it.init_github_repo()
        commit_rc = p_it.gh_repo.create_file(
            "test.txt", "test", "test", branch="master"
        )
        for release_detail in release_details:
            p_it.gh_repo.create_git_tag(
                release_detail[0], release_detail[1], commit_rc["commit"].sha, "commit"
            )
            p_it.gh_repo.create_git_release(
                release_detail[0], release_detail[2], "Line 1\nLine 2"
            )

        assert p_it.get_github_repo_tags() == list(reversed(release_titles))

        p_it.gh_repo.delete()
        pass

    def test_get_pypi_project_details(self, setup_env_self_destruct):
        """Testing packageit_upload_to_enabled()"""
        env_setup = setup_env_self_destruct
        change_ini(env_setup.packageit_ini_pth, "PyPi", "Publishing", "Twine")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.create_venv()
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.create_source_code_py()
        p_it.create__init__()
        p_it.create_source_code_ini()
        # p_it.create_setup_py()
        p_it.create_setup_cfg()
        p_it.create_license()
        p_it.create_test_code()
        p_it.create_conftest_py()
        p_it.create_pyproject_toml()
        p_it.create_readme()
        p_it.create_manifest()
        p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        p_it.create_requirements("requirements_test.txt", p_it.project_import_prod)
        p_it.project_readme_rst.write_text()
        p_it.format_code()
        p_it.make_wheels()
        p_it.upload_to_pypi()

        assert p_it.get_pypi_project_version() == "0.0.0"
        p_it.project_new = False
        assert p_it.get_pypi_project_version() == "0.0.0"
        p_it.project_pypi_publishing = "No"
        assert p_it.get_pypi_project_version() is None
        pass

    def test_get_release_from_title(self, setup_env_self_destruct):
        """Testing packageit__init__()"""
        env_setup = setup_env_self_destruct

        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        assert p_it.get_release_from_title("Version 9.9.9.") == "9.9.9"
        assert p_it.get_release_from_title("Version 9.9.9") == "9.9.9"
        assert (
            p_it.get_release_from_title("Version 9.9.9. and the something else")
            == "9.9.9"
        )
        assert (
            p_it.get_release_from_title("Version 9.9.9 and the something else")
            == "9.9.9"
        )
        assert p_it.get_release_from_title("9.9.9.") == "9.9.9"
        assert p_it.get_release_from_title("9.9.9") == "9.9.9"
        assert not p_it.get_release_from_title("No Version.") == "9.9.9"
        pass

    def test_git_commit(self, setup_env_self_destruct):
        """Testing packageit_git_commit()"""
        env_setup = setup_env_self_destruct
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        # p_it.create_venv()
        p_it.install_prereq_modules_in_venv()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.init_github_master_branch()
        p_it.init_git()
        p_it.marry_git_github()
        env_setup.create_mock_files()

        assert p_it.git_commit() == 0

        p_it.gh_repo.delete()
        pass

    def test_git_push_git_enable(self, setup_env_with_project_ini_self_destruct):
        """Testing packageit_git_push()"""
        env_setup = setup_env_with_project_ini_self_destruct
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.create_venv()
        p_it.create_scaffolding()
        env_setup.create_mock_files()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.init_github_master_branch()
        p_it.init_git()
        p_it.marry_git_github()
        assert p_it.git_commit() == 0

        p_it.git_repo.close()
        p_it.gh_repo.delete()
        pass

    def test_git_push_git_disable(self, setup_env_with_project_ini_self_destruct):
        """Testing packageit_git_push()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "Git", "Enable", "No")
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        env_setup.create_mock_files()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.init_github_master_branch()
        p_it.init_git()
        p_it.marry_git_github()
        pass

    def test_github_sync_release_notes(self, setup_env_with_project_ini_self_destruct):
        """Testing packageit_git_commit()"""
        """Testing init_github_all_enable()"""
        env_setup = setup_env_with_project_ini_self_destruct
        release_details_factory = [
            ["0.0.0", "Version 0.0.0", "This is a test release for 0.0.0"],
            ["0.0.2", "Version 0.0.2", "This is a test release for 0.0.2"],
        ]
        release_notes_001 = {
            "0": {
                "0": {
                    "1": {
                        "Title": "Version 0.0.1",
                        "Description": ["This is a test release for 0.0.1"],
                    }
                }
            }
        }
        release_notes_003 = {
            "0": {
                "0": {
                    "3": {
                        "Title": "Version 0.0.3",
                        "Description": ["This is a test release for 0.0.3"],
                    }
                }
            }
        }

        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.gh_repo.delete()
        p_it.init_github()
        p_it.init_github_repo()
        commit_rc = p_it.gh_repo.create_file(
            "test.txt", "test", "test", branch="master"
        )
        for rel_det in release_details_factory:
            p_it.gh_repo.create_git_tag(
                rel_det[0], rel_det[1], commit_rc["commit"].sha, "commit"
            )
            p_it.gh_repo.create_git_release(rel_det[0], rel_det[2], "Line 1\nLine 2")
        p_it.gh_repo.create_git_tag(
            "0.0.3", "Version 0.0.3", commit_rc["commit"].sha, "commit"
        )
        p_it.create_release()
        p_it.project_release.add_release_note(release_notes_001)
        p_it.project_release.add_release_note(release_notes_003)

        assert p_it.github_sync_release_notes()

        p_it.gh_repo.delete()
        pass

    def test_github_format_titles(self, setup_env_with_project_ini_self_destruct):
        """Testing packageit_git_commit()"""
        """Testing init_github_all_enable()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        release_details_factory = [
            ["0.0.0", "This is a title", "This is a test release for 0.0.0"],
            ["0.0.2", "Version 0.0.2", "This is a test release for 0.0.2"],
        ]

        assert p_it
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.gh_repo.delete()
        p_it.init_github()
        p_it.init_github_repo()

        commit_rc = p_it.gh_repo.create_file(
            "test.txt", "test", "test", branch="master"
        )
        for rel_det in release_details_factory:
            p_it.gh_repo.create_git_tag(
                rel_det[0], rel_det[1], commit_rc["commit"].sha, "commit"
            )
            p_it.gh_repo.create_git_release(rel_det[0], rel_det[2], "Line 1\nLine 2")

        assert p_it.github_format_titles()

        p_it.gh_repo.delete()
        pass

    def test_init_git_new(self, setup_env_with_project_ini_self_destruct):
        """Testing init_git_no_switches()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_git()

        assert (p_it.project_root_dir / ".git").exists()
        assert p_it.git_repo
        pass

    def test_init_git_existing(self, setup_env_with_project_ini_self_destruct):
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()

        # Create a new repo
        p_it.init_git()
        assert p_it.git_repo
        assert Path(p_it.project_root_dir / ".git").exists()
        p_it.git_repo.close()
        # Initialize the existing repo
        p_it.init_git()
        assert p_it.git_repo
        p_it.git_repo.close()
        pass

    def test_init_github_all_enable(self, setup_env_with_project_ini_self_destruct):
        """Testing init_github_all_enable()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()

        assert p_it.init_github()
        assert p_it.github
        pass

    def test_init_github_git_no(self, setup_env_with_project_ini_self_destruct):
        """Testing init_github_git_no()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "Git", "Enable", "No")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()

        assert not p_it.init_github()
        assert not p_it.github
        pass

    def test_init_github_github_no(self, setup_env_with_project_ini_self_destruct):
        """Testing init_github_github_no()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "GitHub", "Enable", "No")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()

        assert not p_it.init_github()
        assert not p_it.github
        pass

    def test_init_github_all_no(self, setup_env_with_project_ini_self_destruct):
        """Testing init_github_all_no()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "GitHub", "Enable", "No")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()

        assert not p_it.init_github()
        assert not p_it.github
        pass

    def test_init_github_master_branch_new(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing init_github_master_branch_new()"""
        env_setup = setup_env_with_project_ini_self_destruct
        # change_ini(env_setup.packageit_ini_pth, 'GitHub', 'Enable', 'No')
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()

        assert p_it.init_github_master_branch()

        p_it.gh_repo.delete()
        pass

    def test_init_github_master_branch_existing(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing init_github_master_branch_existing()"""
        env_setup = setup_env_with_project_ini_self_destruct
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.init_github_master_branch()
        assert p_it.init_github_master_branch()

        p_it.gh_repo.delete()
        pass

    def test_init_github_repo_new(self, setup_env_with_project_ini_self_destruct):
        """Testing init_github_all_enable()"""
        env_setup = setup_env_with_project_ini_self_destruct
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()

        assert p_it.init_github_repo()
        assert p_it.gh_repo

        p_it.gh_repo.delete()
        pass

    def test_init_github_repo_existing(self, setup_env_with_project_ini_self_destruct):
        """Testing init_github_all_enable()"""
        env_setup = setup_env_with_project_ini_self_destruct
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        assert p_it.init_github_repo()  # Create an instance of the repo
        assert p_it.init_github_repo()  # test operation with existing repo
        assert p_it.gh_repo

        p_it.gh_repo.delete()
        pass

    def test_install_prereq_apps_in_venv_new(self, setup_env_self_destruct):
        env_setup = setup_env_self_destruct
        env_setup.reduce_import_list()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_venv()
        p_it.init_git()
        p_it.install_prereq_modules_in_venv()

        assert p_it.install_prereq_apps_in_venv() == 0
        pass

    def test_install_prereq_modules_in_venv(self, setup_env_self_destruct):
        env_setup = setup_env_self_destruct
        env_setup.reduce_import_list()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_venv()
        p_it.init_git()

        assert p_it.install_prereq_modules_in_venv() == ['pip', 'pre-commit']
        pass

    def test_make_project_specific_ini_module(self, setup_env_self_destruct):
        """Testing make_project_specific_ini()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        ini = read_project_ini(p_it.project_packageit_ini_pth)

        assert p_it.project_packageit_ini_pth == Path(
            env_setup.anchor_dir, env_setup.project_name, ".packageit", "packageit.ini"
        )
        print(ini.sections())
        assert sorted(ini.sections()) == [
            "Classifiers",
            "Coverage",
            "Detail",
            "General",
            "Git",
            "GitHub",
            "Import",
            "Install Apps",
            "LogLevels",
            "PyPi",
            'ReadMe',
            "ReadTheDocs",
            "Sphinx",
            "VEnv",
            "flake8",
            "tool:pytest",
        ]
        pass

    def test_make_project_specific_ini_package(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing make_project_specific_ini_package()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "Detail", "Type", "Package")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.make_project_specific_ini()
        ini = read_project_ini(p_it.project_packageit_ini_pth)

        assert p_it.project_packageit_ini_pth == Path(
            env_setup.anchor_dir, env_setup.project_name, ".packageit", "packageit.ini"
        )
        assert ini.sections() == [
            "Classifiers",
            "Coverage",
            "Detail",
            "flake8",
            "General",
            "Git",
            "GitHub",
            "Import",
            "Install Apps",
            "LogLevels",
            "PyPi",
            'ReadMe',
            "ReadTheDocs",
            "Sphinx",
            "tool:pytest",
            "VEnv",
        ]
        pass

    def test_make_wheel(self, setup_env_self_destruct):
        """Testing packageit_make_wheel()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.create_venv()
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.create_source_code_py()
        p_it.create__init__()
        p_it.create_source_code_ini()
        # p_it.create_setup_py()
        p_it.create_setup_cfg()
        p_it.create_license()
        p_it.create_test_code()
        p_it.create_conftest_py()
        p_it.create_pyproject_toml()
        p_it.create_readme()
        p_it.create_manifest()
        p_it.create_requirements("requirements.txt", "ImportProd")
        p_it.create_requirements("requirements_test.txt", "ImportTest")
        p_it.project_readme_rst.write_text()
        p_it.format_code()

        dist_dir = env_setup.anchor_dir / env_setup.project_name / "dist"
        assert p_it.make_wheels() == 0
        assert p_it.project_wheels == [
            Path(dist_dir, "{}-0.0.0-py3-none-any.whl".format(env_setup.project_name)),
            Path(dist_dir, "{}-0.0.0.tar.gz".format(env_setup.project_name)),
        ]
        pass

    def test_marry_git_github_all_enable(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing marry_git_github_all_enable()"""
        env_setup = setup_env_with_project_ini_self_destruct
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.init_github_master_branch()
        p_it.init_git()

        assert p_it.marry_git_github()

        p_it.git_repo.close()
        pass

    def test_marry_git_github_git_disable(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing marry_git_github()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "Git", "Enable", "No")
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.init_github_master_branch()
        p_it.init_git()

        assert not p_it.marry_git_github()
        pass

    def test_marry_git_github_github_disable(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing marry_git_github()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "GitHub", "Enable", "No")
        # env_setup.del_github_repo()
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.init_github_master_branch()
        p_it.init_git()

        assert not p_it.marry_git_github()
        pass

    def test_read_project_detail_specific(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing read_project_detail_specific()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(
            env_setup.packageit_ini_pth,
            "Folders",
            "{}PackageFolder".format(get_os()),
            Path(env_setup.anchor_dir, "foo"),
        )
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )

        assert p_it.project_name == env_setup.project_name
        assert p_it.project_author == "Hendrik du Toit"
        assert p_it.project_author_email == "hendrik@brightedge.co.za"
        assert p_it.project_classifiers == [
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Topic :: Software Development",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.0",
            "Programming Language :: Python :: 3.10",
        ]
        assert p_it.project_dir is None
        assert p_it.project_git_enable
        assert p_it.project_gh_enable
        assert (
            p_it.project_header_description
            == "Project Header Description (project ini)"
        )
        assert p_it.project_import_prod == [["pypi", "termcolor"]]
        assert p_it.project_import_rewrite is True
        assert p_it.project_import_test == [
            ["pypi", "pip"],
            ["pypi", "wheel"],
            ["pypi", "pre-commit"],
            ["pypi", "pytest"],
            ["pypi", "beetools"],
            ["pypi", "pytest-cov"],
            ["pypi", "sphinx"],
            ["pypi", "sphinx-autobuild"],
            ['pypi', 'sphinx-rtd-theme'],
            ["pypi", "black"],
            ["pypi", "build"],
            ["pypi", "configparserext"],
            ["pypi", "pygithub"],
        ]
        assert p_it.project_install_apps == ["pre-commit install"]
        assert (
            p_it.project_long_description
            == "Project long description goes in here (project ini)"
        )
        assert p_it.project_pypi_publishing == "GitHub"
        assert p_it.project_pypi_repository == "testpypi"
        assert p_it.project_python_requires == ">=3.6"
        assert p_it.project_type == "Module"
        assert p_it.project_version.version == "0.0.0"
        assert p_it.project_venv_enable
        assert p_it.project_venv_name == env_setup.project_name
        assert not p_it.project_venv_reinstall
        assert p_it.project_venv_upgrade
        assert p_it.project_url == "www.brightedge.co.za"
        pass

    def test_read_token(self, setup_env_with_project_ini_self_destruct):
        """Testing read_token()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )

        assert (
            p_it.read_token(p_it.packageit_ini.get("PyPi", "TokenFileNamePyPi"))
            == (env_setup.token_dir / "PYPI_API_TOKEN.txt").read_text().strip()
        )
        pass

    def test_run(self, setup_env_self_destruct):
        """Testing packageit_run()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.run()

        assert p_it.success
        # assert p_it.ini_def_pth == env_setup.packageit_ini_pth
        assert p_it.logger_name is None
        assert p_it.packageit_dir == Path(_PATH.parents[1])
        assert p_it.packageit_ini_pth == env_setup.packageit_ini_pth
        assert p_it.project_anchor_dir == env_setup.anchor_dir
        assert p_it.project_name == env_setup.project_name
        assert p_it.project_dir == Path(
            env_setup.anchor_dir,
            env_setup.project_name,
            "src",
            env_setup.project_name.lower(),
        )
        assert p_it.project_git_enable
        assert p_it.project_type == "Module"
        assert p_it.project_author == "Ann Other"
        assert p_it.project_author_email == "ann.other@testmodule.com"
        assert p_it.project_classifiers == env_setup.classifiers
        assert p_it.project_url == "www.{}.com".format(env_setup.project_name.lower())
        assert p_it.project_dir == Path(
            env_setup.anchor_dir,
            env_setup.project_name,
            "src",
            env_setup.project_name.lower(),
        )
        assert p_it.project_packageit_ini_pth == Path(
            env_setup.anchor_dir, env_setup.project_name, ".packageit", "packageit.ini"
        )
        assert p_it.project_name == env_setup.project_name
        assert p_it.project_src_dir == Path(
            env_setup.anchor_dir, env_setup.project_name, "src"
        )
        assert p_it.project_tests_dir == Path(
            env_setup.anchor_dir, env_setup.project_name, "tests"
        )
        assert p_it.project_versionarchive_dir == Path(
            env_setup.anchor_dir, env_setup.project_name, "VersionArchive"
        )
        assert p_it.templ_dir == p_it.packageit_dir / "templates"
        assert p_it.project_venv_root_dir == env_setup.anchor_dir / "venv"
        assert p_it.project_venv_dir == Path(
            env_setup.anchor_dir, "venv", "{}_env".format(env_setup.project_name)
        )
        assert p_it.project_venv_name == env_setup.project_name
        assert p_it.verbose

        # repo = p_it.gh_user.get_repo(env_setup.project_name)
        p_it.gh_repo.delete()
        pass

    def test_setup_sphinx(self, setup_env_self_destruct):
        """Testing packageit_setup_sphinx()"""
        env_setup = setup_env_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.create_venv()
        p_it.create_scaffolding()
        p_it.install_prereq_modules_in_venv()

        assert p_it.setup_sphinx() == 0
        pass

    def test_upload_to_pypi_publishing_no(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing packageit_upload_to_pypi_disabled()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "PyPi", "Publishing", "No")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.create_venv()
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.create_source_code_py()
        p_it.create__init__()
        p_it.create_source_code_ini()
        # p_it.create_setup_py()
        p_it.create_setup_cfg()
        p_it.create_license()
        p_it.create_test_code()
        p_it.create_conftest_py()
        p_it.create_pyproject_toml()
        p_it.create_readme()
        p_it.create_manifest()
        p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        p_it.create_requirements("requirements_test.txt", p_it.project_import_prod)
        p_it.project_readme_rst.write_text()
        p_it.format_code()
        p_it.make_wheels()

        # dist_dir = env_setup.anchor_dir / env_setup.project_name / 'dist'
        assert not p_it.upload_to_pypi()
        pass

    def test_upload_to_pypi_enabled_manual(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing packageit_upload_to_enabled()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "PyPi", "Publishing", "Twine")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.create_venv()
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.create_source_code_py()
        p_it.create__init__()
        p_it.create_source_code_ini()
        # p_it.create_setup_py()
        p_it.create_setup_cfg()
        p_it.create_license()
        p_it.create_test_code()
        p_it.create_conftest_py()
        p_it.create_pyproject_toml()
        p_it.create_readme()
        p_it.create_manifest()
        p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        p_it.create_requirements("requirements_test.txt", p_it.project_import_prod)
        p_it.project_readme_rst.write_text()
        p_it.format_code()
        p_it.make_wheels()

        # dist_dir = working_dir / env_setup.project_name / 'dist'
        assert p_it.upload_to_pypi() == 0
        pass

    def test_update_to_latest_version(self, setup_env_with_project_ini_self_destruct):
        """Testing packageit_upload_to_enabled()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "PyPi", "Publishing", "Twine")
        release_details_factory = [
            ["0.0.0", "Version 0.0.0", "This is a test release for 0.0.0"],
            ["0.0.2", "Version 0.0.2", "This is a test release for 0.0.2"],
        ]
        # release_notes_001 = {
        #     "0": {
        #         "0": {
        #             "1": {
        #                 "Title": "Version 0.0.1",
        #                 "Description": ["This is a test release for 0.0.1"],
        #             }
        #         }
        #     }
        # }
        release_notes_010 = {
            "0": {
                "1": {
                    "0": {
                        "Title": "Version 0.1.0",
                        "Description": ["This is a test release for 0.1.0"],
                    }
                }
            }
        }

        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.create_venv()
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.gh_repo.delete()
        p_it.init_github()
        p_it.init_github_repo()
        p_it.create_source_code_py()
        p_it.create__init__()
        p_it.create_source_code_ini()
        commit_rc = p_it.gh_repo.create_file(
            "test.txt", "test", "test", branch="master"
        )
        for rel_det in release_details_factory:
            p_it.gh_repo.create_git_tag(
                rel_det[0], rel_det[1], commit_rc["commit"].sha, "commit"
            )
            p_it.gh_repo.create_git_release(rel_det[0], rel_det[2], "Line 1\nLine 2")
        p_it.create_release()
        p_it.create_setup_cfg()
        p_it.create_license()
        p_it.create_test_code()
        p_it.create_conftest_py()
        p_it.create_pyproject_toml()
        p_it.create_readme()
        p_it.create_manifest()
        p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        p_it.create_requirements("requirements_test.txt", p_it.project_import_prod)
        p_it.project_readme_rst.write_text()
        p_it.format_code()

        assert p_it.update_to_latest_version() == "0.0.2"
        setup_cfg = configparserext.ConfigParserExt(inline_comment_prefixes="#")
        setup_cfg.read(p_it.project_setup_cfg_pth)
        assert setup_cfg.get("metadata", "version") == "0.0.2"

        p_it.project_release.add_release_note(release_notes_010)
        assert p_it.update_to_latest_version() == "0.1.0"
        setup_cfg = configparserext.ConfigParserExt(inline_comment_prefixes="#")
        setup_cfg.read(p_it.project_setup_cfg_pth)
        assert setup_cfg.get("metadata", "version") == "0.1.0"

        # p_it.project_setup_cfg.set('metadata', 'version', '0.2.0')
        # with open(p_it.project_setup_cfg_pth, 'w') as fp :
        #     p_it.project_setup_cfg.write(fp)
        # p_it.make_wheels()
        # p_it.upload_to_pypi()
        # sleep(30)  # Wait for the project to become available on PyPI
        # with pytest.raises(PackageItException):
        #     p_it.update_to_latest_version()
        pass

    def test_upload_to_pypi_enabled_auto(
        self, setup_env_with_project_ini_self_destruct
    ):
        """Testing packageit_upload_to_enabled()"""
        env_setup = setup_env_with_project_ini_self_destruct
        change_ini(env_setup.packageit_ini_pth, "PyPi", "Publishing", "GitHub")
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        # p_it.create_venv()
        p_it.create_scaffolding()
        p_it.create_git_ignore()
        p_it.create_source_code_py()
        p_it.create__init__()
        p_it.create_source_code_ini()
        # p_it.create_setup_py()
        p_it.create_setup_cfg()
        p_it.create_license()
        p_it.create_test_code()
        p_it.create_conftest_py()
        p_it.create_pyproject_toml()
        p_it.create_readme()
        p_it.create_manifest()
        p_it.create_requirements("requirements.txt", p_it.project_import_prod)
        p_it.create_requirements("requirements_test.txt", p_it.project_import_prod)
        p_it.project_readme_rst.write_text()
        p_it.format_code()
        p_it.make_wheels()

        # dist_dir = working_dir / env_setup.project_name / 'dist'
        assert p_it.upload_to_pypi()
        pass

    def test_zip_project(self, setup_env_with_project_ini_self_destruct):
        """Testing zip_project()"""
        env_setup = setup_env_with_project_ini_self_destruct
        p_it = packageit.PackageIt(
            env_setup.packageit_ini_pth,
            env_setup.project_name,
            p_arc_extern_dir=env_setup.external_arc_dir,
            p_token_dir=env_setup.token_dir,
        )
        p_it.create_scaffolding()
        arc_pth = p_it.zip_project()

        assert arc_pth.exists()
        assert (env_setup.external_arc_dir / arc_pth.name).exists()


del b_tls
