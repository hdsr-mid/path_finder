## path_finder

### Description
An interface for finding directories and files by combining best of both worlds: glob/rglob (speed) and regex (flexibility).

### Features
path_finder officially supports Python 3.5–3.8. \
The two main features are: path_finder.DirFinder and path_finder.FileFinder (see Usage) 

### License 
[MIT][mit]

### Releases
[PyPi][pypi]

### Contributions
All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.
Issues are posted on: https://github.cFileom/hdsr-mid/path_finder/issues

[pypi]: https://pypi.org/project/path-finder/
[mit]: https://github.com/hdsr-mid/path_finder/blob/main/LICENSE.txt

#### Example FileFinder:
```
from pathlib import Path
from path_finder import FileFinder

start_dir1          = Path('start_search_from_this_dir')
start_dir2          = Path('and_start_search_from_this_dir')
limit_depth         = True
depth               = 2  # 2, so search in start_dir1, subdir and subsubdirs (same for start_dir2) 
filename_regex      = '^[0-9]{8}_blabla'
extension           = '.csv'  # choose from ('.jpg', '.png', '.txt', '.xml', '.csv', '.xlsx', '.pdf', '.h5', '.nc', '.zip')   

file_finder = FileFinder(
    multi_start_dir=[start_dir1, start_dir2],
    extension=extension,
    limit_depth=True,                   
    depth=depth,
    filename_regex=filename_regex
)
                    
paths = file_finder.paths  # returns a List[Path]
paths_empty_files = file_finder.paths_empty_file  # returns a List[Path]
```

#### Example DirFinder:
```
from pathlib import Path
from path_finder import DirFinder

dir_finder = DirFinder(
    single_start_dir=Path('start_search_from_this_dir')
    exclude_empty_dirs=True,
    limit_depth=True,
    depth=0,  # so only search in single_start_dir
)

paths = dir_finder.paths  # returns a List[Path]
paths_empty_files = dir_finder.paths_empty_file  # returns a List[Path]
```

### Test coverage
```
----------- coverage: platform win32, python 3.7.9-final-0 -----------
Name                         Stmts   Miss  Cover
------------------------------------------------
path_finder\__init__.py          2      0   100%
path_finder\base.py             47     13    72%
path_finder\dir_finder.py       65     11    83%
path_finder\file_finder.py      61      1    98%
tests\__init__.py                0      0   100%
tests\fixtures.py               41      0   100%
tests\test_dirfinder.py         28      0   100%
tests\test_filefinder.py        71      0   100%
tests\test_fixtures.py          11      0   100%
------------------------------------------------
TOTAL                          326     25    92%
```


### Conda tips
#### Build conda environment (on Windows) from any directory using environment.yml 
```
> conda env create -f <path_to_repo>/environment.yml --name <conda_env_name> python=<python_version>
> conda info --envs  # verify <conda_env_name> is in this list 
```
#### To start the application from any directory:
```
> conda activate <conda_env_name>
> (<conda_env_name>) python <path_to_repo>/main.py
```
#### Build virtual environment (on Windows) using requirement.txt
```
pip install -r <path_to_repo>/requirements.txt
```
#### Test application
```
> conda activate <conda_env_name>
> cd <path_to_repo>
> pytest 
> pytest --cov
```
#### To auto-format and check changes run:
```
> cd <path_to_repo>
> isort  # isort must be installed system wide
> black .  # black must be installed system wide
> pytest  # pytest must be installed system wide
```
#### To list all conda environments on your machine
```
conda info --envs
```
#### To build empty conda env with specific python version:
###### Without 'no--deps' conda will install a list of specified packages in the .condarc file.
###### To get the location of this conda configuration file type 'conda info'
```
> cd <does_not_matter> 
> conda create --name <conda_env_name> python=<python_version> --no-deps
```
#### To write dependencies to environment.yml:
###### By default, the YAML includes platform-specific build constraints. If you transfer across platforms (e.g. win32 to 64) omit the build info with '--no-builds':
```
> conda env export -f <path_to_repo>/environment.yml --name  <conda_env_name> --no-builds 
```
#### To write dependencies to requirements.txt
```
# first activate conda env (with pip installed), or the virtual env
pip list --format=freeze > <path_to_repo>/requirements.txt
```
#### To delete a conda env (remove env folder by hand afterwards)
```
> conda env remove --name <conda_env_name>
```
