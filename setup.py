# setup.py
from setuptools import setup

setup(
    name='feebo',
    version='0.1',
    py_modules=['feebo'],
    entry_points={
        'console_scripts': [
            'feebo = feebo:main',
        ],
    },
    install_requires=[
        # List your project's dependencies here, if any
    ],
    description='Feebo Command Line Tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/feebo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
