"""Testing rstbuilder__init__()"""

from pathlib import Path
from beetools.beearchiver import Archiver

# from beetools.beeutils import rm_tree
from packageit.packageit import RSTBuilder

_DESC = __doc__.split("\n")[0]
_PATH = Path(__file__)
_NAME = _PATH.stem

_IMAGE_TEXT = """.. image:: https://img.shields.io/pypi/v/BEETest?style = plastic
    :align: right
    :alt: PyPi
    :height: 100px
    :scale: 50%
    :target: https://pypi.org/project/BEETest/
    :width: 50px

"""
_NEW_ELEMENT = {"Type": "DirectiveImage", "Text": _IMAGE_TEXT}
_TARGET = "https://pypi.org/project/BEETest/"
_URI = """https://img.shields.io/pypi/v/BEETest?style = plastic"""


b_tls = Archiver(_DESC, _PATH)


class TestRstBuilder:
    def test_rstbuilder__init__no_detail(self, working_dir_self_destruct):
        """Testing rstbuilder__init_no_detail()"""
        working_dir = working_dir_self_destruct

        t_rstbuilder = RSTBuilder(_NAME, working_dir.dir)

        assert t_rstbuilder.log_name is None
        assert t_rstbuilder.logger is None
        assert not t_rstbuilder.contents
        assert t_rstbuilder.curr_pos == 0
        assert t_rstbuilder.element_cntr == 0
        assert t_rstbuilder.elements == {}
        assert t_rstbuilder.pth == working_dir.dir
        assert t_rstbuilder.tab_len == 4
        assert t_rstbuilder.verbose is True
        pass

    def test_rstbuilder__init__with_details(self, working_dir_self_destruct):
        """Testing rstbuilder__init_with_details()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"
        t_rstbuilder = RSTBuilder(
            _NAME,
            readme_pth,
            p_first_level_title="First Level Title",
        )
        assert t_rstbuilder.log_name is None
        assert t_rstbuilder.logger is None
        assert not t_rstbuilder.contents
        assert t_rstbuilder.curr_pos == 0
        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "FirstLevelTitle",
                "Text": "=================\nFirst Level Title\n=================\n\n",
            },
        }
        assert t_rstbuilder.pth == readme_pth
        assert t_rstbuilder.verbose is True
        pass

    def test_rstbuilder__iter__(self, working_dir_self_destruct):
        """Testing rstbuilder__iter_no_detail()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)

        assert isinstance(t_rstbuilder, RSTBuilder)
        assert t_rstbuilder.curr_pos == 0
        pass

    def test_rstbuilder__next__(self, working_dir_self_destruct):
        """Testing rstbuilder__iter_no_detail()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_paragraph("Par 1")
        t_rstbuilder.add_paragraph("Par 2")
        t_rstbuilder.add_paragraph("Par 3")

        elements = iter(t_rstbuilder)

        assert next(elements) == {"Text": "Par 1\n\n", "Type": "Paragraph"}
        assert next(elements) == {"Text": "Par 2\n\n", "Type": "Paragraph"}
        assert next(elements) == {"Text": "Par 3\n\n", "Type": "Paragraph"}
        pass

    def test_rstbuilder_add_comment(self, working_dir_self_destruct):
        """Testing rstbuilder_add_comment()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "index.rst"
        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_comment("This is a comment.")
        t_rstbuilder.add_comment("This is another comment.")
        t_rstbuilder.add_comment("And one more comment.")

        assert t_rstbuilder.element_cntr == 3
        assert t_rstbuilder.elements == {
            0: {"Type": "Comment", "Text": ".. This is a comment.\n"},
            1: {"Type": "Comment", "Text": ".. This is another comment.\n"},
            2: {"Type": "Comment", "Text": ".. And one more comment.\n\n"},
        }
        pass

    def test_rstbuilder_add_image_directive_basic(self, working_dir_self_destruct):
        """Testing rstbuilder_add_image_directive_basic()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_directive_image(p_uri=_URI)

        assert t_rstbuilder.elements == {
            0: {
                "Text": ".. image:: https://img.shields.io/pypi/v/BEETest?style = plastic\n\n",
                "Type": "DirectiveImage",
            }
        }
        assert t_rstbuilder.element_cntr == 1
        pass

    def test_rstbuilder_add_image_directive_with_detail(
        self, working_dir_self_destruct
    ):
        """Testing rstbuilder_add_image_directive_with_detail()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_directive_image(
            p_uri=_URI,
            p_align="right",
            p_alt="PyPi",
            p_height="100px",
            p_level=0,
            p_pos=0,
            p_scale="50%",
            p_target=_TARGET,
            p_width="50px",
        )
        assert t_rstbuilder.elements == {
            0: {"Type": "DirectiveImage", "Text": _IMAGE_TEXT}
        }
        assert t_rstbuilder.element_cntr == 1
        pass

    def test_rstbuilder_add_paragraph(self, working_dir_self_destruct):
        """Testing rstbuilder_add_paragraph()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"
        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_comment("This is a comment.")
        t_rstbuilder.add_comment("This is another comment.")
        t_rstbuilder.add_first_level_title("First Level Title")
        t_rstbuilder.add_second_level_title("Second Level Title.")
        t_rstbuilder.add_comment("This is another comment.", 3)
        assert t_rstbuilder.element_cntr == 5
        assert t_rstbuilder.elements == {
            0: {"Type": "Comment", "Text": ".. This is a comment.\n"},
            1: {"Type": "Comment", "Text": ".. This is another comment.\n\n"},
            2: {
                "Type": "FirstLevelTitle",
                "Text": "=================\nFirst Level Title\n=================\n\n",
            },
            3: {"Type": "Comment", "Text": ".. This is another comment.\n\n"},
            4: {
                "Type": "SecondLevelTitle",
                "Text": "-------------------\nSecond Level Title.\n-------------------\n\n",
            },
        }
        pass

    def test_rstbuilder_add_fifth_level_tile(self, working_dir_self_destruct):
        """Testing rstbuilder_add_fifth_level_tile()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_fifth_level_title("Fifth Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "FifthLevelTitle",
                "Text": "Fifth Level Title\n'''''''''''''''''\n\n",
            }
        }
        pass

    def test_rstbuilder_first_level_title(self, working_dir_self_destruct):
        """Testing rstbuilder_add_first_level_title()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_first_level_title("First Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "FirstLevelTitle",
                "Text": "=================\nFirst Level Title\n=================\n\n",
            }
        }
        pass

    def test_rstbuilder_add_fourth_level_title(self, working_dir_self_destruct):
        """Testing rstbuilder_add_fourth_level_title()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_fourth_level_title("Fourth Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "FourthLevelTitle",
                "Text": "Fourth Level Title\n------------------\n\n",
            }
        }
        pass

    def test_rstbuilder_add_second_level_title(self, working_dir_self_destruct):
        """Testing rstbuilder_add_second_level_title()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_second_level_title("Second Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "SecondLevelTitle",
                "Text": "------------------\nSecond Level Title\n------------------\n\n",
            }
        }
        pass

    def test_rstbuilder_add_third_level_title(self, working_dir_self_destruct):
        """Testing rstbuilder_add_third_level_title()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)
        t_rstbuilder.add_third_level_title("Third Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "ThirdLevelTitle",
                "Text": "Third Level Title\n=================\n\n",
            }
        }
        pass

    def test_rstbuilder_add_toctree(self, working_dir_self_destruct):
        """Testing rstbuilder_add_toctree()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"
        toc_items = ["Conventions", "api", "examples"]

        rstbuilder = RSTBuilder(_NAME, readme_pth)
        rstbuilder.add_toctree(
            toc_items, p_maxdepth=2, p_caption="Contents", p_numbered=True
        )

        assert rstbuilder.element_cntr == 1
        assert rstbuilder.elements == {
            0: {
                "Type": "TocTree",
                "Text": ".. toctree::\n    :maxdepth: 2\n    :caption: Contents\n    :numbered:\n\n    Conventions\n"
                + "    api\n    examples\n\n",
                "Items": ["Conventions", "api", "examples"],
            }
        }
        pass

    def test_rstbuilder_insert_at(self, working_dir_self_destruct):
        """Testing rstbuilder__init_with_details()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"
        t_rstbuilder = RSTBuilder(
            _NAME, readme_pth, p_first_level_title="First Level Title"
        )
        t_rstbuilder.add_second_level_title("Second Level Title")
        t_rstbuilder._insert_at(_NEW_ELEMENT, 1)
        assert t_rstbuilder.element_cntr == 3
        assert t_rstbuilder.elements == {
            0: {
                "Type": "FirstLevelTitle",
                "Text": "=================\nFirst Level Title\n=================\n\n",
            },
            1: {
                "Type": "DirectiveImage",
                "Text": ".. image:: https://img.shields.io/pypi/v/BEETest?style = plastic\n    :align: right\n"
                + "    :alt: PyPi\n    :height: 100px\n    :scale: 50%\n"
                + "    :target: https://pypi.org/project/BEETest/\n    :width: 50px\n\n",
            },
            2: {
                "Type": "SecondLevelTitle",
                "Text": "------------------\nSecond Level Title\n------------------\n\n",
            },
        }
        pass

    def test_rstbuilder_make_indent(self, working_dir_self_destruct):
        """Testing rstbuilder_make_indent()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"

        t_rstbuilder = RSTBuilder(_NAME, readme_pth)

        assert t_rstbuilder._make_indent(0) == ""
        assert t_rstbuilder._make_indent(1) == "    "
        assert t_rstbuilder._make_indent(2) == "        "
        pass

    def test_rstbuilder_underline(self, working_dir_self_destruct):
        """Testing rstbuilder_underline()"""
        working_dir = working_dir_self_destruct
        readme_pth = working_dir.dir / "README.rst"
        t_rstbuilder = RSTBuilder(
            _NAME, readme_pth, p_first_level_title="First Level Title"
        )

        assert t_rstbuilder._underline("First Level Title", "=") == "================="
        assert t_rstbuilder.element_cntr == 1
        pass
