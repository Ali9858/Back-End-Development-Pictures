
from . import app
import os
import json
from flask import jsonify, request

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")

with open(json_url, encoding="utf-8") as file:
    data: list = json.load(file)


######################################################################
# RETURN HEALTH OF THE APP
######################################################################

@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200


######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################

@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################

@app.route("/picture", methods=["GET"])
def get_pictures():
    return jsonify(data), 200


######################################################################
# GET A PICTURE
######################################################################

@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    for picture in data:
        if picture["id"] == id:
            return jsonify(picture), 200

    return jsonify({"message": "picture not found"}), 404


######################################################################
# CREATE A PICTURE
######################################################################

@app.route("/picture", methods=["POST"])
def create_picture():
    picture_in = request.get_json()

    if not picture_in:
        return jsonify({"message": "Invalid input parameter"}), 422

    for picture in data:
        if picture_in["id"] == picture["id"]:
            return jsonify({
                "Message": (
                    f"picture with id {picture_in['id']} already present"
                )
            }), 302

    data.append(picture_in)

    return jsonify(picture_in), 201


######################################################################
# UPDATE A PICTURE
######################################################################

@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    picture_in = request.get_json()

    if not picture_in:
        return jsonify({"message": "Invalid input parameter"}), 422

    for index, picture in enumerate(data):
        if picture["id"] == id:
            data[index] = picture_in
            return jsonify(picture_in), 201

    return jsonify({"message": "picture not found"}), 404


######################################################################
# DELETE A PICTURE
######################################################################

@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    for picture in data:
        if picture["id"] == id:
            data.remove(picture)
            return "", 204

    return jsonify({"message": "picture not found"}), 404
