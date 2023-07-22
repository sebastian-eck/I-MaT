import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    include_package_data=True,
    name='imat',
    version='3.0',
    author='Sebastian Oliver Eck',
    url="https://github.com/sebastian-eck/I-MaT",
    description='Interactive Music Analysis Tool (I-MaT)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'iMaT = iMaT.__main__:main'
        ]
    },
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
        "numpy~=1.23.5",
        "matplotlib~=3.7.1",
        "pandas~=2.0.2",
        "music21~=8.3.0",
        "miditok~=2.0.6",
        "tokenizers~=0.13.3",
        "requests~=2.31.0",
        "openpyxl~=3.1.2",
        "tqdm~=4.65.0",
        "seaborn~=0.12.2",
        "scipy~=1.10.1"

    ],
    extras_require={
        "doc": ["sphinx~=7.0.0",
                "sphinxcontrib-napoleon~=0.7",
                "sphinx-autobuild",
                "myst_parser",
                "sphinx_rtd_theme"]
    }
)
