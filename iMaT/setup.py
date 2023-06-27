from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='iMaT',
    version='0.0.1',
    author='Sebastian Oliver Eck',
    url="https://github.com/sebastian-eck/I-MaT",
    description='Interactive Music Analysis Tool (I-MaT)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    readme='README.md',
    py_modules=['iMaT'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Matplotlib",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
        "Topic :: Text Processing :: Linguistic",
    ],
    install_requires=[
        "numpy==1.23.5",
        "matplotlib~=3.7.1",
        "pandas~=2.0.2",
        "ipython~=8.14.0",
        "scipy~=1.10.1",
        "music21==8.3.0",
        "miditok~=2.0.6",
        "miditoolkit~=0.1.16",
        "tokenizers",
        "lorem-text",
        "requests~=2.31.0",
        "openpyxl~=3.1.2",
        "tqdm~=4.65.0"
    ],
    extras_require={
        "doc": ["sphinx~=7.0.1"]
    }
)
