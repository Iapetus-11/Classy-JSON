import setuptools  # import order matters here wth

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="classy-json-cython",
    version="1.0.4",
    author="Iapetus-11",
    description="Dot access for Python dictionaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Iapetus-11/classy-json",
    setup_requires=["cython"],
    packages=setuptools.find_packages(),
    ext_modules=[
        setuptools.Extension('classyjson.types', sources=['classyjson/types.pyx'])
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
