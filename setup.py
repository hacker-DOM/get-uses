import setuptools

LICENSE = "ISC"
NAME = "get_uses"
VERSION = "1.0.0"
README = "README.adoc"
AUTHOR = "Dominik Teiml"
PYTHON_REQUIRES = ">=3.7"
DESCRIPTION = "Annotate your Python codebase with uses."

DIR = NAME

extras_require = dict(
    tests=[
        "pytest >= 6.2.5, < 7.0.0",
    ]
)

packages = [
    f"{DIR}." + some_dir
    for some_dir in setuptools.find_namespace_packages(DIR)
    if "tests" not in some_dir.split(".")
] + [DIR]

entry_points = dict(console_scripts=[f"{NAME} = {DIR}.__main__:main"])

with open(README) as f:
    long_description = f.read()

setuptools.setup(
    name=NAME,
    author=AUTHOR,
    version=VERSION,
    license=LICENSE,
    packages=packages,
    description=DESCRIPTION,
    entry_points=entry_points,
    extras_require=extras_require,
    python_requires=PYTHON_REQUIRES,
    long_description=long_description,
)
