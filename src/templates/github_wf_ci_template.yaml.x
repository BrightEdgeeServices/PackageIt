name: CI

on: [pull_request, push, workflow_dispatch]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: true
      matrix:
        os: ["ubuntu-latest"]
        python-version: ["3.10.8"]

    steps:
      - name: Checkout source
        uses: actions/checkout@v4

      - name: Setup python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          architecture: x64

      - name: Install
        run: |
          pip install -e .
          pip install -r requirements_test.txt

      - name: Run tests
        run: pytest

      - name: "Upload coverage to Codecov"
        uses: codecov/codecov-action@v5
