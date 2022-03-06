from django.urls import reverse
import json


def get_and_return_json_response(client, endpoint):
    response = client.get(reverse(endpoint))
    return response, json.loads(response.content)
