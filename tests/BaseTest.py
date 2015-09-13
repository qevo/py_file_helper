import unittest, inspect, os, sys

if sys.path[0] != '..':
    sys.path.insert(0, '..')
import file_helper as tested_pkg
from data_helper.transform import camelcase_to_underscore


class BaseTestWrapper(object):
    class BaseTest(unittest.TestCase):
        """Test case class to group common methods"""

        @classmethod
        def setUpClass(self):
            """Setting up the class"""

            cls = self.__mro__[0]
            self._bt = {'test_class': cls}
            self._bt['mod_name'] = os.path.basename(inspect.getfile(cls)).replace('.pyc', '').replace(
                '.py', '')
            self._bt['tested_mod'] = getattr(tested_pkg, self._bt['mod_name'])
            self._bt['func_name'] = camelcase_to_underscore(cls.__name__.replace('TestCase', ''))
            self._bt['func'] = getattr(self._bt['tested_mod'], self._bt['func_name'])
            try:
                self._bt['default_args'] = get_default_args(self._bt['func'])
            except:
                pass

        def setUp(self):
            """Setting up for the test"""
            pass
            # test_name = self.shortDescription()
            # print test_name

        def tearDown(self):
            """Cleaning up after the test"""
            pass
            # print '...done'


def get_default_args(f):
    """Returns a dictionary of arg_name:default_values for the input function

    Args:
        f (func): A function

    Returns:
        dict: Dictionary of function argument keynames with default values.

    """
    args, varargs, keywords, defaults = inspect.getargspec(f)
    return dict(zip(args[-len(defaults):], defaults))
