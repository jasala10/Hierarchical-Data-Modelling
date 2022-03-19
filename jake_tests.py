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
