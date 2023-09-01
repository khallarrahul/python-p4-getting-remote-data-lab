import requests
import json


class GetRequester:
    def __init__(
        self,
        url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json",
    ):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        message_list = []
        messages = json.loads(self.get_response_body())
        for message in messages:
            message_list.append(message)
        return message_list
