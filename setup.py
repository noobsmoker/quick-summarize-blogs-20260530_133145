from setuptools import setup, find_packages

setup(
    name="quick-summarize-blogs-20260530_133145",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'quick=quick:main',
        ],
    },
)
