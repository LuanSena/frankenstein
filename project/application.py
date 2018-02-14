from sanic import Sanic
from sanic.response import json

app = Sanic()

payload = {
    "resources": [
        {
            "endpoint": "v1/start",
            "description": "bla bla bla bla bla bla bla",
            "method": "GET",
            "response_status": 200,
            "response": {"hello": "worldo"},
        },
        {
            "endpoint": "v1/begin",
            "description": "ble ble ble ble ble ble",
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
async def router(request, path):
    return handle_request(request, path, payload)


def sanic_server(server_port):
    app.run(host='0.0.0.0', port=server_port)


def render_doc():
    resources = payload["resources"]
    payload_data = str()
    for resource in resources:
        payload_data = payload_data + """
        <h1>{endpoint}</h1>
        <p>{method}</p>
        """.format(endpoint=resource["endpoint"], method=resource["method"])

    with open("./templates/documentation.html", 'r') as file:
        tmp = str(file.read())
    with open("result.html", "w") as nfile:
        nfile.write(tmp.format(payload_data))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', default=False, type=int, help="port to server")
    args = parser.parse_args()

    if args.server:
        sanic_server(args.server)
    else:
        render_doc()
