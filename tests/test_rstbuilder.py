"""Testing rstbuilder__init__()"""

import logging
from pathlib import Path
from beetools.beearchiver import Archiver
from packageit.packageit import RSTBuilder

_DESC = __doc__.split("\n")[0]
_PATH = Path(__file__)
_NAME = _PATH.stem

_FORMATED_TEXT = """
=======
Testing
=======

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block:: bash

    $ pip install -r requirements_test.txt

"""
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
_WRITE_TEST = """=================
First Level Title
=================

.. This is a comment.

-------------------
Second Level Title.
-------------------


=======
Testing
=======

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block:: bash

    $ pip install -r requirements_test.txt

"""

b_tls = Archiver(_DESC, _PATH)


class TestRstBuilder:
    def test__init__no_detail(self):
        """Testing rstbuilder__init_no_detail()"""
        t_rstbuilder = RSTBuilder()

        assert not t_rstbuilder.contents
        assert t_rstbuilder.curr_pos == 0
        assert t_rstbuilder.element_cntr == 0
        assert t_rstbuilder.elements == {}
        assert t_rstbuilder.loger_name is None
        assert t_rstbuilder.logger is None
        assert t_rstbuilder.src_pth is None
        assert t_rstbuilder.tab_len == 4
        assert t_rstbuilder.verbose is True
        pass

    def test__init__with_details(self, working_dir_self_destruct):
        """Testing rstbuilder__init_with_details()"""
        working_dir = working_dir_self_destruct
        test_rst_pth = working_dir.dir / 'test_rst_file.rst'
        t_rstbuilder = RSTBuilder(
            p_pth=test_rst_pth,
            p_first_level_title="First Level Title",
            p_tab_len=8,
            p_verbose=True,
            p_parent_log_name=_NAME,
        )

        assert not t_rstbuilder.contents
        assert t_rstbuilder.curr_pos == 0
        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "FirstLevelTitle",
                "Text": "=================\nFirst Level Title\n=================\n\n",
            }
        }
        assert t_rstbuilder.loger_name == f"{_NAME}.RSTBuilder"
        assert isinstance(t_rstbuilder.logger, logging.Logger)
        assert t_rstbuilder.src_pth == test_rst_pth
        assert t_rstbuilder.tab_len == 8
        assert t_rstbuilder.verbose is True
        pass

    def test__iter__(self):
        """Testing rstbuilder__iter_no_detail()"""
        t_rstbuilder = RSTBuilder(p_first_level_title="First Level Title")

        assert isinstance(t_rstbuilder, RSTBuilder)
        assert t_rstbuilder.curr_pos == 0
        pass

    def test__next__(self):
        """Testing rstbuilder__iter_no_detail()"""
        t_rstbuilder = RSTBuilder()
        t_rstbuilder.add_paragraph("Par 1")
        t_rstbuilder.add_paragraph("Par 2")
        t_rstbuilder.add_paragraph("Par 3")

        elements = iter(t_rstbuilder)

        assert next(elements) == {"Text": "Par 1\n\n", "Type": "Paragraph"}
        assert next(elements) == {"Text": "Par 2\n\n", "Type": "Paragraph"}
        assert next(elements) == {"Text": "Par 3\n\n", "Type": "Paragraph"}
        pass

    def test_add_comment(self):
        """Testing rstbuilder_add_comment()"""
        t_rstbuilder = RSTBuilder()
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

    def test_add_formatted_text(self):
        """Testing rstbuilder_add_paragraph()"""
        t_rstbuilder = RSTBuilder()

        t_rstbuilder.add_formatted_text(_FORMATED_TEXT)
        assert t_rstbuilder.elements == {
            0: {"Type": "FormattedText", "Text": _FORMATED_TEXT}
        }
        pass

    def test_add_image_directive_basic(self):
        """Testing rstbuilder_add_image_directive_basic()"""
        t_rstbuilder = RSTBuilder()
        t_rstbuilder.add_directive_image(p_uri=_URI)

        assert t_rstbuilder.elements == {
            0: {
                "Text": ".. image:: https://img.shields.io/pypi/v/BEETest?style = plastic\n\n",
                "Type": "DirectiveImage",
            }
        }
        assert t_rstbuilder.element_cntr == 1
        pass

    def test_add_image_directive_with_detail(self):
        """Testing rstbuilder_add_image_directive_with_detail()"""
        t_rstbuilder = RSTBuilder()
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

    def test_add_fifth_level_tile(self):
        """Testing rstbuilder_add_fifth_level_tile()"""
        t_rstbuilder = RSTBuilder()
        t_rstbuilder.add_fifth_level_title("Fifth Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "FifthLevelTitle",
                "Text": "Fifth Level Title\n'''''''''''''''''\n\n",
            }
        }
        pass

    def test_add_first_level_title(self):
        """Testing rstbuilder_add_first_level_title()"""
        t_rstbuilder = RSTBuilder()
        t_rstbuilder.add_first_level_title("First Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "FirstLevelTitle",
                "Text": "=================\nFirst Level Title\n=================\n\n",
            }
        }
        pass

    def test_add_fourth_level_title(self):
        """Testing rstbuilder_add_fourth_level_title()"""
        t_rstbuilder = RSTBuilder()
        t_rstbuilder.add_fourth_level_title("Fourth Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "FourthLevelTitle",
                "Text": "Fourth Level Title\n------------------\n\n",
            }
        }
        pass

    def test_add_paragraph(self):
        """Testing rstbuilder_add_paragraph()"""
        t_rstbuilder = RSTBuilder()
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

    def test_add_second_level_title(self):
        """Testing rstbuilder_add_second_level_title()"""
        t_rstbuilder = RSTBuilder()
        t_rstbuilder.add_second_level_title("Second Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "SecondLevelTitle",
                "Text": "------------------\nSecond Level Title\n------------------\n\n",
            }
        }
        pass

    def test_add_third_level_title(self):
        """Testing rstbuilder_add_third_level_title()"""
        t_rstbuilder = RSTBuilder()
        t_rstbuilder.add_third_level_title("Third Level Title")

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "ThirdLevelTitle",
                "Text": "Third Level Title\n=================\n\n",
            }
        }
        pass

    def test_add_toctree(self):
        """Testing rstbuilder_add_toctree()"""
        t_rstbuilder = RSTBuilder()
        toc_items = ["Conventions", "api", "examples"]
        t_rstbuilder.add_toctree(
            toc_items, p_maxdepth=2, p_caption="Contents", p_numbered=True
        )

        assert t_rstbuilder.element_cntr == 1
        assert t_rstbuilder.elements == {
            0: {
                "Type": "TocTree",
                "Text": ".. toctree::\n    :maxdepth: 2\n    :caption: Contents\n    :numbered:\n\n    Conventions\n"
                + "    api\n    examples\n\n",
                "Items": ["Conventions", "api", "examples"],
            }
        }
        pass

    def test_insert_at(self):
        """Testing rstbuilder__init_with_details()"""
        t_rstbuilder = RSTBuilder(p_first_level_title="First Level Title")
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

    def test_make_indent(self):
        """Testing rstbuilder_make_indent()"""
        t_rstbuilder = RSTBuilder()

        assert t_rstbuilder._make_indent(0) == ""
        assert t_rstbuilder._make_indent(1) == "    "
        assert t_rstbuilder._make_indent(2) == "        "
        pass

    def test_underline(self):
        """Testing rstbuilder_underline()"""
        t_rstbuilder = RSTBuilder(p_first_level_title="First Level Title")
        assert t_rstbuilder._underline("First Level Title", "=") == "================="
        assert t_rstbuilder.element_cntr == 1
        pass

    def test_write(self, working_dir_self_destruct):
        """Testing rstbuilder_underline()"""
        working_dir = working_dir_self_destruct
        test_rst_pth = working_dir.dir / 'test_rst_file.rst'
        t_rstbuilder = RSTBuilder(test_rst_pth)
        t_rstbuilder.add_first_level_title("First Level Title")
        t_rstbuilder.add_comment("This is a comment.")
        t_rstbuilder.add_second_level_title("Second Level Title.")
        t_rstbuilder.add_formatted_text(_FORMATED_TEXT)
        t_rstbuilder.write_text()
        assert test_rst_pth.read_text() == _WRITE_TEST
