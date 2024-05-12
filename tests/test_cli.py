import subprocess


def test_main():
    assert subprocess.check_output(["chatman", "foobar"], text=True) == "foobar\n"
