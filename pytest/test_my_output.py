import sys


def print_my_text():
    sys.stdout.write('Hello\n')
    sys.stderr.write('World\n')


def test_my_output(capsys):
    print_my_text()
    captured = capsys.readouterr()
    assert captured.out == 'Hello\n'
    assert captured.err == 'World\n'


