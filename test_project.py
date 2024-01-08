import pytest
from project import depositMoney, deductMoney, cardValue, handValue


User_Capital = 0
def test_depositMoney():
    global User_Capital
    assert depositMoney(20) == 20
    assert depositMoney(30) == 50

def test_deductMoney():
    global User_Capital
    assert deductMoney(20) == 30
    assert deductMoney(30) == 0

def test_cardValue():
    assert cardValue("Ace of Hearts") == 11
    assert cardValue("King of Clubs") == 10

def test_handValue():
    assert handValue(["Ace of Hearts", "King of Clubs"]) == 21
    assert handValue(["Six of Spades", "Seven of Clovers"]) == 13
    

