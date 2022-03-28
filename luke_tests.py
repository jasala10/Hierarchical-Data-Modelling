from society_hierarchy import *

# Citizen.get_citizen

def test_get_citizen_empty() -> None:
    c = Citizen(1, "", 0, "", 10)
    assert c.get_citizen(123) == None

def test_get_citizen_immediate() -> None:
    a = Citizen(1, "", 0, "", 10)
    b = Citizen(2, "", 0, "", 10)

    a.add_subordinate(b)

    assert a.get_citizen(2) == b

def test_get_citizen_indirect() -> None:
    a = Citizen(1, "", 0, "", 10)
    b = Citizen(2, "", 0, "", 10)
    c = Citizen(3, "", 0, "", 10)

    a.add_subordinate(b)
    b.add_subordinate(c)

    assert a.get_citizen(3) == c

def test_get_citizen_branching() -> None:
    a = Citizen(1, "", 0, "", 10)
    b = Citizen(2, "", 0, "", 10)
    c = Citizen(3, "", 0, "", 10)
    d = Citizen(4, "", 0, "", 10)
    e = Citizen(5, "", 0, "", 10)

    a.add_subordinate(b)
    b.add_subordinate(c)
    b.add_subordinate(d)
    d.add_subordinate(e)

    assert a.get_citizen(5) == e


# Citizen.get_all_subordinates
def test_subordinates_empty() -> None:
    a = Citizen(1, "", 0, "", 10)

    assert a.get_all_subordinates() == []

def test_subordinates_immediate() -> None:
    a = Citizen(1, "", 0, "", 10)
    b = Citizen(2, "", 0, "", 10)

    a.add_subordinate(b)

    assert a.get_all_subordinates() == [b]

def test_subordinates_branching() -> None:
    a = Citizen(1, "", 0, "", 10)
    b = Citizen(2, "", 0, "", 10)
    c = Citizen(13, "", 0, "", 10)
    d = Citizen(8, "", 0, "", 10)
    e = Citizen(100, "", 0, "", 10)

    a.add_subordinate(b)
    b.add_subordinate(c)
    b.add_subordinate(d)
    d.add_subordinate(e)

    assert a.get_all_subordinates() == [b, d, c, e]

# Citizen.get_society_head
def test_head_empty() -> None:
    a = Citizen(1, "", 0, "", 10)

    assert a.get_society_head() == a

def test_head_immediate() -> None:
    a = Citizen(1, "", 0, "", 10)
    b = Citizen(2, "", 0, "", 10)

    a.add_subordinate(b)

    assert b.get_society_head() == a

def test_head_branching() -> None:
    a = Citizen(1, "", 0, "", 10)
    b = Citizen(2, "", 0, "", 10)
    c = Citizen(13, "", 0, "", 10)
    d = Citizen(8, "", 0, "", 10)
    e = Citizen(100, "", 0, "", 10)

    a.add_subordinate(b)
    b.add_subordinate(c)
    b.add_subordinate(d)
    d.add_subordinate(e)

    assert e.get_society_head() == a

if __name__ == "__main__":
    import pytest  # type: ignore

    pytest.main(["luke_tests.py"])

