from path_finder.file_finder import FileFinder
from tests.fixtures import temp_tree_structure1
from tests.fixtures import temp_tree_structure2

import pytest
import re


def test_file_finder_no_depth_limit(temp_tree_structure1):
    file_finder = FileFinder(
        single_start_dir=temp_tree_structure1, extension=".txt", limit_depth=False
    )
    assert len(file_finder.paths) == 3

    file_finder = FileFinder(
        single_start_dir=temp_tree_structure1, extension=".jpg", limit_depth=False
    )
    assert len(file_finder.paths) == 2

    file_finder = FileFinder(
        single_start_dir=temp_tree_structure1, extension=".png", limit_depth=False
    )
    assert len(file_finder.paths) == 0


def test_file_finder_empty_files(temp_tree_structure1):
    file_finder = FileFinder(
        single_start_dir=temp_tree_structure1, extension=".txt", limit_depth=False
    )
    assert len(file_finder.paths) == 3
    assert len(file_finder.paths_empty_file) == 1
    assert file_finder.paths_empty_file[0].name == "subsubdir1_file1.txt"


def test_file_finder_depth_0(temp_tree_structure1):
    """ Limit the search to single_start_dir (no subdirectories). """
    file_finder = FileFinder(
        single_start_dir=temp_tree_structure1,
        extension=".txt",
        limit_depth=True,
        depth=0,
    )
    assert len(file_finder.paths) == 1
    assert file_finder.paths[0].name == "maindir_file1.txt"

    file_finder = FileFinder(
        single_start_dir=temp_tree_structure1,
        extension=".jpg",
        limit_depth=True,
        depth=0,
    )
    assert len(file_finder.paths) == 0


def test_file_finder_depth_1(temp_tree_structure1):
    """ Limit the search to single_start_dir and its subdirs"""
    file_finder = FileFinder(
        single_start_dir=temp_tree_structure1,
        extension=".txt",
        limit_depth=True,
        depth=1,
    )
    assert len(file_finder.paths) == 2
    assert sorted([x.name for x in file_finder.paths]) == [
        "maindir_file1.txt",
        "subdir1_file1.txt",
    ]

    file_finder = FileFinder(
        single_start_dir=temp_tree_structure1,
        extension=".jpg",
        limit_depth=True,
        depth=1,
    )
    assert len(file_finder.paths) == 2
    assert sorted([x.name for x in file_finder.paths]) == [
        "subdir1_file2.jpg",
        "subdir2_file1.jpg",
    ]


def test_file_finder_multi_start_dir(temp_tree_structure1):
    dir_path1 = sorted([x for x in temp_tree_structure1.iterdir() if x.is_dir()])[0]
    dir_path2 = sorted([x for x in temp_tree_structure1.iterdir() if x.is_dir()])[1]
    assert dir_path1.stem == "subdir1"
    assert dir_path2.stem == "subdir2"
    file_finder = FileFinder(
        multi_start_dir=[dir_path1, dir_path2],
        extension=".txt",
        depth=1,
        limit_depth=True,
    )
    assert sorted([x.stem for x in file_finder.paths]) == [
        "subdir1_file1",
        "subsubdir1_file1",
    ]


def test_file_finder_wrong_setup(temp_tree_structure1):

    # limit_depth=True requires also depth argument
    with pytest.raises(AssertionError) as err:
        FileFinder(
            single_start_dir=temp_tree_structure1,
            extension=".txt",
            limit_depth=True,
            depth=None,
        )
    assert err.value.args[0] == "depth None must be a int and in range: 0 <= depth <= 6"

    # wrong format extension
    with pytest.raises(AssertionError) as err:
        extension = "txt"
        FileFinder(single_start_dir=temp_tree_structure1, extension=extension)
    assert (
        err.value.args[0]
        == f"extension {extension} must either be None or a str in {FileFinder.EXTENTION_CHOICES}"
    )

    # unknown extension
    with pytest.raises(AssertionError) as err:
        extension = ".tar"
        FileFinder(single_start_dir=temp_tree_structure1, extension=extension)
    assert (
        err.value.args[0]
        == f"extension {extension} must either be None or a str in {FileFinder.EXTENTION_CHOICES}"
    )

    # single_start_dir must be a pathlib.Path
    with pytest.raises(AssertionError) as err:
        FileFinder(single_start_dir="test", extension=".txt")
    assert err.value.args[0] == "single_start_dir must be a pathlib.Path"

    # depth provided without limit_depth=True
    with pytest.raises(AssertionError) as err:
        FileFinder(
            single_start_dir=temp_tree_structure1,
            extension=".txt",
            limit_depth=False,
            depth=4,
        )
    assert err.value.args[0] == "depth=4 is only possible with limit_depth=True"

    # filename_regex should be a string, not e.g. a re.Pattern
    with pytest.raises(AssertionError) as err:
        FileFinder(
            single_start_dir=temp_tree_structure1,
            extension=".txt",
            filename_regex=re.compile("abc"),
        )
    assert err.value.args[0] == "filename_regex must be a str"

    # both single_start_dir and multi_start_dir is not possible
    with pytest.raises(AssertionError) as err:
        FileFinder(
            single_start_dir=temp_tree_structure1,
            multi_start_dir=temp_tree_structure1,
            extension=".txt",
        )
    assert err.value.args[0] == "use either single_start_dir or multi_start_dir"


def test_filefinder_caw_histtags(temp_tree_structure2):
    file_finder = FileFinder(
        single_start_dir=temp_tree_structure2,
        extension=".csv",
        filename_regex="^[0-9]{8}_HistTags$",
        limit_depth=False,
    )
    paths = file_finder.paths
    assert len(paths) == 1
    assert paths[0].name == "20191030_HistTags.csv"


def test_filefinder_caw_debietinstellingen(temp_tree_structure2):
    file_finder = FileFinder(
        single_start_dir=temp_tree_structure2,
        extension=".csv",
        filename_regex="^[0-9]{8}_DebietFormuleInstellingen$",
        limit_depth=True,
        depth=1,
    )
    paths = file_finder.paths
    assert len(paths) == 1
    assert paths[0].name == "20200722_DebietFormuleInstellingen.csv"
