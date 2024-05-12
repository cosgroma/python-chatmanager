#!/usr/bin/env python
import re
from pathlib import Path

from setuptools import find_packages
from setuptools import setup

# from setuptools.dist import Distribution


# class BinaryDistribution(Distribution):
#     """
#     Distribution which almost always forces a binary package with platform name
#     """

#     def has_ext_modules(self):
#         return super().has_ext_modules() or not os.environ.get("SETUPPY_ALLOW_PURE")


def read(*names, **kwargs):
    with Path(__file__).parent.joinpath(*names).open(encoding=kwargs.get("encoding", "utf8")) as fh:
        return fh.read()


def get_requirements(filename="requirements.txt"):
    with Path.open(filename) as f:
        requires = [line.replace("\n", "") for line in f.readlines()]
    return requires


setup(
    name="chatmanager",
    # use_scm_version={
    #     "local_scheme": "dirty-tag",
    #     "write_to": "src/chatmanager/_version.py",
    #     "fallback_version": "0.0.0",
    # },
    version="0.0.0",
    license="LGPL-3.0-or-later",
    description="Manages conversations from large language models",
    long_description="{}\n{}".format(
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub("", read("README.rst")),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst")),
    ),
    author="Mathew Cosgrove",
    author_email="cosgroma@gmail.com",
    url="https://github.com/cosgroma/python-chatmanager",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[path.stem for path in Path("src").glob("*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)" "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        # uncomment if you test on these interpreters:
        # "Programming Language :: Python :: Implementation :: IronPython",
        # "Programming Language :: Python :: Implementation :: Jython",
        # "Programming Language :: Python :: Implementation :: Stackless",
        "Topic :: Utilities",
        "Private :: Do Not Upload",
    ],
    project_urls={
        "Changelog": "https://github.com/cosgroma/python-chatmanager/blob/master/CHANGELOG.rst",
        "Issue Tracker": "https://github.com/cosgroma/python-chatmanager/issues",
    },
    keywords=[
        # eg: "keyword1", "keyword2", "keyword3",
    ],
    python_requires=">=3.11",
    install_requires=get_requirements(),
    extras_require={
        # eg:
        #   "rst": ["docutils>=0.11"],
        #   ":python_version=='3.8'": ["backports.zoneinfo"],
    },
    # We only require CFFI when compiling.
    # pyproject.toml does not support requirements only for some build actions,
    # but we can do it in setup.py.
    setup_requires=(
        [
            # "setuptools_scm>=3.3.1",
            # "cffi>=1.0.0",
        ]
        # if any(arg.startswith(("build", "bdist")) for arg in sys.argv)
        # else [
        #     "setuptools_scm>=3.3.1",
        # ]
    ),
    entry_points={
        "console_scripts": [
            "chatman = chatmanager.cli:run",
        ]
    },
    # cffi_modules=[f"{path}:ffi" for path in Path("src").glob("**/_*_build.py")],
)
