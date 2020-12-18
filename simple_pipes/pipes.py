import subprocess
from io import TextIOWrapper


def pipe_call(call, cwd=".", break_str=None):
    wrapper = TextIOWrapper(
        subprocess.Popen(
            call, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd
        ).stdout,
        encoding="utf-8",
    )

    for line in wrapper:
        print(line, end="")

        if break_str and break_str in line:
            wrapper.detach()
            return wrapper


def pipe_capture(call, cwd="."):
    lines = subprocess.check_output(call, cwd=cwd)
    return lines.decode("utf-8").split("\n")[:-1]

