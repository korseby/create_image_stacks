# Create Image Stacks
Create script to build image stacks based on a list of XMP files containing color badges.

Version: 0.2

## Usage

```
create_image_stacks.py [-h] [-v] [-V] [-n] -x dir -d dir

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version
  -V, --verbose         be verbose and show what is being done
  -n, --dry-run         do not do anything, just show what is being done
  -x dir, --xmp_dir dir
                        directory containing the xmp files
  -d dir, --img_dir dir
                        destination image directory
```

## TODO
- check python > 3.7 requirement to be able to do: `os.makedirs(dir_name, parents=True, exist_ok=True)`
- python version in she bang

## Changes

### Version 0.2:
- iteration bugfix

### Version 0.1:
- initial release
