from task_2.task2_run import parse_txt, task2


def test_task2():
    path_file1 = '/home/vjachesalv/Performance_lab/task_2/fixture/centr_radius.txt'
    path_file2 = '/home/vjachesalv/Performance_lab/task_2/fixture/coordinate_point.txt'
    data = parse_txt(path_file1, path_file2)
    result = task2(data)
    print(result)