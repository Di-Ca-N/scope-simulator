import subprocess
import pathlib

def run_program(program, scope):
    p = subprocess.run(['python3', "main.py", "--scoping", scope, program], encoding='utf-8', stdout=subprocess.PIPE)

    return p.stdout

def test_prog1_static():
    output = run_program("tests/prog1.pd", "static")
    expected = pathlib.Path("tests/prog1_out_static.txt").read_text()
    assert output == expected

def test_prog1_dynamic():
    output = run_program("tests/prog1.pd", "dynamic")
    expected = pathlib.Path("tests/prog1_out_dynamic.txt").read_text()
    assert output == expected


def test_prog2_static():
    output = run_program("tests/prog2.pd", "static")
    expected = pathlib.Path("tests/prog2_out_static.txt").read_text()
    assert output == expected

def test_prog2_dynamic():
    output = run_program("tests/prog2.pd", "dynamic")
    expected = pathlib.Path("tests/prog2_out_dynamic.txt").read_text()
    assert output == expected
