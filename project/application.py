from sanic import Sanic
from sanic.response import json

app = Sanic()

payload = {
    "resources": [
        {
            "endpoint": "v1/start",
            "method": "GET",
            "response_status": 200,
            "response": {"hello": "worldo"},
        },
        {
            "endpoint": "v1/begin",
            "method": "GET",
            "response_status": 200,
            "response": {"banana": "monkey"},
        }
    ]
}


def handle_request(request, path, json_payload: dict):
    resources = json_payload["resources"]
    for resource in resources:
        if path == resource["endpoint"] and request.method == resource["method"]:
            return json(resource["response"], resource["response_status"])
    return json({'message': 'path not found'}, 404)


@app.route('/<path:path>', methods=["POST", "GET", "PATCH", "DELETE", "PUT", "OPTIONS"])
async def test(request, path):
    return handle_request(request, path, payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
