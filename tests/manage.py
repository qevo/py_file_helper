"""Tests for the file_helper.manage module"""

import os, sys, unittest, inspect
from re import IGNORECASE
from BaseTest import BaseTestWrapper


class FindFileTestCase(BaseTestWrapper.BaseTest):
    """manage.find_file() test cases"""

    def test_this_file(self):
        """Test if this same file can be found by searching this same directory"""

        path = os.path.abspath(inspect.getfile(inspect.currentframe()).replace('.pyc', '.py'))
        name = os.path.basename(path)

        args = {
            "re_filter": ['*' + name],
            "branch": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": True,
            "get_dir": False,
            "case_i": False
        }

        result = self._bt['func'](**args)
        self.assertIn(path, result)


    def test_this_file_case_i(self):
        """Test if this same file can be found by searching this same directory case insensitive"""

        path = os.path.abspath(inspect.getfile(inspect.currentframe()).replace('.pyc', '.py'))
        name = os.path.basename(path)

        args = {
            "re_filter": ['*' + name.upper()],
            "branch": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": True,
            "get_dir": False,
            "case_i": True
        }

        result = self._bt['func'](**args)
        self.assertIn(path, result)


    def test_this_dir(self):
        """Test if the current working directory can be found by searching its parent directory"""
    
        path = os.getcwd()
        name = os.path.basename(path)

        args = {
            "re_filter": ['*' + name],
            "branch": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": False,
            "get_dir": True,
            "case_i": False
        }
    
        result = self._bt['func'](**args)
        self.assertEqual(path, ''.join(result))
    
    
    def test_this_file_recurse(self):
        """Test if this same file can be found recursively"""
    
        path = os.path.abspath(inspect.getfile(inspect.currentframe()).replace('.pyc', '.py'))
        name = os.path.basename(path)
    
        args = {
            "re_filter": ['*' + name],
            "branch": os.path.abspath(os.path.dirname(path) + '/..'),
            "recurse": True,
            "depth": 0,
            "get_file": True,
            "get_dir": False,
            "case_i": False
        }
    
        result = self._bt['func'](**args)
        # it is only because 'branch' is an absolute path that we can expect 'path' to be in 'result'
        self.assertIn(path, result)
    
    
    def test_this_dir_recurse(self):
        """Test if the current working directory can be found by searching its parent's parent directory"""
    
        path = os.getcwd()
        name = os.path.basename(path)
    
        args = {
            "re_filter": ['*' + name],
            "branch": os.path.abspath(os.path.dirname(path) + '/..'),
            "recurse": True,
            "depth": 0,
            "get_file": False,
            "get_dir": True,
            "case_i": False
        }
    
        result = self._bt['func'](**args)
        self.assertIn(path, result)
    
    
    def test_os_mod_file(self):
        """Test if this same file can be found"""
    
        path = inspect.getfile(sys.modules['os'])
        name = os.path.basename(path)
    
        args = {
            "re_filter": ['*' + name],
            "branch": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": True,
            "get_dir": False,
            "case_i": False
        }
    
        result = self._bt['func'](**args)
        self.assertEqual(path, ''.join(result))


class FindFileReTestCase(BaseTestWrapper.BaseTest):
    """manage.find_file_re() test cases"""

    def test_this_file(self):
        """Test if this same file can be found by searching this same directory"""

        path = os.path.abspath(inspect.getfile(inspect.currentframe()).replace('.pyc', '.py'))
        name = os.path.basename(path)

        args = {
            "re_filter": ['^.*' + name + '$'],
            "branch": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": True,
            "get_dir": False,
            "re_flag": 0
        }

        result = self._bt['func'](**args)
        self.assertEqual(path, ''.join(result))


    def test_this_file_case_i(self):
        """Test if this same file can be found by searching this same directory case insensitive"""

        path = os.path.abspath(inspect.getfile(inspect.currentframe()).replace('.pyc', '.py'))
        name = os.path.basename(path)

        args = {
            "re_filter": ['^.*' + name + '$'],
            "branch": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": True,
            "get_dir": False,
            "re_flag": IGNORECASE
        }

        result = self._bt['func'](**args)
        self.assertEqual(path, ''.join(result))


    def test_this_dir(self):
        """Test if the current working directory can be found by searching its parent directory"""

        path = os.getcwd()
        name = os.path.basename(path)

        args = {
            "re_filter": ['^.*' + name + '$'],
            "branch": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": False,
            "get_dir": True,
            "re_flag": 0
        }

        result = self._bt['func'](**args)
        self.assertEqual(path, ''.join(result))


    def test_this_file_recurse(self):
        """Test if this same file can be found recursively"""

        path = os.path.abspath(inspect.getfile(inspect.currentframe()).replace('.pyc', '.py'))
        name = os.path.basename(path)

        args = {
            "re_filter": ['^.*' + name + '$'],
            "branch": os.path.abspath(os.path.dirname(path) + '/..'),
            "recurse": True,
            "depth": 0,
            "get_file": True,
            "get_dir": False,
            "re_flag": 0
        }

        result = self._bt['func'](**args)
        # it is only because 'branch' is an absolute path that we can expect 'path' to be in 'result'
        self.assertIn(path, result)


    def test_this_dir_recurse(self):
        """Test if the current working directory can be found by searching its parent's parent directory"""

        path = os.getcwd()
        name = os.path.basename(path)

        args = {
            "re_filter": ['^.*' + name + '$'],
            "branch": os.path.abspath(os.path.dirname(path) + '/..'),
            "recurse": True,
            "depth": 0,
            "get_file": False,
            "get_dir": True,
            "re_flag": 0
        }

        result = self._bt['func'](**args)
        self.assertIn(path, result)


    def test_os_mod_file(self):
        """Test if this same file can be found"""

        path = inspect.getfile(sys.modules['os'])
        name = os.path.basename(path)

        args = {
            "re_filter": ['^.*' + name + '$'],
            "branch": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": True,
            "get_dir": False,
            "re_flag": 0
        }

        result = self._bt['func'](**args)
        self.assertEqual(path, ''.join(result))


class ListDirTestCase(BaseTestWrapper.BaseTest):
    """manage.list_dir() test cases"""

    def test_this_file(self):
        """Test if this same file can be found by searching this same directory"""

        path = os.path.abspath(inspect.getfile(inspect.currentframe()).replace('.pyc', '.py'))
        name = os.path.basename(path)

        args = {
            "dir": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": True,
            "get_dir": False
        }

        result = self._bt['func'](**args)
        self.assertIn(path, result)


    def test_this_file_recurse(self):
        """Test if this same file can be found by recursively searching this same directory"""

        path = os.path.abspath(inspect.getfile(inspect.currentframe()).replace('.pyc', '.py'))
        name = os.path.basename(path)

        args = {
            "dir": os.path.dirname(path),
            "recurse": True,
            "depth": 1,
            "get_file": True,
            "get_dir": False
        }

        result = self._bt['func'](**args)
        self.assertIn(path, result)


    def test_this_dir(self):
        """Test if the current working directory can be found by searching its parent directory"""

        path = os.getcwd()
        name = os.path.basename(path)

        args = {
            "dir": os.path.dirname(path),
            "recurse": False,
            "depth": 0,
            "get_file": False,
            "get_dir": True
        }

        result = self._bt['func'](**args)
        self.assertIn(path, result)


    def test_this_dir_recurse(self):
        """Test if the current working directory can be found by recursively searching its parent directory"""

        path = os.getcwd()
        name = os.path.basename(path)

        args = {
            "dir": os.path.dirname(path),
            "recurse": True,
            "depth": 1,
            "get_file": False,
            "get_dir": True
        }

        result = self._bt['func'](**args)
        self.assertIn(path, result)


loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(sys.modules[__name__])

if __name__ == '__main__':
    result = unittest.result.TestResult()
    suite.run(result)
    print result
    for f in result.failures:
        for t in f:
            print t
        print ''
    for e in result.errors:
        for t in e:
            print t
        print ''
