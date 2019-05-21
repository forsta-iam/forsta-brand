import os.path
import re
import setuptools

with open('README.md') as f:
    long_description = f.read()

with open(os.path.join('forsta_brand', '__init__.py')) as f:
    version = re.search(
        r'''^__version__\s*=\s*(['"])(.*)\1''', f.read(), re.MULTILINE
    ).group(2)

setuptools.setup(
    name='forsta-brand',
    version=version,
    author='Alexander Dutton',
    author_email='forsta@alexdutton.co.uk',
    description='A default brand for the Forstå ecosystem',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/forsta-iam/forsta-brand",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django :: 2.2",
        "Topic :: Internet :: WWW/HTTP",
    ],
    install_requires=[
    ],
    extra_require={
    },
)
