from setuptools import setup

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='conf',
      version='0.4.0',
      author='Ramon Hagenaars',
      author_email='ramon.hagenaars@gmail.com',
      description='Facilitates a convenient use of configuration files',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      url='https://github.com/ramonhagenaars/conf',
      test_suite='tests',
      packages=[
          'conf',
          'conf.parsers',
      ],
      extras_require={
          'yaml': ['PyYAML>=5.1'],
      },
      tests_require=[
          'PyYAML>=5.1',
      ],
      zip_safe=False,
      classifiers=(
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent'))
