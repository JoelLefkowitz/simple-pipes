import os
from src.pipes import pipe_capture


def test_project_name():
    assert pipe_capture("pwd")[0] == os.getcwd()
