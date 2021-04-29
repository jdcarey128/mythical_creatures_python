import pytest
from lib.pirate import *

def test_it_has_a_name():
    pirate = Pirate("Jack")
    assert pirate.name == "Jack"

def test_it_has_a_different_name():
    pirate = Pirate("Blackbeard")
    assert pirate.name == "Blackbeard"

def test_it_is_a_scallywag_by_default():
    pirate = Pirate("Jack")
    assert pirate.job == "Scallywag"

def test_its_not_always_a_scallywag():
    pirate = Pirate("Jack", "Cook")
    assert pirate.job == "Cook"

def test_isnt_cursed_by_default():
    pirate = Pirate("Jack")
    assert not pirate.is_cursed()

def test_becomes_cursed_after_enough_heinous_acts():
    pirate = Pirate("Jack")
    assert not pirate.is_cursed()
    pirate.commit_heinous_act()
    assert not pirate.is_cursed()
    pirate.commit_heinous_act()
    assert not pirate.is_cursed()
    pirate.commit_heinous_act()
    assert pirate.is_cursed()

def test_a_pirate_has_booty():
    pirate = Pirate("Jack")
    assert pirate.booty == 0

def test_a_pirate_gets_100_booty_for_robbing_ships():
    pirate = Pirate("Jack")
    assert pirate.booty == 0
    pirate.rob_ship()
    assert pirate.booty == 100
    pirate.rob_ship()
    pirate.rob_ship()
    assert pirate.booty == 300
