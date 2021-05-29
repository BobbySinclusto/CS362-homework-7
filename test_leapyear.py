import leapyear

# Test to make sure that the program correctly detects that years divisible by 4
# are leap years (excluding those divisible by 100)
def test_div_4():
    assert leapyear.is_leapyear(4) == True
    assert leapyear.is_leapyear(2020) == True
    assert leapyear.is_leapyear(1924) == True

# Test to make sure thzt the program correctly detects that years not divisible by 4
# are not leap years
def test_not_div_4():
    assert leapyear.is_leapyear(3) == False
    assert leapyear.is_leapyear(1999) == False
    assert leapyear.is_leapyear(2001) == False

# Test to make sure that the program correctly detects that years divisible by 100 are
# not leap years.
def test_div_100():
    assert leapyear.is_leapyear(1800) == False
    assert leapyear.is_leapyear(1900) == False
    assert leapyear.is_leapyear(2100) == False

# Test to make sure that the program correctly detects that years divisible by 400 are
# leap years.
def test_div_400():
    assert leapyear.is_leapyear(1600) == True
    assert leapyear.is_leapyear(2000) == True
    assert leapyear.is_leapyear(2400) == True
