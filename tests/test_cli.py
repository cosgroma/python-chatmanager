import subprocess


def test_main():
    assert subprocess.check_output(["chatman", "foo", "foobar"], text=True) == "foobar\n"
