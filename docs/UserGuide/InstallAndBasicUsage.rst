Install and Basic Usage
=======================

PyPI Install
^^^^^^^^^^^^

.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.

You can also install directly from PyPI using:
.. code-block:: bash
   $ pip install ezhost


Starting ezhost
^^^^^^^^^^^^

As described above, to run Ganga simply execute ``ezhost`` (for PyPI install)

This code can be accessed using the help system:
.. code-block:: python
        $ ezhost -h


This code is a basic usage of ezhost:
.. code-block:: python
        $ ezhost -s lamp -H 127.0.0.1:2201 -U vagrant -P vagrant

