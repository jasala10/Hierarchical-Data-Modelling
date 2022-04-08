from society_hierarchy import *

# ~~~ TASK 1 ~~~


def test_add_subordinate_00()-> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    assert len(c1._subordinates) == 0


def test_add_subordinate_01() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c1.add_subordinate(c2)
    assert len(c1._subordinates) == 1


def test_add_subordinate_02() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(4, "Hookins National Lab", 3024, "Manager", 30)
    c1.add_subordinate(c2)
    c1.add_subordinate(c3)
    assert len(c1._subordinates) == 2
    # assert c1._subordinates[0].cid == 2
    # assert c1._subordinates[1].cid == 4


def test_add_subordinate_03() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(10, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(4, "Hookins National Lab", 3024, "Manager", 30)
    c1.add_subordinate(c2)
    assert len(c1._subordinates) == 1
    c1.add_subordinate(c3)
    assert len(c1._subordinates) == 2
    assert c1._subordinates[0].cid == 4
    assert c1._subordinates[1].cid == 10


def test_remove_subordinate_00() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(10, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(4, "Hookins National Lab", 3024, "Manager", 30)
    c1.add_subordinate(c2)
    c1.add_subordinate(c3)
    assert c2._superior == c1
    assert c3._superior == c1
    assert len(c1._subordinates) == 2
    c1.remove_subordinate(10)
    assert c1._subordinates == [c3]
    assert c2._superior is None


def test_become_subordinate_to_00() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c1.become_subordinate_to(c2)
    assert c1.get_superior().cid == 2
    assert c2.get_direct_subordinates()[0].cid == 1
    c1.become_subordinate_to(None)
    assert c1.get_superior() is None
    assert c2.get_direct_subordinates() == []


def test_become_subordinate_01() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c1.become_subordinate_to(None)
    assert c1._superior is None


def test_become_subordinate_02() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(4, "Hookins National Lab", 3024, "Manager", 30)
    c1.become_subordinate_to(c3)
    c1.become_subordinate_to(c2)
    assert c3._subordinates == []
    assert c1._superior == c2
    assert c2._subordinates == [c1]


def test_society_get_citizen_00() -> None:
    s = Society()
    assert s.get_citizen(10) is None


def test_society_get_citizen_01() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(4, "Hookins National Lab", 3024, "Manager", 30)
    s.add_citizen(c1)
    s.add_citizen(c2)
    s.add_citizen(c3)
    assert s.get_citizen(10) is None
    assert s.get_citizen(4) is c3
    assert s.get_citizen(2) is c2
    assert s.get_citizen(1) is c1


def test_get_all_citizens_00() -> None:
    c = Citizen(6, "Starky Industries", 3036, "Commander", 50)
    c2 = Citizen(2, "Hookins National", 3027, "Manager", 55)
    c3 = Citizen(3, "Starky Industries", 3050, "Labourer", 50)
    c4 = Citizen(5, "S.T.A.R.R.Y Lab", 3024, "Manager", 17)
    c5 = Citizen(8, "Hookins National", 3024, "Cleaner", 74)
    c6 = Citizen(7, "Hookins National", 3071, "Labourer", 5)
    c7 = Citizen(9, "S.T.A.R.R.Y Lab", 3098, "Engineer", 86)

    s = Society()
    s.add_citizen(c)
    s.add_citizen(c2, 6)
    s.add_citizen(c3, 6)
    s.add_citizen(c4, 6)
    s.add_citizen(c5, 6)
    s.add_citizen(c6, 5)
    s.add_citizen(c7, 5)

    assert s.get_all_citizens() == [c2, c3, c4, c, c6, c5, c7]


def test_society_add_citizen_00() -> None:
    s = Society()
    c5 = Citizen(5, "Hookins National", 3024, "Cleaner", 5)
    c6 = Citizen(6, "Jake", 2003, "job", 6)
    s.add_citizen(c5)
    assert s.get_head() == c5
    s.add_citizen(c6, 5)
    assert s.get_head() == c5
    assert c5._subordinates == [c6]


def test_society_add_citizen_01() -> None:
    s = Society()
    c5 = Citizen(5, "Hookins National", 3024, "Cleaner", 5)
    c18 = Citizen(18, "Jake", 2003, "job", 18)
    c6 = Citizen(6, "Jake", 2003, "job", 6)
    s.add_citizen(c5)
    s.add_citizen(c18, 5)
    assert s.get_head() == c5
    s.add_citizen(c6, 5)
    assert s.get_head() == c5
    assert c5._subordinates == [c6, c18]


def test_society_add_citizen_02() -> None:
    s = Society()
    c5 = Citizen(5, "Hookins National", 3024, "Cleaner", 5)
    c18 = Citizen(18, "Jake", 2003, "job", 18)
    c19 = Citizen(19, "Jack", 2014, "child", 19)
    c6 = Citizen(6, "Jake", 2003, "job", 6)
    s.add_citizen(c5)
    s.add_citizen(c18, 5)
    assert s.get_head() == c5
    s.add_citizen(c6, 5)
    s.add_citizen(c19, 5)
    assert s.get_head() == c5
    assert c5._subordinates == [c6, c18, c19]


def test_society_add_citizen_03() -> None:
    s = Society()
    c1 = Citizen(1, "Hookins National", 3024, "Cleaner", 1)
    c5 = Citizen(5, "Jake", 2003, "job", 5)
    c18 = Citizen(18, "Jake", 2003, "job", 18)
    c6 = Citizen(6, "Dr. Jacques Bailly", 1978, "Scripps", 6)
    s.add_citizen(c1)
    s.add_citizen(c5, 1)
    s.add_citizen(c18, 5)
    assert s.get_head() == c1
    assert c1._subordinates == [c5]
    assert c5._subordinates == [c18]
    s.add_citizen(c6, 5)
    assert c5.get_all_subordinates() == [c6, c18]


def test_society_add_citizen_04() -> None:
    s = Society()
    c6 = Citizen(10, "Olga Lance", 1964, "Mother", 10)
    s.add_citizen(c6)
    assert s.get_head() == c6


def test_society_add_citizen_05() -> None:
    s = Society()
    c6 = Citizen(10, "Olga Lance", 1964, "Mother", 10)
    c17 = Citizen(17, "Jake Lance", 2003, "Anthropologist", 17)
    s.add_citizen(c17)
    s.add_citizen(c6)
    assert s.get_head() == c6


def test_society_add_citizen_06() -> None:
    s = Society()
    c5 = Citizen(5, "Olga Lance", 1964, "Mother", 5)
    s.add_citizen(c5)
    c18 = Citizen(18, "Jake Lance", 2003, "Anthropologist", 18)
    c19 = Citizen(5, "Chloe Lance", 2008, "Dog", 19)
    s.add_citizen(c18, 5)
    s.add_citizen(c19, 5)
    c10 = Citizen(10, "Pope Francis", 1949, "Pope", 10)
    s.add_citizen(c10)
    assert s.get_head() == c10


def test_district_00() -> None:
    c = DistrictLeader(6, "Starky Industries", 3036, "Commander", 50, "Area 52")
    c2 = DistrictLeader(2, "Hookins National", 3027, "Manager", 55, "France")
    c3 = Citizen(3, "Starky Industries", 3050, "Labourer", 50)
    c4 = DistrictLeader(5, "S.T.A.R.R.Y Lab", 3024, "Manager", 17, "Finance")
    c5 = Citizen(8, "Hookins National", 3024, "Cleaner", 74)
    c6 = Citizen(7, "Hookins National", 3071, "Labourer", 5)
    c7 = Citizen(9, "S.T.A.R.R.Y Lab", 3098, "Engineer", 86)

    s = Society()
    s.add_citizen(c)
    s.add_citizen(c2, 6)
    s.add_citizen(c3, 6)
    s.add_citizen(c4, 6)
    s.add_citizen(c5, 6)
    s.add_citizen(c6, 5)
    s.add_citizen(c7, 5)


### SAMPLE TREES
