import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Classy-Json',
    version='1.2.3',
    author='Iapetus-11',
    description='An attempt to recreate the way json behaves in Javascript, but in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Iapetus-11/Classy-Json',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
