"""Tests for pyglint."""


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
    assert "bad-name" in output
    assert "import-from" in output
