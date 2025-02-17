[tool:pytest]
addopts = --doctest-modules --cov=./ --ignore-glob=*\VersionArchive --ignore-glob=*\Archive --ignore-glob=*\Templates --cov-report=html
#addopts = --ignore-glob=*\VersionArchive --ignore-glob=*\Archive  --cov-report=html

[flake8]
exclude = __init__.py, VersionArchive/, Archive/
max-line-length = 120
