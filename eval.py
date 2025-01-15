def eval(s):
    for c in s:
        assert c in "-0123456789.", "Invalid input"
    n = 0

    if s[0] == "-":
        sign = -1
        #drops the first char then returns the rest of the string
        s = s[1:]
    else:
        sign = 1 
    multi = 1.0
    fractional = False
    assert len(s) > 0, "Invalid input"
    while len(s) > 0:
        c = s[0]
        s = s[1:]
        if c == ".":
            assert not fractional, "Invalid input"
            fractional = True
            continue
        n = n * 10 + ord(c) - ord("0")
        if fractional:
            multi *= 10
    for c in s:
        n = n * 10 + ord(c) - ord("0")
    return n * sign

def test_eval():
    """ test eval """
    print("testing eval")
    assert eval("0") == 0, "Expect 0 to be 0"
    assert eval("1") == 1
    assert eval("99") == 99
    assert eval("123456789") == 123456789
    assert eval("1099") == 1099
    assert eval("0001") == 1
    assert eval("-99") == -99


if __name__ == "__main__":
    test_eval()
    print("eval.py: all tests pass")