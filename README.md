# simple_tracker

[license-image]: https://img.shields.io/npm/l/make-coverage-badge.svg
[license-url]: https://opensource.org/licenses/MIT

[ci-image]: https://github.com/bherbruck/simple_tracker/workflows/Python%20package/badge.svg
[ci-url]: https://github.com/bherbruck/simple_tracker/actions?query=workflow%3A%22Python+package%22

[![License][license-image]][license-url]
[![Python package][ci-image]][ci-url]

Track multiple objects using just x, y coordinates!

simple_tracker is a simple cemtrpod object tracker and requires no external dependencies other than the Python standard library. It is originally designed to count and track objects on [OpenMV](https://openmv.io/) MicroPython boards and will see future use with opencv-python on Raspberry Pi.

## In action

This was made using an OpenMV cam and the example [here](examples/openmv/simple_tracking.py)

![Video](docs/media/tacking3.gif)

## Installation
```bash
$ pip install git+https://github.com/bherbruck/simple_tracker
```
or
```bash
$ pip install simple-tracker
```
## Usage
All you need to do is pass a list of tuples (x, y) to the Tracker.update() method
```python
from simple_tracker import Tracker

tracker = Tracker()
while True:
    centroids = some_detection_algorithm()
    tracker.update(centroids)
```