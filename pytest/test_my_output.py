import sys

from pytest import CaptureFixture


def print_my_text() -> None:
    sys.stdout.write('Hello\n')
    sys.stderr.write('World\n')


def test_my_output(capsys: CaptureFixture) -> None:
    print_my_text()
    captured = capsys.readouterr()
    assert captured.out == 'Hello\n'
    assert captured.err == 'World\n'
