from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author='Christopher Bell',
    author_email='Chris.E.Bell24@gmail.com',
    maintainer='Christopher Bell',
    maintainer_email='Chris.E.Bell24@gmail.com',
    url='https://github.com/chrisebell24/sklearn_linear_model_modification',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    name='sklearn_linear_model_modification',
    version='0.0.1',
    description='Wraps sklearn linear_model regression functions to allow Drop1, Add1, and VIF calculations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['linear_model'],
    package_dir={'': 'src'},
    install_requires = [
        "numpy>=1.16.1",
        "pandas>=1.0.0",
        "sklearn>=0.22.0",
        "statsmodels>=0.12.0",
    ],
    extras_require = {
        "dev": [
            "pytest >= 3.7",
        ],
    },
)