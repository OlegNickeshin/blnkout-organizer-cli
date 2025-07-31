from setuptools import setup, find_packages

setup(
    name='blnkout-organizer-cli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'blnk-org=cli.blnk_org:main',
        ],
    },
    author='Oleg (blnkout)',
    description='A CLI tool for organizing files by extension, size, date, and more.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
)
