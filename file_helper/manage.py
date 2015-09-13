"""File management wrapper functions to streamline common use cases"""

import os, re, sys
from functools import partial
from data_helper import list_filter, wildcard_re, is_bool, is_str, is_int_neg, is_list, is_str_not_empty


def find_file(re_filter=None, branch=".", recurse=True, depth=0, get_file=True, get_dir=True, case_i=True):
    """Search a branch directory for files and / or directories whose name matches one or more of the filter patterns

    Args:
        branch (str): (optional) Directory to search. Suggestion: use absolute path. Defaults to current working directory.
        re_filter (list): (optional) List of strings of wildcard patterns. Defaults to None, which skips any filtering.
        recurse (bool): (optional) Recursive search flag. Defaults to True.
        depth (int): (optional) Set the recursion depth. Defaults to 0, which has a max of Python's recursion limit.
        get_file (bool): (optional) Return entry for file. Defaults to True.
        get_dir (bool): (optional) Return entry for directory. Defaults to True.
        case_i (bool): (optional) Case insensitive search. Defaults to True.

    Returns:
        list: List of strings with paths of files.

    """
    if not is_str_not_empty(branch): raise ValueError("branch must be a non empty string")
    if not os.path.isdir(branch): raise ValueError("branch must be a valid directory")
    if not is_bool(recurse): raise ValueError("recurse must be True or False")
    if is_int_neg(depth): raise ValueError("depth must be >= 0")
    if not is_bool(get_file): raise ValueError("get_file must be True or False")
    if not is_bool(get_dir): raise ValueError("get_dir must be True or False")
    if not is_bool(case_i): raise ValueError("case_i must be True or False")

    search_results = list_dir(branch, recurse, depth, get_file, get_dir)

    if re_filter is None or len(re_filter) < 1:
        return search_results
    elif re_filter == '*':
        return search_results
    elif is_list(re_filter) and '*' in re_filter:
        return search_results

    if is_str(re_filter):
        re_filter = [re_filter]

    re_flag = 0
    if case_i:
        re_flag = re.IGNORECASE

    bre = partial(wildcard_re, wildcard='*', escape='\\')
    return list_filter( map(bre, re_filter), search_results, re_flag)


def find_file_re(re_filter=None, branch='.', recurse=True, depth=0, get_file=True, get_dir=True, re_flag=0):
    """Search a branch directory for files and / or directories whose name matches one or more of the regex filter patterns

    Args:
        branch (str): (optional) Directory to search. Suggestion: use absolute path. Defaults to current working directory.
        re_filter (list): (optional) List of strings of regular expression patterns. Defaults to None, which skips any filtering.
        recurse (bool): (optional) Recursive search flag. Defaults to True.
        depth (int): (optional) Set the recursion depth. Defaults to 0, which has a max of Python's recursion limit.
        get_file (bool): (optional) Return entry for file. Defaults to True.
        get_dir (bool): (optional) Return entry for directory. Defaults to True.
        re_flag (int): (optional) See :py:mod:`re`

    Returns:
        list: List of strings with paths of files.

    """
    if not is_str_not_empty(branch): raise ValueError("branch must be a non empty string")
    if not os.path.isdir(branch): raise ValueError("branch must be a valid directory")
    if not is_bool(recurse): raise TypeError("recurse must be True or False")
    if is_int_neg(depth): raise ValueError("depth must be >= 0")
    if not is_bool(get_file): raise ValueError("get_file must be True or False")
    if not is_bool(get_dir): raise ValueError("get_dir must be True or False")

    search_results = list_dir(branch, recurse, depth, get_file, get_dir)

    if re_filter is None or len(re_filter) < 1:
        return search_results

    if is_str(re_filter):
        re_filter = [re_filter]

    return list_filter(re_filter, search_results, re_flag)


def list_dir(dir='.', recurse=True, depth=0, get_file=True, get_dir=True):
    """Search a directory for files and directories

    Args:
        dir (str): (optional) Directory to search. Suggestion: use absolute path. Defaults to current working directory.
        recurse (bool): (optional) Recursive search flag. Defaults to True.
        depth (int): (optional) Set the recursion depth. Defaults to 0, which has a max of Python's recursion limit.
        get_dir (bool): (optional) Return entry for directory. Defaults to True.
        get_file (bool): (optional) Return entry for file. Defaults to True.

    Returns:
        list: List of strings of paths for files and directories.

    """
    if not is_str_not_empty(dir): raise ValueError("dir must be a non empty string")
    if not os.path.isdir(dir): raise ValueError("dir must be a valid directory")
    if not is_bool(recurse): raise TypeError("recurse must be True or False")
    if is_int_neg(depth): raise ValueError("depth must be >= 0")
    if not is_bool(get_file): raise TypeError("get_file must be True or False")
    if not is_bool(get_dir): raise TypeError("get_dir must be True or False")

    list = []
    i = 0
    if recurse == True:
        os_walk = os.walk(dir, topdown=True)
        for root, dirs, files in os_walk:
            if get_file == True:
                for name in files:
                    list.append(os.path.join(os.path.abspath(root), name))
            if get_dir == True:
                for name in dirs:
                    list.append(os.path.join(os.path.abspath(root), name))
            i += 1
            if depth == i:
                break
    else:
        listdir = os.listdir(dir)
        for name in listdir:
            path = os.path.join(os.path.abspath(dir), name)
            if get_dir == True and get_file == True:
                list.append(path)
            elif get_file == True and os.path.isfile(path) == True:
                list.append(path)
            elif get_dir == True and os.path.isdir(path) == True:
                list.append(path)
    return list
