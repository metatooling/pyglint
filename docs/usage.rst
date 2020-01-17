=====
Usage
=====

1. Install pyglint.


2. Write a linter.


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
