======
reiter
======

Wrapper for Python iterators and iterables that implements a list-like random-access interface by caching retrieved items for later reuse.

|pypi|

.. |pypi| image:: https://badge.fury.io/py/reiter.svg
   :target: https://badge.fury.io/py/reiter
   :alt: PyPI version and link.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install reiter

The library can be imported in the usual way::

    import reiter
    from reiter import reiter

Testing and Conventions
-----------------------
Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint reiter

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
