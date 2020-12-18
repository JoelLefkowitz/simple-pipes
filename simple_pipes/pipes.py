import subprocess
from io import TextIOWrapper


def pipe_call(call, cwd=".", break_str=None):
    p = subprocess.Popen(
        call, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd
    )

    for line in TextIOWrapper(p.stdout, encoding="utf-8"):
        print(line, end="")

        if break_str and break_str in line:
            break

def pipe_capture(call, cwd="."):
    lines = subprocess.check_output(call, cwd=cwd)
    return lines.decode("utf-8").split("\n")[:-1]
