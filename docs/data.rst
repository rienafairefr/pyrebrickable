pyrebrickable_data documentation
================================

Installation
------------

As part of pyrebrickable

    pip install pyrebrickable

Or standalone

    pip install pyrebrickable-data


Download and Import
-------------------

Before anything, you need to download and import the database CSV dumps into your own local database
The local database will be created in your user data directory (somewhere in ~/.local/share, or %APPDATA% for Windows)
The database dumps will be saved there as well. Use:

    python -m rebrickable_data.download
    python -m rebrickable_data.import

This can take some time (a few minutes)

Usage
-----

After you have downloaded and imported the data, you can use the data through the SQLAlchemy interface:

    from rebrickable_data.database import Session
    from rebrickable_data.models import Part

    # all the parts
    Session.query(Part).all()

etc.



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
