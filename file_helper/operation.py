"""File operations wrapper functions to streamline common use cases"""

import os
from data_helper import hash, is_str_not_empty, is_int_pos, is_int_not_neg


def hash_file(hash_name, path, size=None, offset=0, whence=0):
    """Return the hash of a file

    Args:
        hash_name (str): Hash algorithm name. See :py:mod:`hashlib`
        path (str): Path of file.
        size (int): (optional) Read length in bytes. Defaults to None.
        offset (int): (optional) Offset from the whence position. Defaults to 0.
        whence (int): (optional) Originating file seek position. 0 - Absolute, 1 - Current, 2 - End of file. Defaults to 0.

    Returns:
        str: Hash (hex) string.

    """
    if not is_str_not_empty(hash_name): raise ValueError("hash_name must be a string")
    if not is_str_not_empty(path): raise ValueError("file path must be a string")
    if not is_int_not_neg(offset): raise ValueError("offset must be a positive integer")
    if whence not in [0,1,2]: raise ValueError("whence must be 0 - Absolute, 1 - Current, 2 - End of file")

    data = read_file(path, size, offset, whence)
    alg = getattr(hash, hash_name.lower())
    return alg(data)


def read_file(path, size=None, offset=0, whence=0):
    """Read a file in binary mode

    Args:
        path (str): Path of file.
        size (int): Read length in bytes. Defaults to None.
        offset (int): (optional) Offset from the whence position. Defaults to 0.
        whence (int): (optional) Originating file seek position. 0 - Absolute, 1 - Current, 2 - End of file. Defaults to 0.

    Returns:
        str: Binary data.

    """
    if not is_str_not_empty(path): raise ValueError("file path must be a string")
    if not is_int_not_neg(offset): raise ValueError("offset must be a positive integer")
    if whence not in [0,1,2]: raise ValueError("whence must be 0 - Absolute, 1 - Current, 2 - End of file")

    f = open(path, 'rb')
    f.seek(offset, whence)
    if size is None:
        data = f.read()
    else:
        data = f.read(size)
    f.close()
    return data


def slice_file(path, size, offset=0, whence=0, output_dir=None, slice_name=None, slice_ext=None):
    """Write a new file from a slice of an existing file

    Args:
        path (str): Path of existing file.
        size (int): Read length in bytes.
        offset (int): (optional) Offset from the whence position. Defaults to 0.
        whence (int): (optional) Originating file seek position. 0 - Absolute, 1 - Current, 2 - End of file. Defaults to 0.
        output_dir (str): (optional) Path to the directory where new file is saved.
        slice_name (str): (optional) File name of the slice file. Defaults to the full file's name (with extension).
        slice_ext (str): (optional) File extension of the slice file. Defaults to 'slice_oYYwXX' where YY and XX are the offset and whence respectively.

    Returns:
        str: File path of slice file.

    """
    if not is_str_not_empty(path): raise ValueError("file path must be a string")
    if not is_int_pos(size): raise ValueError("size must be a positive integer")
    if not is_int_not_neg(offset): raise ValueError("offset must be a non negative integer")
    if whence not in [0,1,2]: raise ValueError("whence must be 0 - Absolute, 1 - Current, 2 - End of file")

    output_dir = os.path.abspath('.') if output_dir is None else os.path.abspath(output_dir)
    ext = slice_ext if is_str_not_empty(slice_ext) else 'slice_o' + str(offset) + 'w' + str(whence)
    name = slice_name if is_str_not_empty(slice_name) else os.path.split(path)[1]

    slice_path = os.path.abspath(os.path.join(output_dir, name + '.' + ext))

    write_file(slice_path, read_file(path, size, offset, whence))

    return slice_path


def write_file(path, data, mode='new', offset=0, whence=0):
    """Write a file in binary mode

    Args:
        path (str): Path of file.
        data (str): Data to be written.
        mode (str): (optional) 'new' for a new or replacement file. 'insert' for writing more data into a file. 'overwrite' for writing new data over a file. 'append' for adding to the end of a file. Defaults to 'new'.
        offset (int): (optional) Offset from the whence position. Defaults to 0.
        whence (int): (optional) Originating file seek position. 0 - Absolute, 1 - Current, 2 - End of file. Defaults to 0.

    Returns:
        str: File path to written file.

    """
    if not is_str_not_empty(path): raise ValueError("file path must be a string")
    if not is_str_not_empty(data): raise ValueError("data must be a string")
    if mode not in ['new','insert','overwrite','append']: raise ValueError("mode must be 'new' or 'insert' or 'overwrite' or 'append'")
    if not is_int_not_neg(offset): raise ValueError("offset must be a non negative integer")
    if whence not in [0,1,2]: raise ValueError("whence must be 0 - Absolute, 1 - Current, 2 - End of file")

    path = os.path.abspath(path)
    #: create the directory path to the file if it doesn't exist
    if not os.path.exists(os.path.split(path)[0]):
        mode = 'new'
        os.makedirs(os.path.split(path)[0])
    #: stop an attempt to overwrite a directory
    elif os.path.isdir(path) == True:
        raise ValueError('may not write file over a directory: ' + path)

    if mode == 'append':
        offset = 0
        whence = 2

    if mode == 'insert' or mode == 'overwrite' or mode == 'append':
        original_file_size = os.stat(path).st_size
        original_file = open(path, 'rb')
        #: determine the offset position for the write action
        original_file.seek(offset, whence)
        start_pos = original_file.tell()
        original_file.seek(0, 0)

        #: create a temporary file
        temp_file = open(path + '.tmp', 'wb')
        #: write any offset data
        if start_pos > 0:
            temp_file.write(original_file.read(start_pos))
        #: write new data
        temp_file.write(data)
        temp_file.flush()
        os.fsync(temp_file.fileno())
        temp_file.close()
        temp_file_size = os.stat(path + '.tmp').st_size

        #: write any remaining data from the original file
        if mode == 'overwrite' and temp_file_size < original_file_size:
            temp_file = open(path + '.tmp', 'ab')
            original_file.seek(temp_file_size, 0)
            temp_file.write(original_file.read())
            temp_file.flush()
            os.fsync(temp_file.fileno())
            temp_file.close()
        elif mode == 'insert':
            temp_file = open(path + '.tmp', 'ab')
            original_file.seek(start_pos, 0)
            temp_file.write(original_file.read())
            temp_file.flush()
            os.fsync(temp_file.fileno())
            temp_file.close()

        original_file.close()
        #: replace the original file
        os.rename(path + '.tmp', path)
    elif mode == 'new':
        f = open(path, 'wb')
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
        f.close()

    return path
