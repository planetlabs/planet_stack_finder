from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='planet_stack_finder',
      version='0.0.1',
      description=u"Find local clusters from geojson.",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Josh Tennefoss",
      author_email='jt@planet.com',
      url='https://github.com/planetlabs/planet_stack_finder',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'numpy',
          'sklearn',
          'scipy'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      findstacks=stackfinder.cli:findstacks
      """
      )
