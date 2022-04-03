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


def test_common_superior_cid_superior() -> None:
    head = Citizen(1, "", 0, "", 10)
    cid = Citizen(2, "", 0, "", 10)
    child = Citizen(3, "", 0, "", 10)

    head.add_subordinate(cid)
    cid.add_subordinate(child)

    # NOTE: The correct case might be that this `== head`
    assert child.get_closest_common_superior(2) == cid


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


# Citizen.get_highest_rated_subordinate
def test_highest_rating_branching() -> None:
    a = DistrictLeader(15, "", 0, "", 10, "Florida")
    b = Citizen(2, "", 0, "", 20)
    c = Citizen(13, "", 0, "", 40)

    a.add_subordinate(b)
    a.add_subordinate(c)

    assert a.get_highest_rated_subordinate() == c
    a.remove_subordinate(13)
    assert a.get_highest_rated_subordinate() == b


# Society.add_citizen
def test_add_citizen() -> None:
    s = Society()
    a = DistrictLeader(15, "", 0, "", 10, "Florida")

    s.add_citizen(a)

    assert s.get_head() == a

    b = Citizen(2, "", 0, "", 10)
    s.add_citizen(b, None)

    assert s.get_head() == b
    assert b.get_all_subordinates() == [a]

    c = Citizen(13, "", 0, "", 10)
    s.add_citizen(c, 15)

    assert a.get_all_subordinates() == [c]


# Society.get_citizens_with_job
def test_get_citizens_with_job() -> None:
    o = Society()
    c1 = Citizen(10, "Starky Industries", 3024, "Manager", 50)
    c2 = Citizen(20, "Hookins National Lab", 3024, "Manager", 65)
    c3 = Citizen(12, "Starky Industries", 3024, "Labourer", 50)
    c4 = Citizen(6, "S.T.A.R.R.Y Lab", 3024, "Manager", 30)
    c5 = Citizen(52, "Hookins National Lab", 3024, "Labourer", 50)
    c6 = Citizen(8, "S.T.A.R.R.Y Lab", 3024, "Lawyer", 30)

    o.add_citizen(c4)
    o.add_citizen(c2)
    o.add_citizen(c6)
    o.add_citizen(c1)
    o.add_citizen(c3)
    o.add_citizen(c5)

    assert o.get_citizens_with_job("Manager") == [c4, c1, c2]


# Society.change_citizen_type
def test_change_citizen_type_branching() -> None:
    c = DistrictLeader(6, "Starky Industries", 3036, "Commander", 50, "Area 52")
    c2 = DistrictLeader(2, "Hookins National", 3027, "Manager", 55, "France")
    c3 = Citizen(3, "Starky Industries", 3050, "Labourer", 50)
    c4 = DistrictLeader(5, "S.T.A.R.R.Y Lab", 3024, "Manager", 17, "Finance")
    c5 = Citizen(8, "Hookins National", 3024, "Cleaner", 74)
    c6 = Citizen(7, "Hookins National", 3071, "Labourer", 5)
    c7 = Citizen(9, "S.T.A.R.R.Y Lab", 3098, "Engineer", 86)

    society = Society()
    society.add_citizen(c)
    society.add_citizen(c2, 6)
    society.add_citizen(c3, 6)
    society.add_citizen(c4, 6)
    society.add_citizen(c5, 6)
    society.add_citizen(c6, 5)
    society.add_citizen(c7, 5)

    old = society.get_citizen(5)
    assert old is not None
    old_subordinates = old.get_all_subordinates()

    changed = society.change_citizen_type(5)
    fetched_changed = society.get_citizen(5)

    assert isinstance(changed, Citizen)
    assert changed == fetched_changed
    assert changed.get_all_subordinates() == old_subordinates
    assert society.get_all_citizens() == [c2, c3, changed, c, c6, c5, c7]


if __name__ == "__main__":
    import pytest  # type: ignore

    pytest.main(["luke_tests.py"])
