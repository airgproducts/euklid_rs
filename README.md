# Euklid_rs [2D and 3D vector operations]

[![maturin](https://github.com/airgproducts/euklid_rs/actions/workflows/maturin.yml/badge.svg?branch=main)](https://github.com/airgproducts/euklid_rs/actions/workflows/maturin.yml)
[![rsaudit](https://github.com/airgproducts/euklid_rs/actions/workflows/rsaudit.yml/badge.svg?branch=main)](https://github.com/airgproducts/euklid_rs/actions/workflows/rsaudit.yml)
[![rsfmt](https://github.com/airgproducts/euklid_rs/actions/workflows/rsformat.yml/badge.svg?branch=main)](https://github.com/airgproducts/euklid_rs/actions/workflows/rsformat.yml)
[![rstest](https://github.com/airgproducts/euklid_rs/actions/workflows/rstest.yml/badge.svg?branch=main)](https://github.com/airgproducts/euklid_rs/actions/workflows/rstest.yml)

The project will replace [euklid](https://github.com/airgproducts/euklid).
The latest stable version of euklid can be obtained from [![PyPI version](https://badge.fury.io/py/euklid.svg)](https://badge.fury.io/py/euklid).

## About

A [Rust](https://www.rust-lang.org/) module with bindings for [python](https://www.python.org/) to help dealing with common CAD-like operations:

* Vectors
* PolyLines
* Spline Curves

## Support Table

[support.md](./support.md)

## Development Setup

To build the *euklid_rs* python module [PyO3](https://github.com/PyO3/pyo3) and [maturin](https://github.com/PyO3/maturin) is used.

Install the latest version of Rust with the [Getting started](https://www.rust-lang.org/learn/get-started) guide.

```
# create virtual environment
python -m venv venv

# activate venv
source venv/bin/activate

# Install python dependencies
pip install -r ./requirements.txt

# Build euklid_rs module
maturin dev

# Run python tests with pytest
pytest
```

### Code-Style
```
# Run pylint for prettier tests/*
pylint tests/*

# Run cargo fmt for prettier rust src files
cargo fmt 
```

## Build Setup

```
# Build euklid_rs module
maturin build
```

# License

[MIT License](./LICENSE)

Copyright (c) 2022-present, airG distribution GmbH