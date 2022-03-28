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


"""
Remove subordinate:

-- one item list, becomes empty
-- two item list where cid at start
-- three item list, cid at end
-- five item list, cid in position 4

-- make sure _subordinates has changed appropriately
-- make sure the item's superior is also changed
"""


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
