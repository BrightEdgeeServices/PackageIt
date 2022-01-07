
'''Testing {1}__init__()'''

from pathlib import Path
from beetools.beearchiver import Archiver
import {1}


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)


def project_desc():
    return _PROJ_DESC


b_tls = Archiver(_PROJ_DESC, _PROJ_PATH)


class Test{0}:
    def test__init__(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_{1} = {1}.{0}(env_setup.dir, True)

        assert t_{1}.success
        pass

    def test_method_1(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_{1} = {1}.{0}("{0}", env_setup.dir)

        assert t_{1}.method_1()
        pass

del b_tls
