***************
Eventize-expect
***************

.. image:: https://pypip.in/v/eventize-expect/badge.png
        :target: https://pypi.python.org/pypi/eventize-expect


Utility to simplify use of eventize handlers "when" method by defining methods to test events attributes.

---------------------------------------------------------------------

**Table of Contents**


.. contents::
    :local:
    :depth: 1
    :backlinks: none


=============
Installation
=============

Install it from pypi::

  pip install eventize

or from sources::

  git clone git@github.com:apieum/eventize-expect.git
  cd eventize-expect
  python setup.py install

=====
Usage
=====

see: https://pypi.python.org/pypi/eventize

===========
Development
===========

Your feedback, code review, improvements or bugs, and help to document is appreciated.
You can contact me by mail: apieum [at] gmail [dot] com

Test recommended requirements::

  pip install -r dev-requirements.txt

Sometimes --spec-color doesn't function. Uninstall nosespec and nosecolor then reinstall nosecolor and nosespec separatly in this order (nosecolor first).

Launch tests::

  git clone git@github.com:apieum/eventize-expect.git
  cd eventize-expect
  nosetests --with-spec --spec-color ./eventize-expect
  # or with watch
  # nosetests --with-spec --spec-color --with-watch ./eventize-expect
