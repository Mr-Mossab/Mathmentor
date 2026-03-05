"""
Setup script for MathMentor library
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mathmentor",
    version="1.0.0",
    author="MOSSAB",
    author_email="arabemossab@gmail.com",
    description="Interactive Mathematics Learning Library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mathmentor/mathmentor",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
    keywords="mathematics education learning algebra geometry calculus statistics",
    project_urls={
        "Bug Reports": "https://github.com/mathmentor/mathmentor/issues",
        "Source": "https://github.com/mathmentor/mathmentor",
        "Documentation": "https://mathmentor.readthedocs.io",
    },
)
