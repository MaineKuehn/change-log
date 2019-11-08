``change log`` Fragments
------------------------

Fragments are YAML files that contain meta-data
and human-readable descriptions of individual changes.
Each fragment file contains a mappings that must contain
the fields ``category``, ``summary``, and ``description`` and optionally the fields
``pull requests`` and ``issues``; a unique naming convention of files such as
``<first PR>.<topic>.yaml`` is recommended.
Both ``summary`` and ``description`` fields are interpreted as reStructured Text.

.. code:: YAML

    # file `39.line_format.fixes.yaml`
    # any of 'added', 'changed', 'fixed', 'deprecated', 'removed', 'security'
    category: fixed
    # short description of changes
    summary: "fixed Line Protocol sending illegal content"
    # pull requests of this change
    pull requests:
      - 39
      - 44
    # issues solved by this change
    issues:
      - 42
    # long description of changes
    description: |
      The Line Protocol implementation has been extended to remove cases that
      previously led to illegal output. ``None`` values are
      forbidden, and strings are escaped in field values, tags, and measurements.

The ``version`` is optional and in most cases does not need manual definitions.
Unversioned fragments belong to the "next" release, and
specific release information is added automatically when a release is prepared.
