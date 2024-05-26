import subprocess
from io import TextIOWrapper


def pipe_call(call, cwd=".", break_str=None):
    with subprocess.Popen(
        call, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd
    ) as proc:
        wrapper = TextIOWrapper(proc.stdout, encoding="utf-8")

        for line in wrapper:
            if break_str and break_str in line:
                wrapper.detach()
                return wrapper

            print(line, end="")
            return None


def pipe_capture(call, cwd="."):
    lines = subprocess.check_output(call, cwd=cwd)
    return lines.decode("utf-8").split("\n")[:-1]
