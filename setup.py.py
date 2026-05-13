from setuptools import setup, find_packages

setup(
    name='my_grep',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'mygrep = bin.cli:show_results',
        ],
    },
)