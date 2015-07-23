# Planet Labs Stack Finder #

Find locations where there are deep stacks of imagery by clustering the location of polygons. 

## Setup ##
pip install -e .

## Tests ##
nosetests

## CLI ##
findstacks /path/to/file.geojson 

## Python ##
import from stack_finder
from src import stack_finder
