# path_finder
An interface for finding directories and files by combining best of both worlds: glob/rglob (speed) and regex (flexibility)


Example DirFinder:
```
from pathlib import Path
import path_finder

single_start_dir    = pathlib.Path('this_is_my_start_dir')
limit_depth         = True
depth               = 2  # <-- 2, so search in start_dir, subdir and subsubdirs
filename_regex      = '^[0-9]{8}_blabla'
extension           = '.csv'  <-- choose from ('.jpg', '.png', '.txt', '.xml', '.csv', '.xlsx', '.pdf', '.h5', '.nc', '.zip')   

file_finder = path_finder.FileFinder(
    single_start_dir=single_start_dir,
    extension=extension,
    limit_depth=True,                   
    depth=depth,
    filename_regex=filename_regex
)
                    
paths = file_finder.paths
paths_empty_files = file_finder.paths_empty_file
```


Example FileFinder:
```
from pathlib import Path
import path_finder

dir_finder = DirFinder(
    single_start_dir=single_start_di,
    exclude_empty_dirs=True,
    limit_depth=True,
    depth=0,
)

               
paths = file_finder.paths
paths_empty_files = file_finder.paths_empty_file
```

