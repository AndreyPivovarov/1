from task_2.task2_run import parse_txt, task2
import json


def test_task2():
    path_file1 = '/home/vjachesalv/Performance_lab/task_2/fixture/centr_radius.txt'
    path_file2 = '/home/vjachesalv/Performance_lab/task_2/fixture/coordinate_point.txt'
    data = parse_txt(path_file1, path_file2)
    result = task2(data)
    result_json = json.dumps(result, indent=4)
    with open('/home/vjachesalv/Performance_lab/task_2/fixture/result.json', 'r') as f:
        test_json = json.dumps(json.load(f), indent=4)
        result_json = json.dumps(result, indent=4)
        assert result_json == test_json
