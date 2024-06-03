import pytest
from src.func import find_executed_elements
from src.func import format_date
from src.func import format_secret_card
from src.func import date_to_int
from src.func import display_transaction

@pytest.fixture
def list_fixture():
    return [{"id": 111, "state": "EXECUTED", "payment": 'Счет 11223344556677889900'},
            {"id": 222, "state": "PENDING", "payment": 'Visa Card 1122334455667788'},
            {"id": 333, "payment": 'Maestro Card 8877665544332211'},
            {},
            {"id": 444, "state": "EXECUTED", "payment": 'счёт 00998877665544332211'}
            ]
@pytest.fixture
def date_fixture():
    return "2019-02-14T03:09:23.006652"

def test_find_executed_elements(list_fixture):
    assert find_executed_elements(list_fixture) == [{"id": 111, "state": "EXECUTED", "payment": 'Счет 11223344556677889900'},
                                                    {"id": 444, "state": "EXECUTED", "payment": 'счёт 00998877665544332211'}]
    assert isinstance(find_executed_elements(list_fixture), list)

def test_format_date(date_fixture):
    assert format_date(date_fixture) == '14.02.2019'

def test_format_secret_card1(list_fixture):
    test_string = list_fixture[0]["payment"]
    assert format_secret_card(test_string) == 'Счет **9900'

def test_format_secret_card2(list_fixture):
    test_string = list_fixture[1]["payment"]
    assert format_secret_card(test_string) == 'Visa Card 1122 33** **** 7788'

def test_date_to_int(date_fixture):
    assert date_to_int(date_fixture) == 20190214030923006652

def test_display_transaction(list_fixture):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        display_transaction(list_fixture[0])
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1
