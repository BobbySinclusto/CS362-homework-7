import fizzbuzz

def test_first_line(capsys):
    fizzbuzz.fizzbuzz()
    # Capture stdout so that we can check for things in tests
    # We'll get an array that contains each line in the output (the -1 is to deal with the trailing newline)
    output_lines = capsys.readouterr().out.split('\n')[:-1]
    assert output_lines[0] == '1'

# Make sure that lines that just contain numbers are correct
def test_non_special_lines(capsys):
    fizzbuzz.fizzbuzz()
    # Capture stdout so that we can check for things in tests
    # We'll get an array that contains each line in the output (the -1 is to deal with the trailing newline)
    output_lines = capsys.readouterr().out.split('\n')[:-1]
    
    for i in range(1, 101):
        if i % 3 != 0 and i % 5 != 0:
            assert output_lines[i - 1] == str(i)

# Make sure that lines that are divisible by 3 (but not 5) are correct
def test_fizz(capsys):
    fizzbuzz.fizzbuzz()
    # Capture stdout so that we can check for things in tests
    # We'll get an array that contains each line in the output (the -1 is to deal with the trailing newline)
    output_lines = capsys.readouterr().out.split('\n')[:-1]
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            assert output_lines[i - 1] == 'Fizz'

# Make sure that lines that are divisible by 5 (but not 3) are correct
def test_buzz(capsys):
    fizzbuzz.fizzbuzz()
    # Capture stdout so that we can check for things in tests
    # We'll get an array that contains each line in the output (the -1 is to deal with the trailing newline)
    output_lines = capsys.readouterr().out.split('\n')[:-1]
    
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 != 0:
            assert output_lines[i - 1] == 'Buzz'

# Make sure that lines that are divisible by 5 and 3 are correct
def test_fizz_and_buzz(capsys):
    fizzbuzz.fizzbuzz()
    # Capture stdout so that we can check for things in tests
    # We'll get an array that contains each line in the output (the -1 is to deal with the trailing newline)
    output_lines = capsys.readouterr().out.split('\n')[:-1]
    
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            assert output_lines[i - 1] == 'FizzBuzz'