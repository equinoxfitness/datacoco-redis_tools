datacoco-redis_tools
=======================

.. image:: https://badge.fury.io/py/datacoco-redis-tools.svg
    :target: https://badge.fury.io/py/datacoco-redis-tools
    :alt: PyPI Version

.. image:: https://readthedocs.org/projects/datacoco-redis-tools/badge/?version=latest
    :target: http://datacoco-redis-tools.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://api.codacy.com/project/badge/Grade/63acaa6f8c1a4bd7a58722a65217407f
    :target: https://www.codacy.com/gh/equinoxfitness/datacoco-redis_tools?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=equinoxfitness/datacoco-redis_tools&amp;utm_campaign=Badge_Grade
    :alt: Code Quality Grade

.. image:: https://api.codacy.com/project/badge/Coverage/63acaa6f8c1a4bd7a58722a65217407f
    :target: https://www.codacy.com/gh/equinoxfitness/datacoco-redis_tools?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=equinoxfitness/datacoco-redis_tools&amp;utm_campaign=Badge_Coverage
    :alt: Coverage

.. image:: https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg
    :target: https://github.com/equinoxfitness/datacoco-email_tools/blob/master/CODE_OF_CONDUCT.rst
    :alt: Code of Conduct

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
        host=<HOST>,
        port=<PORT>,
        db=<DB>,
        decode_responses=True,
    )

    self.rconn.connect()
    self.rconn.set_key('key', 'key_value')

Development
-----------

Getting Started
~~~~~~~~~~~~~~~

It is recommended to use the steps below to set up a virtual environment for development:

::

    python3 -m venv <virtual env name>
    source <virtual env name>/bin/activate
    pip install -r requirements.txt

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