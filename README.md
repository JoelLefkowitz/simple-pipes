# Simple pipes

Subprocess utils.

## Status

| Source     | Shields                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Project    | ![release][release_shield] ![license][license_shield] ![dependents][dependents_shield]                             |
| Health     | ![travis][travis_shield] ![codacy][codacy_shield] ![coverage][coverage_shield] ![readthedocs][readthedocs_shield]  |
| Repository | ![issues][issues_shield] ![pulls][pulls_shield]                                                                    |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]           |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield] |

## Installation

```bash
pip install simple_pipes
```

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

## Tests

To run unit tests:

```bash
grunt tests:unit
```

To generate a coverage report:

```bash
grunt tests:coverage
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To generate the sphinx configuration:

```bash
grunt docs:generate
```

Then build the documentation:

```bash
grunt docs:build
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

Before commiting new code:

```bash
grunt precommit
```

This will run linters, formaters, generate a test coverage report and the sphinx configuration.

## Versioning

This repository adheres to semantic versioning standards.
For more inforamtion on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joellefkowitz]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Github links -->

[pulls]: https://github.com/JoelLefkowitz/simple-pipes/pulls
[issues]: https://github.com/JoelLefkowitz/simple-pipes/issues

<!-- External links -->

[readthedocs]: https://simple-pipes.readthedocs.io/en/latest/
[semver]: http://semver.org/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[joellefkowitz]: https://github.com/JoelLefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/simple-pipes
[license_shield]: https://img.shields.io/github/license/joellefkowitz/simple-pipes
[dependents_shield]: https://img.shields.io/librariesio/dependent-repos/pypi/simple_pipes

<!-- Health shields -->

[travis_shield]: https://img.shields.io/travis/joellefkowitz/simple-pipes
[codacy_shield]: https://img.shields.io/codacy/coverage/simple-pipes
[coverage_shield]: https://img.shields.io/codacy/grade/simple-pipes
[readthedocs_shield]: https://img.shields.io/readthedocs/simple-pipes

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/simple-pipes
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/simple-pipes

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/simple_pipes
[python_versions_shield]: https://img.shields.io/pypi/pyversions/simple_pipes
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/simple_pipes

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/simple-pipes
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/simple-pipes
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/simple-pipes
