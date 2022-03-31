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

# Citizen.get_closest_common_superior
def test_common_superior_branching() -> None:
    a = Citizen(1, "", 0, "", 10)
    b = Citizen(2, "", 0, "", 10)
    c = Citizen(13, "", 0, "", 10)
    d = Citizen(8, "", 0, "", 10)
    e = Citizen(100, "", 0, "", 10)

    a.add_subordinate(b)
    b.add_subordinate(c)
    b.add_subordinate(d)
    d.add_subordinate(e)

    assert e.get_closest_common_superior(8) == d
    assert e.get_closest_common_superior(1) == a
    assert e.get_closest_common_superior(13) == b


# Citizen.get_district_name
def test_get_set_district_name_branching() -> None:
    a = Citizen(1, "", 0, "", 10)
    b2 = Citizen(1, "", 0, "", 10)
    b = DistrictLeader(2, "", 0, "", 10, "Canada")
    c = Citizen(13, "", 0, "", 10)
    d = DistrictLeader(8, "", 0, "", 10, "Ontario")
    e = Citizen(100, "", 0, "", 10)
    f = Citizen(72, "", 0, "", 10)

    a.add_subordinate(b)
    a.add_subordinate(b2)
    b.add_subordinate(c)
    b.add_subordinate(d)
    d.add_subordinate(e)
    d.add_subordinate(f)

    assert f.get_district_name() == "Ontario"
    assert a.get_district_name() == ""
    assert d.get_district_name() == "Ontario"
    assert d.get_district_name() == "Ontario"
    assert b2.get_district_name() == ""


# DistrictLeader.(get/set)_district_name
def test_get_set_district_name() -> None:
    a = DistrictLeader(15, "", 0, "", 10, "Florida")
    assert a.get_district_name() == "Florida"

    a.rename_district("Northwater")
    assert a.get_district_name() == "Northwater"

# DistrictLeader.get_district_citizens
def test_district_citizens_branching() -> None:
    a = DistrictLeader(15, "", 0, "", 10, "Florida")
    b = Citizen(2, "", 0, "", 10)
    c = Citizen(13, "", 0, "", 10)
    d = Citizen(8, "", 0, "", 10)
    e = Citizen(100, "", 0, "", 10)

    a.add_subordinate(b)
    b.add_subordinate(c)
    b.add_subordinate(d)
    d.add_subordinate(e)

    assert a.get_district_citizens() == [b, d, c, a, e]

if __name__ == "__main__":
    import pytest  # type: ignore

    pytest.main(["luke_tests.py"])

