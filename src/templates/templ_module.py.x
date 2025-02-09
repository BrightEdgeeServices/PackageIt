'''{3}

{4}
'''

import logging
from pathlib import Path

# from beetools import beearchiver
from beetools import utils
from termcolor import colored

_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)


def project_desc():
    return _PROJ_DESC


class {0}:
    '''Class short description one-liner goes here.

    Class multi-liner detail description goes here.
    '''
    def __init__(
        self,
        p_project_name,
        p_dir,
        p_parent_log_name = '',
        p_verbose = True
    ):
        '''Initialize the class

        Parameters
        ----------
        p_parent_log_name : str
            Name of the parent.  In combination witt he class name it will
            form the logger name.
        p_logger : bool, default = False
            Activate the logger
        p_verbose: bool, default = True
            Write messages to the console.

        Returns
        -------

        See Also
        --------

        Notes
        -----

        Examples
        --------
        '''
        self.success = True
        if p_parent_log_name:
            self.log_name = '{1}.{1}'.format(p_parent_log_name, {0})
            self.logger = logging.getLogger(self._log_name)
        self.project_name = p_project_name
        self.dir = p_dir
        self.verbose = p_verbose

    def method_1(self, p_msg):
        '''Method short description one-liner goes here.

        Class multi-liner detail description goes here.

        Parameters
        ----------

        Returns
        -------

        See Also
        --------

        Notes
        -----

        Examples
        --------

        '''
        print(colored('Testing {1}...'.format(self.project_name), 'yellow'))
        print(colored('Message: {1}'.format(p_msg), 'yellow'))
        return True

def do_examples(p_cls = True):
    '''A collection of implementation examples for {0}.

    A collection of implementation examples for {0}. The examples
    illustrate in a practical manner how to use the methods.  Each example
    show a different concept or implementation.

    Parameters
    ----------
    p_cls : bool, default = True
        Clear the screen or not at startup of Archiver

    Returns
    -------
    success : boolean
        Execution status of the examples.

    See Also
    --------

    Notes
    -----

    Examples
    --------

    '''
    success = do_example1(p_cls)
    success = do_example2(False) and success
    return success


def do_example1(p_cls = True):
    '''A working example of the implementation of {0}.

    Example1 illustrate the following concepts:
    1. Bla, bla, bla
    2. Bla, bla, bla

    Parameters
    ----------
    p_cls : bool, default = True
        Clear the screen or not at startup of Archiver

    Returns
    -------
    success : boolean
        Execution status of the example

    See Also
    --------

    Notes
    -----

    Examples
    --------

    '''
    success = True
    # archiver = beearchiver.Archiver(_PROJ_DESC, _PROJ_PATH)
    # archiver.print_header(p_cls = p_cls)
    t_dir = utils.get_tmp_dir()
    t_{2} = {0}("{0}", t_dir)
    t_{2}.method_1('This is do_example1')
    utils.rm_tree(t_dir)
    # archiver.print_footer()
    return success


def do_example2(p_cls = True):
    '''Another working example of the implementation of {0}.

    Example2 illustrate the following concepts:
    1. Bla, bla, bla
    2. Bla, bla, bla

    Parameters
    ----------
    p_cls : bool, default = True
        Clear the screen or not at startup of Archiver

    Returns
    -------
    success : boolean
        Execution status of the method

    See Also
    --------

    Notes
    -----

    Examples
    --------

    '''
    success = True
    archiver = beearchiver.Archiver(_PROJ_DESC, _PROJ_PATH)
    archiver.print_header(p_cls = p_cls)
    t_dir = utils.get_tmp_dir()
    t_{2} = {0}("{0}", t_dir)
    t_{2}.method_1('This is do_example2')
    utils.rm_tree(t_dir)
    archiver.print_footer()
    return success


if __name__ == '__main__':
    do_examples()
