"""Setup file"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snekify",
    version="2.0.1",
    author="Tushar Sadhwani",
    author_email="tushar.sadhwani000@gmail.com",
    description="Convert text to snake case",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tusharsadhwani/snekify",
    py_modules=['snekify'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pytest'],
    entry_points={
        'console_scripts': ['snekify=snekify:main'],
    }
)
