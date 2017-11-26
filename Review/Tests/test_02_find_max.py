from Tasks.Random_FindMax_task import find_max_from_random


def test_01_check_all():
    original_list = find_max_from_random()[0]
    max_list = find_max_from_random()[1]
    assert len(original_list) == 1000
    assert max_list[0] != max_list[1] and max_list[0] > max_list[1]
    for ch in original_list:
        assert (max_list[0] >= ch or max_list[1] >= ch) is True
