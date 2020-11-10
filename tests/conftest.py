import os
from glob import glob

fixture_dir_globs = ["tests/fixtures/*"]

pytest_plugins = [
    path.replace("/", ".").replace(".py", "")
    for pattern in fixture_dir_globs
    for path in glob(pattern)
    if os.path.isfile(path) and path.endswith(".py")
]
