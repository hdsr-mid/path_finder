from path_finder.dir_finder import DirFinder
from tests.fixtures import temp_tree_structure1
from tests.fixtures import temp_tree_structure2


# silence flake8
temp_tree_structure1 = temp_tree_structure1
temp_tree_structure2 = temp_tree_structure2


def test_dirfinder_no_limit_depth(temp_tree_structure1):
    dir_finder = DirFinder(single_start_dir=temp_tree_structure1, limit_depth=False)
    paths = dir_finder.paths
    assert len(paths) == 4
    assert sorted([x.stem for x in paths]) == [
        "subdir1",
        "subdir2",
        "subdir3",
        "subsubdir1",
    ]


def test_dirfinder_depth_0(temp_tree_structure1):
    dir_finder = DirFinder(single_start_dir=temp_tree_structure1, limit_depth=True, depth=0)
    paths = dir_finder.paths
    assert len(paths) == 3
    assert sorted([x.stem for x in paths]) == ["subdir1", "subdir2", "subdir3"]


def test_dirfinder_exclude_empty_dirs(temp_tree_structure1):
    dir_finder = DirFinder(single_start_dir=temp_tree_structure1, exclude_empty_dirs=True, limit_depth=False,)
    assert sorted([x.stem for x in dir_finder.paths]) == [
        "subdir1",
        "subdir2",
        "subsubdir1",
    ]

    assert dir_finder.paths_empty_dir == []  # all empty dirs were skipped during search

    dir_finder = DirFinder(single_start_dir=temp_tree_structure1, exclude_empty_dirs=False, limit_depth=False,)
    assert len(dir_finder.paths_empty_dir) == 1
    assert dir_finder.paths_empty_dir[0].stem == "subdir3"


def test_dirfinder_exclude_empty_dirs_depth_0(temp_tree_structure1):
    dir_finder = DirFinder(single_start_dir=temp_tree_structure1, exclude_empty_dirs=True, limit_depth=True, depth=0,)
    assert sorted([x.stem for x in dir_finder.paths]) == ["subdir1", "subdir2"]


def test_dirfinder_typical_dirs(temp_tree_structure2):
    dir_finder = DirFinder(
        single_start_dir=temp_tree_structure2, limit_depth=True, depth=2, dirname_regex="^[0-9]{4}-[0-9]{2}$",
    )
    paths = dir_finder.paths
    assert len(paths) == 1
    assert paths[0].stem == "2020-08"
