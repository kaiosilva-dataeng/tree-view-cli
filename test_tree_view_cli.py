import pytest
import tempfile
import os
from pathlib import Path
from tree_view_cli import DirectoryTreeGenerator

@pytest.fixture
def temp_directory():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield Path(tmpdirname)

def create_file_structure(root):
    (root / "dir1" / "subdir1").mkdir(parents=True)
    (root / "dir1" / "subdir2").mkdir(parents=True)
    (root / "dir1" / "file1.txt").touch()
    (root / "dir1" / "subdir1" / "file2.txt").touch()
    (root / "dir1" / "subdir2" / "file3.txt").touch()

def test_basic_structure(temp_directory, capsys):
    create_file_structure(temp_directory)
    tree_gen = DirectoryTreeGenerator(temp_directory)
    tree_gen.generate_tree()
    captured = capsys.readouterr()
    assert "dir1" in captured.out
    assert "subdir1" in captured.out
    assert "subdir2" in captured.out
    assert "file1.txt" in captured.out
    assert "file2.txt" in captured.out
    assert "file3.txt" in captured.out

def test_max_depth(temp_directory, capsys):
    create_file_structure(temp_directory)
    tree_gen = DirectoryTreeGenerator(temp_directory, max_depth=1)
    tree_gen.generate_tree()
    captured = capsys.readouterr()
    assert "dir1" in captured.out
    assert "subdir1" not in captured.out
    assert "file2.txt" not in captured.out

def test_gitignore_file(temp_directory, capsys):
    create_file_structure(temp_directory)
    with open(temp_directory / ".gitignore", "w") as f:
        f.write("**/file1.txt\n")
    tree_gen = DirectoryTreeGenerator(temp_directory)
    tree_gen.generate_tree()
    captured = capsys.readouterr()
    assert "file1.txt" not in captured.out
    assert "file2.txt" in captured.out

def test_gitignore_directory(temp_directory, capsys):
    create_file_structure(temp_directory)
    with open(temp_directory / ".gitignore", "w") as f:
        f.write("dir1/\n")
    tree_gen = DirectoryTreeGenerator(temp_directory)
    tree_gen.generate_tree()
    captured = capsys.readouterr()
    assert "dir1" not in captured.out

def test_gitignore_subdirectory(temp_directory, capsys):
    create_file_structure(temp_directory)
    with open(temp_directory / ".gitignore", "w") as f:
        f.write("**/subdir1\n")
    tree_gen = DirectoryTreeGenerator(temp_directory)
    tree_gen.generate_tree()
    captured = capsys.readouterr()
    assert "subdir1" not in captured.out
    assert "subdir2" in captured.out

# def test_cyclic_reference(temp_directory, capsys):
#     (temp_directory / "dir1" / "subdir1").mkdir(parents=True)
#     os.symlink(temp_directory / "dir1", temp_directory / "dir1" / "subdir1" / "cycle")
#     tree_gen = DirectoryTreeGenerator(temp_directory)
#     tree_gen.generate_tree()
#     captured = capsys.readouterr()
#     assert "Cyclic reference to" in captured.out

def test_empty_directory(temp_directory, capsys):
    tree_gen = DirectoryTreeGenerator(temp_directory)
    tree_gen.generate_tree()
    captured = capsys.readouterr()
    assert captured.out.strip() == temp_directory.name + "/"

def test_git_directory_excluded(temp_directory, capsys):
    create_file_structure(temp_directory)
    (temp_directory / ".git").mkdir()
    tree_gen = DirectoryTreeGenerator(temp_directory)
    tree_gen.generate_tree()
    captured = capsys.readouterr()
    assert "dir1" in captured.out
    assert ".git" not in captured.out