import fizzbuzz

def test_first_line(capsys):
    fizzbuzz.fizzbuzz()
    # Capture stdout so that we can check for things in tests
    # We'll get an array that contains each line in the output (the -1 is to deal with the trailing newline)
    output_lines = capsys.readouterr().out.split('\n')[:-1]
    assert output_lines[0] == '1'