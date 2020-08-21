import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='classy-json',
    version='1.7.5',
    author='Iapetus-11',
    description='An attempt to recreate the way json behaves in Javascript, but in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Iapetus-11/classy-json',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
