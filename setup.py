from setuptools import setup
from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='naniapi',
    version='2.0.0',
    author='Kimberly',
    author_email='kimberly@error44.tech',
    license='MIT',
    description='Simple API requests with many output customizations, access to over 1k images with a token-protected system.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "aiohttp >= 3.6"
    ],
    url='https://github.com/Kimii55/Nani-Python',
    py_modules=['naniapi'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
