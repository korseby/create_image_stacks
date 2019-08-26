# Create Image Stacks
Create script to build image stacks based on a list of XMP files containing color badges.

Version: 0.3

## Usage

```
usage: create_image_stacks.py [-h] [-v] [-V] [-n] [-c] -x dir -d dir [-f]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version
  -V, --verbose         be verbose and show what is being done
  -n, --dry-run         do not do anything, just show what is being done
  -c, --create_dirs_only
                        only create output directories and do not move
                        destination images
  -x dir, --xmp_dir dir
                        directory containing the xmp files
  -d dir, --img_dir dir
                        destination image directory
  -f, --force           force action and do not exit when image file(s) do not
                        exist
```

## TODO
- python version in she bang

## Changes

### Version 0.3:
- added force option
- added create dirs only option

### Version 0.2:
- iteration bugfix

### Version 0.1:
- initial release
