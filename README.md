# Pipes

Subprocess utils

### Status

| Source     | Shields                                                        |
| ---------- | -------------------------------------------------------------- |
| Project    | ![license][license] ![release][release]                        |
| Publishers | [![pypi][pypi]][pypi_link]                                     |
| Downloads  | ![pypi_downloads][pypi_downloads]                              |
| Raised     | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

### Installing

To install the package from pypi:

```bash
pip install simple_pipes
```

Alternatively, you can clone the repo and build the package locally.

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

Changing directory before execxution:

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

### Docs

Additional details are available in the [full documentation](https://pipes.readthedocs.io/en/latest/).

To generate the documentation locally:

```bash
multi-job docs
```

### Tests

Unit tests and behaviour tests are written with the pytest framework.

To run tests:

```bash
multi-job tests
```

Additionally, an html report will be saved to the local directory.

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

### Versioning

[SemVer](http://semver.org/) is used for versioning. For a list of versions available, see the tags on this repository.

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

Releases are made on every major change.

### Author

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz](https://github.com/JoelLefkowitz)

See also the list of contributors who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

None yet!

<!--- Table links --->

[license]: https://img.shields.io/github/license/joellefkowitz/pipes
[release]: https://img.shields.io/github/v/tag/joellefkowitz/pipes
[pypi_downloads]: https://img.shields.io/pypi/dw/simple_pipes
[pypi]: https://img.shields.io/pypi/v/simple_pipes "PyPi"
[pypi_link]: https://pypi.org/project/simple_pipes
[issues]: https://img.shields.io/github/issues/joellefkowitz/pipes "Issues"
[issues_link]: https://github.com/JoelLefkowitz/pipes/issues
[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/pipes "Pull requests"
[pulls_link]: https://github.com/JoelLefkowitz/pipes/pulls
