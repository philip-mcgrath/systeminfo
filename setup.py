from setuptools import setup

setup(
    name='systeminfo',
    version='0.1',
    packages=['systeminfo'],
    url='',
    license='GPL3',
    author='Philip McGrath',
    author_email='philip.mc-grath@ucdconnect.ie',
    description='Basic system information for COMP30670',
    entry_points={'console_scripts': ['comp30670_systeminfo=systeminfo.main:main']}
)
