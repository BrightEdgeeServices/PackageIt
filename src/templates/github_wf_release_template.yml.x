name: Distribute to PyPI

on: [push, pull_request]

jobs:
  ReleaseToPyPi:
    runs-on: "ubuntu-latest"

    steps:
      - name: Checkout source
        uses: actions/checkout@v4

      - name: Set up Python 3.9
        uses: actions/setup-python@v5
        with:
          python-version: 3.9

      - name: Install build dependencies
        run: python -m pip install build wheel

      - name: Build distributions
        shell: bash -l {0}
        run: python -m build

      - name: Publish package to PyPI
        if: github.repository == 'hendrikdutoit/PackageIt' && github.event_name == 'push' && startsWith(github.ref, 'refs/tags')
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: __token__
          password: ${1}{1} secrets.{3} {2}{2}
          repository_url: {4}
          verbose: true
