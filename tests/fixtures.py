import pytest


@pytest.fixture
def temp_tree_structure1(tmp_path):
    """
    Creates temporary directories and files:
        maindir/
         |-- subdir1/
         |    |-- subsubdir1/
         |    |    |-- subsubdir1_file1.txt
         |    |-- subdir1_file1.txt
         |    |-- subdir1_file2.jpg
         |-- subdir2/
         |    |-- subdir2_file1.jpg
         |-- subdir3/ <-- empty!
         |-- maindir_file1.txt


    NOTE on tmp_path:
    tmp_path is a predefined fixture (=fixed name defined) in pytest, which is
    passed on to your test function if you have it as an argument name.
    We use it below to create a temporary tree structure (nested dirs + files)
    that is required for testing. It is temporary, as the created dirs and
    files (written to disk) are deleted as soon as the test finishes.
    """

    # create temp dirs
    maindir = tmp_path
    subdir1 = maindir / "subdir1"
    subdir1.mkdir()
    subdir2 = maindir / "subdir2"
    subdir2.mkdir()
    subdir3 = maindir / "subdir3"
    subdir3.mkdir()
    subsubdir1 = subdir1 / "subsubdir1"
    subsubdir1.mkdir()

    # fill temp dirs with temp files
    maindir_file1 = maindir / "maindir_file1.txt"
    maindir_file1.write_text("im a txt file")

    subdir1_file1 = subdir1 / "subdir1_file1.txt"
    subdir1_file1.write_text("im a txt file")

    subdir1_file2 = subdir1 / "subdir1_file2.jpg"
    subdir1_file2.write_text("im a jpg file")

    subdir2_file1 = subdir2 / "subdir2_file1.jpg"
    subdir2_file1.write_text("im a jpg file")

    subsubdir1_file1 = subsubdir1 / "subsubdir1_file1.txt"
    subsubdir1_file1.write_text("")  # <-- empty txt file

    return tmp_path


@pytest.fixture
def temp_tree_structure2(tmp_path):
    """Temporary dirs+files with dirnames and filenames that typically exists:
    Creates temporary directories and files:
        maindir/
         |-- 2020-08/
         |    |-- Repaired_2182_Q1_Q4/
         |    |    |-- series_201406_corrected_A.xml
         |    |-- HDSR_CAW_202004010250.xml
         |    |-- 20191030_HistTags.csv
         |-- HistTagLijst/
         |    |-- 20200722_DebietFormuleInstellingen.csv
         |-- 20200803101158_HDSR_PS0140_Waterlevel.jpg
    """
    # create temp dirs
    maindir = tmp_path
    subdir1 = maindir / "2020-08"
    subdir1.mkdir()
    subdir2 = maindir / "HistTagLijst"
    subdir2.mkdir()
    subsubdir1 = subdir1 / "Repaired_2182_Q1_Q4"
    subsubdir1.mkdir()

    # fill temp dirs with temp files
    maindir_file1 = maindir / "20200803101158_HDSR_PS0140_Waterlevel.jpg"
    maindir_file1.write_text("im a jpg file")

    subdir1_file1 = subdir1 / "HDSR_CAW_202004010250.xml"
    subdir1_file1.write_text("im a xml file")

    subdir1_file2 = subdir1 / "20191030_HistTags.csv"
    subdir1_file2.write_text("im a csv file")

    subdir2_file1 = subdir1 / "20200722_DebietFormuleInstellingen.csv"
    subdir2_file1.write_text("im a csv file")

    subsubdir1_file1 = subsubdir1 / "series_201406_corrected_A.xml"
    subsubdir1_file1.write_text("im a xml file")

    return tmp_path
