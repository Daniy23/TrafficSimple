import flask
from flask.json import jsonify
import uuid
from traffic2 import Street, Car

games = {}

app = flask.Flask(__name__)


@app.route("/games", methods=["POST"])
def create():
    global games
    id = str(uuid.uuid4())
    games[id] = Street()
    cars = []
    for ghost in games[id].schedule.agents:
        cars.append({"id": ghost.unique_id, "x": int(ghost.pos[0]), "z": int(ghost.pos[1]), "degrees": int(ghost.diagonalPos)})

    #response = flask.make_response()
    #response.headers['Location'] = f"/games/{id}"
    #response.status_code = 201
    #response.data = jsonify(lista)
    #return response
    return jsonify({"cars": cars, 'location': f"/games/{id}"}), 201, {'location': f"/games/{id}"}

@app.route("/games/<id>", methods=["GET"])
def queryState(id):
    global model
    model = games[id]
    model.step()
    lista = []
    for ghost in model.schedule.agents:
       lista.append({"id": ghost.unique_id, "x": int(ghost.pos[0]), "z": int(ghost.pos[1]), "degrees": int(ghost.diagonalPos)})
    return jsonify({"cars": lista})

app.run()
