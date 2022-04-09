import pytest
import subprocess
from enum import Enum
from pathlib import Path
import git


class Env:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    @property
    def dir_a(self):
        return self.base_dir / Path('dir_a')

    @property
    def dir_b(self):
        return self.base_dir / Path('dir_b')

    @property
    def file_a(self):
        return self.dir_b / Path('file_a.txt')

    @property
    def bookmarks_file(self):
        # the bookmark file to be used during testing
        # it would be reckless to use the real system-wide file
        return self.base_dir / Path('bookmarks.txt')


@pytest.fixture
def environment(tmp_path):
    env = Env(tmp_path)
    # Initialize a dummy environment in the file system
    (env.dir_a).mkdir()
    (env.dir_b).mkdir()
    open(env.file_a, 'a').close()
    return env


def invoke(command, bookmarks_file):
    repo_root = git.Repo('.', search_parent_directories=True).working_tree_dir
    r = subprocess.run(['/bin/zsh', 'zfm.zsh'] + command,
                       cwd=repo_root,
                       capture_output=True,
                       text=True,
                       env={'ZFM_BOOKMARKS_FILE': bookmarks_file})
    r.check_returncode
    return r.stdout


class BookmarkType(Enum):
    File = 1
    Dir = 2


class Bookmark:
    def __init__(self, path, type):
        self.path = path
        self.type = type

    @classmethod
    def fromLine(cls, bookmark_line):
        s = bookmark_line.split()
        path = Path(s[0].strip())
        type = BookmarkType.Dir if s[1].strip(
        ) == '[d]' else BookmarkType.File
        return cls(path, type)

    def __eq__(self, other):
        return self.path == other.path and self.type == other.type


def create_bookmarks(zfm_list_output):
    return [Bookmark.fromLine(line) for line in zfm_list_output.splitlines()]


def list_bookmarks(bookmarks_file):
    output = invoke(['zfm', 'list'], bookmarks_file)
    return create_bookmarks(output)


def list_file_bookmarks(bookmarks_file):
    output = invoke(['zfm', 'list', '--files'], bookmarks_file)
    return create_bookmarks(output)


def list_directory_bookmarks(bookmarks_file):
    output = invoke(['zfm', 'list', '--dirs'], bookmarks_file)
    return create_bookmarks(output)


def test_initial_empty_bookmarks(environment):
    assert len(list_bookmarks(environment.bookmarks_file)) == 0
    assert len(list_file_bookmarks(environment.bookmarks_file)) == 0
    assert len(list_directory_bookmarks(environment.bookmarks_file)) == 0


def test_bookmark_directory(environment):
    invoke(['zfm', 'add', environment.dir_a], environment.bookmarks_file)
    assert list_bookmarks(environment.bookmarks_file) == [
        Bookmark(environment.dir_a, BookmarkType.Dir)]
    assert list_directory_bookmarks(environment.bookmarks_file) == [
        Bookmark(environment.dir_a, BookmarkType.Dir)]
    assert list_file_bookmarks(environment.bookmarks_file) == []


def test_bookmark_file(environment):
    invoke(['zfm', 'add', environment.file_a], environment.bookmarks_file)
    assert list_bookmarks(environment.bookmarks_file) == [
        Bookmark(environment.file_a, BookmarkType.File)]
    assert list_file_bookmarks(environment.bookmarks_file) == [
        Bookmark(environment.file_a, BookmarkType.File)]
    assert list_directory_bookmarks(environment.bookmarks_file) == []


def test_bookmark_multiple(environment):
    invoke(['zfm', 'add', environment.dir_a, environment.file_a],
           environment.bookmarks_file)
    invoke(['zfm', 'add', environment.dir_b], environment.bookmarks_file)
    assert list_bookmarks(environment.bookmarks_file) == [
        Bookmark(environment.dir_a, BookmarkType.Dir),
        Bookmark(environment.file_a, BookmarkType.File),
        Bookmark(environment.dir_b, BookmarkType.Dir)]
    assert list_directory_bookmarks(environment.bookmarks_file) == [
        Bookmark(environment.dir_a, BookmarkType.Dir),
        Bookmark(environment.dir_b, BookmarkType.Dir)]
    assert list_file_bookmarks(environment.bookmarks_file) == [
        Bookmark(environment.file_a, BookmarkType.File)]


def test_query(environment):
    invoke(['zfm', 'add', environment.dir_a, environment.dir_b],
           environment.bookmarks_file)
    invoke(['zfm', 'add', environment.file_a], environment.bookmarks_file)
    output = invoke(['zfm', 'query', 'dir_a'], environment.bookmarks_file)
    assert Path(output.strip()) == environment.dir_a
    output = invoke(['zfm', 'query', '--dirs', 'dir_a'],
                    environment.bookmarks_file)
    assert Path(output.strip()) == environment.dir_a
    output = invoke(['zfm', 'query', 'file_'],
                    environment.bookmarks_file)
    assert Path(output.strip()) == environment.file_a
    output = invoke(['zfm', 'query', '--files', 'file_'],
                    environment.bookmarks_file)
    assert Path(output.strip()) == environment.file_a


def test_fix(environment):
    invoke(['zfm', 'add', environment.dir_a], environment.bookmarks_file)
    assert list_bookmarks(environment.bookmarks_file) == [
        Bookmark(environment.dir_a, BookmarkType.Dir)]
    # remove directory a, it should removed from bookmarks after fix
    environment.dir_a.rmdir()
    invoke(['zfm', 'fix'], environment.bookmarks_file)
    assert list_bookmarks(environment.bookmarks_file) == []


def test_clear(environment):
    invoke(['zfm', 'add', environment.dir_a], environment.bookmarks_file)
    assert list_bookmarks(environment.bookmarks_file) == [
        Bookmark(environment.dir_a, BookmarkType.Dir)]
    invoke(['zfm', 'clear'], environment.bookmarks_file)
    assert list_bookmarks(environment.bookmarks_file) == []
