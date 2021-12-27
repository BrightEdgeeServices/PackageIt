"""Testing genlicense__init__()"""

from pathlib import Path
from beetools.beearchiver import Archiver

# from beetools.beeutils import rm_tree
from packageit.packageit import GenLicense

_DESC = __doc__.split("\n")[0]
_PATH = Path(__file__)
_NAME = _PATH.stem


def generate_lic_templates(working_dir):
    """Generate licence types"""
    templ_pth = working_dir / "templ_lic_MITLicense.txt"
    templ_pth.write_text("This is a MIT Licence")
    templ_pth = working_dir / "templ_lic_ApacheLicense20.txt"
    templ_pth.write_text("This is an Apache License")
    return templ_pth.parents[0]


b_tls = Archiver(_DESC, _PATH)


class TestGenLicense:
    def test_genlicense__init__(self, working_dir_self_destruct):
        """Testing genlicense__init__()"""
        lic_templ_pth = generate_lic_templates(working_dir_self_destruct.dir)
        t_genlicense = GenLicense(_NAME, "ApacheLicense20", lic_templ_pth)
        assert t_genlicense.log_name is None
        assert t_genlicense.logger is None
        assert t_genlicense.contents == "This is an Apache License"
        assert t_genlicense.templ_prefix == "templ_lic"
        assert t_genlicense.templ_pth == lic_templ_pth
        assert t_genlicense.type == "ApacheLicense20"
        assert t_genlicense.lic_types == ["ApacheLicense20", "MITLicense"]
        assert t_genlicense.verbose
        pass

    def test_genlicense__get_type_text(self, working_dir_self_destruct):
        """Testing genlicense__init__()"""
        lic_templ_pth = generate_lic_templates(working_dir_self_destruct.dir)
        t_genlicense = GenLicense(_NAME, "ApacheLicense20", lic_templ_pth)
        assert t_genlicense.get_lic_types() == ["ApacheLicense20", "MITLicense"]
        pass

    def test_genlicense_get_type_text(self, working_dir_self_destruct):
        """Testing genlicense_get_type_text()"""
        lic_templ_pth = generate_lic_templates(working_dir_self_destruct.dir)
        t_genlicense = GenLicense(_NAME, "ApacheLicense20", lic_templ_pth)
        assert t_genlicense.get_type_text() == "This is an Apache License"
        pass

    def test_genlicense_verify_lic_type(self, working_dir_self_destruct):
        """Testing genlicense_verify_lic_type()"""
        lic_templ_pth = generate_lic_templates(working_dir_self_destruct.dir)
        t_genlicense = GenLicense(_NAME, "ApacheLicense20", lic_templ_pth)
        assert t_genlicense.verify_lic_type()
        pass


del b_tls
