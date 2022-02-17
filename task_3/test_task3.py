import json
from task_3.task3_run import task3


def test_parse_json():
    path_value = '/home/vjachesalv/Performance_lab/task_3/fixture/values.json'
    path_test = '/home/vjachesalv/Performance_lab/task_3/fixture/tests.json'
    result = task3(path_value, path_test)
    with open(
            '/home/vjachesalv/Performance_lab/task_3/fixture/result.json',
            'rb'
    ) as f:
        test_json = json.dumps(json.load(f), indent=4)
    assert result == test_json


test_parse_json()
