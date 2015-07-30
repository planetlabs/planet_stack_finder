# Planet Labs Stack Finder #

Find locations where there are deep stacks of imagery by clustering the location of geojson polygons. 

Input is a list of geojson dictionaries.

Each dictionary in the list must have keys ['geometry']['coordinates'] or
['coordinates'] 

## Generic Setup ##
`pip install planet_stack_finder`

## Setup from github repo ##
`pip install -e .[test]`

## Tests ##
`pytest`

## CLI ##
```
find-stacks /path/to/file.metadata
cat path/to/file.geojson | planet search | find-stacks
``` 

## Python ##
```
from stackfinder import findstacks
```
