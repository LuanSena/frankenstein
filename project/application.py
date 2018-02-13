from sanic import Sanic, response
from sanic.response import json

app = Sanic()

payload = {
    "resources": [
        {
            "endpoint": "v1/start",
            "response_status": 200,
            "response": {"hello": "worldo"},
        },
        {
            "endpoint": "v1/begin",
            "response_status": 200,
            "response": {"banana": "monkey"},
        }
    ]
}


@app.route('/<path:path>', methods=["POST", "GET"])
async def test(request, path, payload=payload):
    resources = payload["resources"]
    for resource in resources:
        if path == resource["endpoint"]:
            return json(resource["response"], resource["response_status"])
    return json({'message': 'path not found'}, 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
