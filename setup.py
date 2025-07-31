from setuptools import setup, find_packages

setup(
    name='WebSecScanner',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple CLI tool to scan websites for basic security vulnerabilities.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)