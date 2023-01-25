from requests import Response

from utils import create_user, add_habit_for_user, generate_graph_id, record_data_in_habit, get_data


def test_create_user_successful(mocker, capsys):
    # success case
    res = Response()
    res.status_code = 200
    res._content = b'{ "message" : "true" }'

    mocker.patch("requests.post", return_value=res)

    create_user(["create", "mock"])
    captured = capsys.readouterr()
    assert "User created successfully" in captured.out


def test_create_user_failure(mocker, capsys):

    res = Response()
    res.status_code = 400
    res._content = b'{ "message" : "true" }'

    mocker.patch("requests.post", return_value=res)

    create_user(["create", "mock"])
    captured = capsys.readouterr()
    assert "Try again!" in captured.out


def test_add_habit_for_user_successful(mocker, capsys):
    # success case

    res = Response()
    res.status_code = 200
    res._content = b'{ "message" : "true" }'

    mocker.patch("requests.post", return_value=res)

    add_habit_for_user(["create", "mock", "habit"])
    captured = capsys.readouterr()
    assert "Graph created successfully" in captured.out


def test_add_habit_for_user_failure(mocker, capsys):
    # failure case

    res = Response()
    res.status_code = 400
    res._content = b'{ "message" : "true" }'

    mocker.patch("requests.post", return_value=res)

    add_habit_for_user(["create", "mock", "habit"])
    captured = capsys.readouterr()
    assert "Try again!" in captured.out


# def test_generate_graph_id():
#     username = "pooja"
#     habit = "habit1"
#
#     result = generate_graph_id(username, habit)
#
#     assert result == f"{username}-{habit}"[0:16]


def test_record_data_in_habit_successfully(mocker, capsys):
    # success

    res = Response()
    res.status_code = 200
    res._content = b'{ "message" : "true" }'

    mocker.patch("requests.post", return_value=res)

    record_data_in_habit(["create", "mock", "habit", "20012023"])
    captured = capsys.readouterr()
    assert "Entry added in habit graph" in captured.out


def test_record_data_in_habit_failure(mocker, capsys):
    # failure

    res = Response()
    res.status_code = 400
    res._content = b'{ "message" : "true" }'

    mocker.patch("requests.post", return_value=res)

    record_data_in_habit(["create", "mock", "habit", "20012023"])
    captured = capsys.readouterr()
    assert "Try again!" in captured.out


def test_get_data(mocker, capsys):

    mocker.patch("utils.generate_graph_id", return_value="gid")

    get_data(["create", "mock", "habit"])
    captured = capsys.readouterr()

    assert f"https://pixe.la/v1/users/mock/graphs/gid.html" in captured.out
