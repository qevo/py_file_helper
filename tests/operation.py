"""Tests for the file_helper.operation module"""

import os, sys, unittest, inspect, shutil
from BaseTest import BaseTestWrapper


class HashFileTestCase(BaseTestWrapper.BaseTest):
    """operation.hash_file() test cases"""

    def test_sample_md5(self):
        """Test the sample file md5"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        name = '_4k_sample.txt'

        known_hash = '88a12349e07201fe1dc60270220893a1'

        hash_name = 'md5'
        path = os.path.join(dir, name)
        size=None
        offset=0
        whence=0

        result = self._bt['func'](hash_name, path, size, offset, whence)
        self.assertEqual(known_hash, result)


    def test_sample_sha1(self):
        """Test the sample file sha1"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        name = '_4k_sample.txt'

        known_hash = 'fd5e763f35957236886c4394e2273c14ac0ff4e6'

        hash_name = 'sha1'
        path = os.path.join(dir, name)
        size=None
        offset=0
        whence=0

        result = self._bt['func'](hash_name, path, size, offset, whence)
        self.assertEqual(known_hash, result)


    def test_sample_slice(self):
        """Test the slice of a sample file"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        hash_name = 'sha1'
        size=None
        offset=0
        whence=0

        name = '_1k_sample.txt'
        path = os.path.join(dir, name)
        result_1k = self._bt['func'](hash_name, path, size, offset, whence)

        name = '_2k_sample.txt'
        path = os.path.join(dir, name)
        f = open(path, 'rb')
        contents = f.read(1000)
        f.close()

        name = '_2k_sample.txt.slice'
        path = os.path.join(dir, name)
        f = open(path, 'wb')
        f.write(contents)
        f.close()
        result_2k = self._bt['func'](hash_name, path, size, offset, whence)
        os.remove(path)

        self.assertEqual(result_1k, result_2k)


class ReadFileTestCase(BaseTestWrapper.BaseTest):
    """operation.read_file() test cases"""

    def test_sample_1k(self):
        """Test the sample file"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        name = '_1k_sample.txt'

        path = os.path.join(dir, name)
        size = None
        offset = 0
        whence = 0

        compare = '0'
        while len(compare) < 1000:
            compare += '0'
        result = self._bt['func'](path, size, offset, whence)
        self.assertEqual(compare, result)


    def test_sample_slice(self):
        """Test the sample file"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        name = '_2k_sample.txt'

        path = os.path.join(dir, name)
        size = 1000
        offset = 0
        whence = 0

        compare = '0'
        while len(compare) < 1000:
            compare += '0'
        result = self._bt['func'](path, size, offset, whence)
        self.assertEqual(compare, result)


class SliceFileTestCase(BaseTestWrapper.BaseTest):
    """operation.slice_file() test cases"""

    def test_sample_2k(self):
        """Test the sample file"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        name = '_2k_sample.txt'

        path = os.path.join(dir, name)
        size = 1000
        offset = 0
        whence = 0
        output_dir = dir
        slice_name = None
        slice_ext = None

        slice_path = self._bt['func'](path, size, offset, whence, output_dir, slice_name, slice_ext)

        name = '_1k_sample.txt'
        path = os.path.join(dir, name)
        f = open(path, 'rb')
        contents1 = f.read()
        f.close()

        f = open(slice_path, 'rb')
        contents2 = f.read()
        f.close()
        os.remove(slice_path)
        self.assertEqual(contents1, contents2)


    def test_sample_slice(self):
        """Test the sample contents"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        name = '_2k_sample.txt'

        path = os.path.join(dir, name)
        size = 1000
        offset = 0
        whence = 0

        compare = '0'
        while len(compare) < 1000:
            compare += '0'
        slice_path = self._bt['func'](path, size, offset, whence)
        f = open(slice_path, 'rb')
        contents = f.read()
        f.close()
        os.remove(slice_path)
        self.assertEqual(compare, contents)


class WriteFileTestCase(BaseTestWrapper.BaseTest):
    """operation.write_file() test cases"""

    def test_new_1k(self):
        """Test if a write creates the same file as sample"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        name = '_1k_sample.txt'

        path = os.path.join(dir, name)
        temp_path = os.path.join(dir, name+'.tmp')

        data = '0'
        while len(data) < 1000:
            data += '0'
        mode = 'new'
        offset = 0
        whence = 0

        temp_path = self._bt['func'](temp_path, data, mode, offset, whence)

        f = open(path, 'rb')
        contents1 = f.read()
        f.close()

        f = open(temp_path, 'rb')
        contents2 = f.read()
        f.close()
        os.remove(temp_path)
        self.assertEqual(contents1, contents2)


    def test_overwrite(self):
        """Test the overwrite of a sample"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        name = '_2k_sample.txt'

        path = os.path.join(dir, name)
        shutil.copy(path, path+'.tmp')

        s_zero = '0'
        s_one = '1'
        while len(s_one) < 1000:
            s_zero += '0'
            s_one += '1'

        mode = 'overwrite'
        offset = 1000
        whence = 0

        temp_path = self._bt['func'](path+'.tmp', s_one, mode, offset, whence)

        f = open(temp_path, 'rb')
        contents = f.read()
        f.close()
        os.remove(temp_path)
        self.assertEqual(s_zero + s_one, contents)


    def test_append(self):
        """Test the append of data to a sample file"""

        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        name = '_2k_sample.txt'

        path = os.path.join(dir, name)
        path_4k = os.path.join(dir, '_4k_sample.txt')
        shutil.copy(path, path+'.tmp')

        s_zero = '0'
        while len(s_zero) < 2000:
            s_zero += '0'

        mode = 'append'
        offset = 0
        whence = 2

        temp_path = self._bt['func'](path+'.tmp', s_zero, mode, offset, whence)

        f = open(path_4k, 'rb')
        contents1 = f.read()
        f.close()

        f = open(temp_path, 'rb')
        contents2 = f.read()
        f.close()
        os.remove(temp_path)
        self.assertEqual(contents1, contents2)


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
