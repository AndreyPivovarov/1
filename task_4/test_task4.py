from task_4.task4_run import parse_txt, task4_run


def test_task4():
    path_test_file = '/home/vjachesalv/Performance_lab/task_4/fixture/test.txt'
    massiv = parse_txt(path_test_file)
    result = task4_run(massiv)
    assert result == 16
