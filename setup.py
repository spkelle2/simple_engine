import setuptools
import simple_engine
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_engine",
    version=simple_engine.__version__,
    author="Sean",
    description="A Simple Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spkelle2/simple_engine",
    packages=['simple_engine', 'test_simple_engine'],
    install_requires=[
        'ticdat',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)