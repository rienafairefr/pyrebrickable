pyrebrickable data documentation
================================

Installation
------------

As part of pyrebrickable

    pip install pyrebrickable

Download and Import
-------------------

Before anything, you need to download and import the database CSV dumps into your own local database
The local database will be created in your user data directory (somewhere in ```~/.local/share```, or %APPDATA% for Windows)
The database dumps will be saved there as well. Use:

.. code-block:: bash

    rebrickable data download
    rebrickable data import

This can take some time (a few minutes)

Usage
-----

After you have downloaded and imported the data, you can use the data through the SQLAlchemy interface:

.. code-block:: python

    from rebrickable.data.database import Session
    from rebrickable.data.models import Part

    # all the parts
    Session.query(Part).all()

etc.



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
