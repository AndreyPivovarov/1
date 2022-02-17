from task_1.task1_run import task1


def test_task1():
    assert task1(4, 3) == '13'
    assert task1(5, 4) == '14253'
