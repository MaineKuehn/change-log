========================
``change log`` Fragments
========================

The ``change log`` utility manages change fragments
and compiles entire changelogs if required.
Each fragment represents an individual change made
for some version of your project;
versions tie together all changes that are released together.

Changelogs are based on `keep a changelog`_ and `semantic versioning`_.

Fragments
---------

Fragments are YAML files that contain meta-data
and human-readable descriptions of individual changes.
Each fragment file contains a mapping that must contain
the fields ``category``, ``summary``, and ``description`` and optionally the fields
``pull requests`` and ``issues``; a unique naming convention of files such as
``<first PR>.<topic>.yaml`` is recommended.
Both ``summary`` and ``description`` fields are interpreted as reStructured Text.
The ``category`` should be one of
``added``, ``changed``, ``fixed``, ``deprecated``, ``removed``, or ``security``.

.. code:: YAML

    # file `4.documentation.yaml`
    # any of 'added', 'changed', 'fixed', 'deprecated', 'removed', 'security'
    category: added
    # short description of changes
    summary: "Added basic documentation on readthedocs.io"
    # pull requests of this change
    pull requests:
      - 4
    # issues solved by this change
    issues:
      - 5
    # long description of changes
    description: |
      A ``sphinx`` documentation for tool usage and code maintenance is available at
      `change-log.readthedocs.io <https://change-log.readthedocs.io/en/feature-docs/>`_.

The ``version`` is optional and in most cases does not need manual definition.
Unversioned fragments belong to the *next* release, and
specific release information is added automatically when a release is prepared.

.. _keep a changelog: https://keepachangelog.com/
.. _semantic versioning: https://semver.org
