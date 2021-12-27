"""Testing packageit__init__()"""

from pathlib import Path
from beetools.beearchiver import Archiver
from packageit.packageit import GenSetUpPy

_DESC = __doc__.split("\n")[0]
_PATH = Path(__file__)
_NAME = _PATH.stem

b_tls = Archiver(_DESC, _PATH)


_setup_py_contents = """
import setuptools


with open('README.rst', 'r') as fh:
    long_description = fh.read()
with open('requirements.txt', 'r') as fh:
    requirements = [line.strip() for line in fh]


setuptools.setup(
    name = 'pymodule',
    version = '0.0.1',
    author = 'Ann Other',
    author_email = 'ann.other@testmodule.com',
    description = 'Insert project description here',
    long_description = long_description,
    long_description_content_type = 'text/x-rst',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    package_dir = {'': 'src'},
    packages = setuptools.find_packages(where = 'src'),
    python_requires = '>=3.6',
    install_requires = requirements
)
"""


_setup_py_def = {
    "Name": "pymodule",
    "Author": "Ann Other",
    "Version": "0.0.1",
    "AuthorEmail": "ann.other@testmodule.com",
    "Description": "Insert project description here",
    "Classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    "PackageDir": """{'': 'src'}""",
    "Packages": """setuptools.find_packages(where = 'src')""",
    "PythonRequires": ">=3.6",
}


class TestGenSetUp:
    def test_gensetuppy__init_no_detail(self, working_dir_self_destruct):
        """Testing gensetuppy__init__()"""
        t_gensetuppy = GenSetUpPy(working_dir_self_destruct.dir)
        assert t_gensetuppy.name is None
        assert t_gensetuppy.version is None
        assert t_gensetuppy.author is None
        assert t_gensetuppy.author_email is None
        assert t_gensetuppy.description is None
        assert t_gensetuppy.classifiers is None
        assert t_gensetuppy.long_description is None
        assert t_gensetuppy.long_description_content_type == """'text/x-rst',\n"""
        assert t_gensetuppy.packages_dir is None
        assert t_gensetuppy.packages is None
        assert t_gensetuppy.python_requires is None
        assert t_gensetuppy.install_requires is None
        pass

    def test_gensetuppy__init_with_detail_params(self, working_dir_self_destruct):
        """Testing gensetuppy_exists_false()"""
        t_gensetuppy = GenSetUpPy(
            p_setup_py_dir=working_dir_self_destruct.dir,
            p_name=_setup_py_def["Name"],
            p_version=_setup_py_def["Version"],
            p_author=_setup_py_def["Author"],
            p_author_email=_setup_py_def["AuthorEmail"],
            p_description=_setup_py_def["Description"],
            p_classifiers=_setup_py_def["Classifiers"],
            p_package_dir=_setup_py_def["PackageDir"],
            p_packages=_setup_py_def["Packages"],
            p_python_requires=_setup_py_def["PythonRequires"],
        )
        assert t_gensetuppy.name == _setup_py_def["Name"]
        assert t_gensetuppy.version == _setup_py_def["Version"]
        assert t_gensetuppy.author is _setup_py_def["Author"]
        assert t_gensetuppy.author_email is _setup_py_def["AuthorEmail"]
        assert t_gensetuppy.description is _setup_py_def["Description"]
        assert t_gensetuppy.classifiers is _setup_py_def["Classifiers"]
        assert t_gensetuppy.long_description is None
        assert t_gensetuppy.long_description_content_type == """'text/x-rst',\n"""
        assert t_gensetuppy.packages_dir is _setup_py_def["PackageDir"]
        assert t_gensetuppy.packages is _setup_py_def["Packages"]
        assert t_gensetuppy.python_requires is _setup_py_def["PythonRequires"]
        assert t_gensetuppy.install_requires is None
        pass

    def test_gensetuppy_exists_no_data_false(self, working_dir_self_destruct):
        """Testing gensetuppy_exists_false()"""
        t_gensetuppy = GenSetUpPy(working_dir_self_destruct.dir)
        assert not t_gensetuppy.exists()
        pass

    def test_gensetuppy_exists_with_data_false(self, working_dir_self_destruct):
        """Testing gensetuppy_exists_false()"""
        t_gensetuppy = GenSetUpPy(
            p_setup_py_dir=working_dir_self_destruct.dir,
            p_name=_setup_py_def["Name"],
            p_version=_setup_py_def["Version"],
            p_author=_setup_py_def["Author"],
            p_author_email=_setup_py_def["AuthorEmail"],
            p_description=_setup_py_def["Description"],
            p_classifiers=_setup_py_def["Classifiers"],
            p_package_dir=_setup_py_def["PackageDir"],
            p_packages=_setup_py_def["Packages"],
            p_python_requires=_setup_py_def["PythonRequires"],
        )
        assert not t_gensetuppy.exists()
        pass

    def test_gensetuppy_write(self, working_dir_self_destruct):
        """Testing gensetuppy_exists_false()"""
        t_gensetuppy = GenSetUpPy(
            p_setup_py_dir=working_dir_self_destruct.dir,
            p_name=_setup_py_def["Name"],
            p_version=_setup_py_def["Version"],
            p_author=_setup_py_def["Author"],
            p_author_email=_setup_py_def["AuthorEmail"],
            p_description=_setup_py_def["Description"],
            p_classifiers=_setup_py_def["Classifiers"],
            p_package_dir=_setup_py_def["PackageDir"],
            p_packages=_setup_py_def["Packages"],
            p_python_requires=_setup_py_def["PythonRequires"],
        )
        t_gensetuppy.write_text()
        assert t_gensetuppy.exists()
        pass

    def test_gensetuppy_wrie_with_data(self, working_dir_self_destruct):
        """Testing gensetuppy_exists_false()"""
        working_dir = working_dir_self_destruct.dir
        t_gensetuppy = GenSetUpPy(
            p_setup_py_dir=working_dir,
            p_name=_setup_py_def["Name"],
            p_version=_setup_py_def["Version"],
            p_author=_setup_py_def["Author"],
            p_author_email=_setup_py_def["AuthorEmail"],
            p_description=_setup_py_def["Description"],
            p_classifiers=_setup_py_def["Classifiers"],
            p_package_dir=_setup_py_def["PackageDir"],
            p_packages=_setup_py_def["Packages"],
            p_python_requires=_setup_py_def["PythonRequires"],
        )
        t_gensetuppy.write_text()
        setup_py_text = (working_dir / "setup.py").read_text()
        assert setup_py_text == _setup_py_contents
        pass


del b_tls
