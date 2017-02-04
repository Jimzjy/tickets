from setuptools import setup

setup(
    name='tickets',
    version="0.10",
    description="Get tickets info via 12306",
    author="Jimzjy",
    url="https://github.com/Jimzjy",
    py_modules=['tickets', 'stations'],
    install_requires=['requests', 'docopt', 'prettytable', 'colorama'],
    entry_points={
        'console_scripts': ['tickets=tickets:cli']
    }
)