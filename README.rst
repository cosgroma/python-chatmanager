========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |github-actions| |codecov|
    * - package
      - |commits-since|

.. |github-actions| image:: https://github.com/cosgroma/python-chatmanager/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/cosgroma/python-chatmanager/actions

.. |codecov| image:: https://codecov.io/gh/cosgroma/python-chatmanager/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/cosgroma/python-chatmanager

.. |commits-since| image:: https://img.shields.io/github/commits-since/cosgroma/python-chatmanager/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/cosgroma/python-chatmanager/compare/v0.0.0...main



.. end-badges

Manages conversations from large language models

* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Installation
============

::

    pip install chatmanager

You can also install the in-development version with::

    pip install https://github.com/cosgroma/python-chatmanager/archive/main.zip


Documentation
=============


To use the project:

.. code-block:: python

    import chatmanager
    chatmanager.compute(...)



Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
