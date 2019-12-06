datacoco-redis_tools
=======================

.. image:: https://img.shields.io/pypi/v/datacoco-redis_tools.svg
   :target: https://pypi.python.org/pypi/datacoco-redis_tools
   :alt: Pypi Version
.. image:: https://travis-ci.org/readthedocs/datacoco-redis_tools.svg?branch=master
   :target: https://travis-ci.org/readthedocs/datacoco-redis_tools
   :alt: Build Status
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
  :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

datacoco-redis_tools provides basic interaction to redis database

Installation
------------

datacoco-redis_tools requires Python 3.6+

::

    python3 -m venv <virtual env name>
    source <virtual env name>/bin/activate
    pip install datacoco-redis_tools


Quickstart
----------

::

    self.rconn = RedisInteraction(
        host=AWS_ACCESS_KEY,
        port=AWS_SECRET_KEY,
        db=SENDER,
        decode_responses=True,
    )

    self.rconn.connect()
    self.rconn.set_key('key', 'key_value')


Testing
~~~~~~~

::

    pip install -r requirements-dev.txt

To run the testing suite, simply run the command: ``tox`` or ``python -m unittest discover tests``


Contributing
------------

Contributions to datacoco-redis\_tools are welcome!

Please reference guidelines to help with setting up your development
environment
`here <https://github.com/equinoxfitness/datacoco-redis_tools/blob/master/CONTRIBUTING.rst>`__.