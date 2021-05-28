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