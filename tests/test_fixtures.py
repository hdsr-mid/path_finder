from tests.fixtures import temp_tree_structure1


# silence flake8
temp_tree_structure1 = temp_tree_structure1


def test_temp_tree_structure(temp_tree_structure1):
    """Ensure a certain dir+file structure for tests that use temp_tree_structure."""
    glob_pattern = "*.txt"
    assert len(list(temp_tree_structure1.glob(f"{glob_pattern}"))) == 1
    assert len(list(temp_tree_structure1.rglob(f"{glob_pattern}"))) == 3  # recursively
    assert len(list(temp_tree_structure1.glob(f"**/{glob_pattern}"))) == 3
    assert len(list(temp_tree_structure1.glob(f"**/**/{glob_pattern}"))) == 3  # same as above..

    glob_pattern = "*.jpg"
    assert len(list(temp_tree_structure1.glob(f"{glob_pattern}"))) == 0
    assert len(list(temp_tree_structure1.rglob(f"{glob_pattern}"))) == 2  # recursively
    assert len(list(temp_tree_structure1.glob(f"**/{glob_pattern}"))) == 2
