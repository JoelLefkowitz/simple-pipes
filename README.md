# Simple pipes

Subprocess utils.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/simple-pipes/review.yml)
![Version](https://img.shields.io/pypi/v/simple-pipes)
![Downloads](https://img.shields.io/pypi/dw/simple-pipes)
![Quality](https://img.shields.io/codacy/grade/dc58dc1425df48c5be692f01029b732e)
![Coverage](https://img.shields.io/codacy/coverage/dc58dc1425df48c5be692f01029b732e)

## Installation

```bash
pip install simple-pipes
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/simple-pipes).

### Usage

Pass a command in exec form:

```python
from simple_pipes import pipe_call, pipe_capture

pipe_call(["echo", "Hello"])
```

This is equivalent to:

```python
import subprocess

subprocess.Popen(["echo", "Hello"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
```

Changing directory before execution:

```python
pipe_call(["echo", "Hello"], cwd=".")
```

If you're running a command does not terminate, such as starting a server, the program will remain attached.

To detach the running process on a given string output:

```python
wrapper = pipe_call(["echo", "Hello"], break_str="Hello"):
```

You must keep the wrapper object in scope or the detached process will be terminated in garbage collection.

Often you want to run a process until it terminates and capture the entire output:

```python
output = pipe_capture(["echo", "Hello"], cwd=".")

print(output)

>> Hello
```

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
