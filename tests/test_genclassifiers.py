"""Testing genclassifiers__init__()"""

from pathlib import Path

# from beetools.beeutils import rm_tree
from beetools.beearchiver import Archiver

from packageit.packageit import GenClassifiers

# from genclassifiers_conftest import setup_env, make_ini

_DESC = __doc__.split("\n")[0]
_PATH = Path(__file__)
_NAME = _PATH.stem

_CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "Topic :: Software Development",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.10",
]
b_tls = Archiver(_DESC, _PATH)


class TestGenClassifiers:
    def test_genclassifiers__init__(self, setup_env_with_project_ini_self_destruct):
        """Testing genclassifiers__init__()"""
        env_setup = setup_env_with_project_ini_self_destruct
        ini_pth = env_setup.make_project_ini()
        t_genclassifier = GenClassifiers(_NAME, ini_pth)
        assert t_genclassifier.success
        assert t_genclassifier.verbose
        assert t_genclassifier.log_name is None
        assert t_genclassifier.logger is None
        assert t_genclassifier.dev_status == "Development Status :: 1 - Planning"
        assert t_genclassifier.ini_pth == ini_pth
        assert t_genclassifier.intended_audience == [
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
        ]
        assert t_genclassifier.license == "License :: OSI Approved :: MIT License"
        assert t_genclassifier.programming_language == [
            "Programming Language :: Python :: 3.0",
            "Programming Language :: Python :: 3.10",
        ]
        assert t_genclassifier.topic == ["Topic :: Software Development"]
        assert t_genclassifier.contents == _CLASSIFIERS
        pass

    def test_genclassifiers_read_ini(self, setup_env_with_project_ini_self_destruct):
        """Testing genclassifiers_read_ini()"""
        env_setup = setup_env_with_project_ini_self_destruct
        ini_pth = env_setup.make_project_ini()
        t_genclassifier = GenClassifiers(_NAME, ini_pth)
        assert t_genclassifier.read_ini() == _CLASSIFIERS
        assert t_genclassifier.dev_status == "Development Status :: 1 - Planning"
        assert t_genclassifier.intended_audience == [
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
        ]
        assert t_genclassifier.license == "License :: OSI Approved :: MIT License"
        assert t_genclassifier.programming_language == [
            "Programming Language :: Python :: 3.0",
            "Programming Language :: Python :: 3.10",
        ]
        assert t_genclassifier.topic == ["Topic :: Software Development"]
        assert t_genclassifier.contents == _CLASSIFIERS
        pass


del b_tls
