from comics.tests.helpers import get_and_return_json_response


def test_health_gives_200(client):
    response, response_body = get_and_return_json_response(client, "health")

    assert response.status_code == 200
    assert response_body["message"] == "ok"
