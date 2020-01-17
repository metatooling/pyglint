=====
Usage
=====

.. currentmodule:: pyglint

1. Install pyglint.


2. Write a linter.

A checker takes a node and yields :class:`Problem` objects.

.. autoclass:: Problem
   :members:


There are two ways to write a check.

   #. Define a :class:`Problem` beforehand with :meth:`CheckerGroup.problem()` and reference it with :meth:`CheckerGroup.check_for_problems()`.

   #. Define a :class:`Problem` on the fly for a single function with :meth:`CheckerGroup.standalone_check()`.

.. autoclass:: CheckerGroup
   :members:


.. literalinclude:: ../examples/mylinter.py
   :language: python


3. Register it with Pylint.

.. code-block:: python

    def register(linter):
        """Register checkers."""
        checker = pyglint.make_pylint_checker(chk)
        linter.register_checker(checker(linter))

4. Run Pylint with it. ::

    python -m pylint --load-plugins examples.mylinter examples/to-be-linted.py


Or enable it in your Pylint configuration file. ::


    # .pylintrc
    load-plugins=examples.mylinter
