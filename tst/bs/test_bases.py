from bs import Base, parse_base, InvalidCliArgsError

BASE = Base([], "blah", 2, "prefix")

def test_parse_base():
    cases = [
        (("h", "hex", "hexadecimal"), ("hexadecimal", 16)),
        (("b", "bin", "binary"), ("binary", 2)),
        (("d", "dec", "decimal"), ("decimal", 10)),
        (("o", "oct", "octal"), ("octal", 8)),
        (("he", "oc", "bi", "deci", "flabbygooberblat", "H", "D"), None),
        (("2",), ("base-2", 2)),
        (("16",), ("base-16", 16)),
        (("1", "17"), None)
    ]
    for ss, expected in cases:
        for s in ss:
            print(s, expected)
            if expected is None:
                threw = False
                try:
                    base = parse_base(s)
                    print("oops:", base.full_name)
                except InvalidCliArgsError:
                    threw = True
                assert threw
            else:
                full_name, n = expected
                base = parse_base(s)
                assert full_name == base.full_name
                assert n == base.size

def test_matches():
    assert BASE.matches("0")
    assert BASE.matches("1")
    assert BASE.matches("10")
    assert BASE.matches("11")
    assert not BASE.matches("01") # no leading 0s
    assert BASE.matches("prefix1")
    assert BASE.matches("prefix0")
    assert not BASE.matches("pre1")
    assert not BASE.matches("pre0")
    assert not BASE.matches("2")
    assert not BASE.matches("-0")
    assert not BASE.matches("-1")
    assert not BASE.matches("prefix2")

def test_parse():
    # Don't bother checking what happens in the failure cases, they
    # should be caught by matches().
    assert 0 == BASE.parse("0")
    assert 1 == BASE.parse("1")
    assert 2 == BASE.parse("10")
    assert 3 == BASE.parse("11")
    assert 4 == BASE.parse("100")
    assert 5 == BASE.parse("101")
    assert 0 == BASE.parse("prefix0")
    assert 1 == BASE.parse("prefix1")
    assert 2 == BASE.parse("prefix10")

def test_format():
    assert "0" == BASE.format(0)
    assert "1" == BASE.format(1)
    assert "10" == BASE.format(2)
    assert "11" == BASE.format(3)
    assert "100" == BASE.format(4)
