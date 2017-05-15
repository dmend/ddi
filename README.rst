DDI
===

Question 1
----------

Solution is found at ``sql/query.sql``.


Question 2
----------

Simple solution is found at ``python/simple.py``.

Prod solution is found at ``python/port_tools.py`` and
``python/test_port_tools.py``.

Running the tests requires tox:

.. code-block:: bash

    pip install tox

    tox -e py36

Running the style checker:

.. code-block:: bash

    tox -e pep8
