from Tasks.DataCheck_task import check_my_date


def test_01_check_valid_date(valid_date):
    assert check_my_date(valid_date) is True


def test_02_check_invalid_date(invalid_date):
    assert check_my_date(invalid_date) is False
