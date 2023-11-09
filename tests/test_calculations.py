from app.calculations import add, BankAccount, Insufficient
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3,2,5),
    (-3,8,5),
    (9,0,9)
] )

def test_add(num1, num2, expected):
    print("===testing add function===")
    assert add(num1, num2) == expected

def test_bank_set_initial_amount():
    bank = BankAccount(50)
    assert bank.balance == 50

def test_bank_default_amount(zero_bank_account):
    print('testing my bank acc')
    assert zero_bank_account.balance == 0





































@pytest.mark.parametrize("deposited, withdraw, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000),
    #(10, 50, -40)
])
def test_bank_transaction(zero_bank_account, deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(Insufficient):
        bank_account.withdraw(200)