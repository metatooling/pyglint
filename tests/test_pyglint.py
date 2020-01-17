import subprocess
import sys


def test_example():
    args = [
        sys.executable,
        "-m",
        "pylint",
        "--load-plugins",
        "examples.mylinter",
        "examples/to-be-linted.py",
    ]
    output = subprocess.run(args, check=False, stdout=subprocess.PIPE).stdout.decode()

    assert (
        "examples/to-be-linted.py:6:0: E4019: The name 'xor' is against the guidelines. (bad-name)"
        in output
    )
    assert (
        "examples/to-be-linted.py:1:0: E4012: `from ... import` is not allowed. (import-from)"
        in output
    )
