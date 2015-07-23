"""cli interface for stack finding
"""
import click
from stack_finder import find_stacks
import json

import pprint


@click.command("findstacks")
@click.argument('metadata', default='-', required=False, nargs=1)
@click.option('--index', default=0, help='zero indexed stack number')
@click.pass_context
def findstacks(ctx, metadata, index):
    """
    find the deepest stack in a set of images
    example run: cat tests/polygon.geojson | planet search | findstacks
    """
    if metadata == '-':
        src = click.open_file('-')

        if not src.isatty():
            data = src.read()
        else:
            click.echo(ctx.get_usage())
            ctx.exit(1)
    else:
        with open(metadata, 'r') as src:
            data = src.read()

    geojson = json.loads(data)

    scenes_md = []
    for i in geojson['features']:
        scenes_md.append(i)

    stacks, stack_centers = find_stacks(scenes_md, min_depth=2, max_sep_km=2)

    if len(stacks) < index+1:
        click.echo("No Stack of that index")

    # create a feature collection from the stacks
    FC = {
        "type": "FeatureCollection",
        "features": stacks[index]
    }

    click.echo(json.dumps(FC))
