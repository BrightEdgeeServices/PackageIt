"""Testing FileTmeplate"""

from pathlib import Path
from packageit.packageit import ReadMe

# from beetools.beearchiver import Archiver
# from packageit.packageit import RSTBuilder

_DESC = __doc__.split("\n")[0]
_PATH = Path(__file__)
_NAME = _PATH.stem


class TestReadMe:
    def test__init__(self, working_dir_self_destruct):
        """Testing TestFileTemplate.init"""
        working_dir = working_dir_self_destruct

        t_readme = ReadMe(p_src_pth=working_dir.dir)
        assert t_readme.src_pth == working_dir.dir / 'README.rst'
        pass

    def test_create_from_template(self, working_dir_self_destruct):
        """Testing TestFileTemplate.create_from_template"""
        working_dir = working_dir_self_destruct

        FILE_CONTENTS = 'ReadMe'
        templ_pth = working_dir.dir / 'template_readme.rst'
        templ_pth.write_text(FILE_CONTENTS)
        t_readme = ReadMe(p_src_pth=working_dir.dir)
        t_readme.create_from_template(templ_pth)
        assert t_readme.src_pth.read_text() == FILE_CONTENTS

        templ_pth.write_text(FILE_CONTENTS + FILE_CONTENTS)
        t_readme.create_from_template(templ_pth)
        assert t_readme.src_pth.read_text() == FILE_CONTENTS

        t_readme.create_from_template(templ_pth, p_ow=True)
        assert t_readme.src_pth.read_text() == FILE_CONTENTS + FILE_CONTENTS

        pass
