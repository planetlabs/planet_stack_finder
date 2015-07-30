"""cli interface for stack finding
"""
import click
from stackfinder import findstacks
import json


@click.command("find-stacks")
@click.argument('metadata', default='-', required=False, nargs=1)
@click.option('--index', default=0, help='zero indexed stack number ordered by decreasing number of objects in cluster')
@click.pass_context
def find_stacks(ctx, metadata, index):
    """
    Input is a list of geojson dictionaries.

    Each dictionary in the list must have keys ['geometry']['coordinates'] or
    ['coordinates']

    e.g. find the deepest stack in a set of planet labs images
    cat path/to/file.geojson | planet search | find-stacks
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

    stacks, stack_centers = findstacks(scenes_md, min_depth=2, max_sep_km=2)

    if len(stacks) < index+1:
        click.echo("No Stack of that index")

    # create a feature collection from the stacks
    FC = {
        "type": "FeatureCollection",
        "features": stacks[index]
    }

    click.echo(json.dumps(FC))
