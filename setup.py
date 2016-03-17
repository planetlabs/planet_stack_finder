from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='stackfinder',
      version='0.0.12',
      description=u"Find local clusters from geojson.",
      long_description=long_description,
      classifiers=[],
      keywords=['stack_finder', 'planet', 'planet labs', 'overlaps'],
      author=u"Josh Tennefoss",
      author_email='jt@planet.com',
      url='https://github.com/planetlabs/planet_stack_finder',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click>=4.1',
          'numpy>=1.9.2',
          'scikit-learn>=0.16.1',
          'scipy>=0.16.0'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      find-stacks=stackfinder.cli:find_stacks
      """
      )
