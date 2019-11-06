# -*- coding: utf-8 -*-
import logging
import os
import signal
import subprocess
import threading
import traceback

from bson import ObjectId

from flask import Flask, jsonify, request

from pymongo import MongoClient

from .json import MongoDBJSONEncoder

logger = logging.getLogger('app')

app = Flask(__name__)
app.json_encoder = MongoDBJSONEncoder


def mongodb_dsn():
    """
    Returns the DSN string for connecting with MongoDB
    """
    return os.environ.get('POSTGRES_DSN', 'mongodb://localhost:27017/db')


def get_db():
    return MongoClient(
        mongodb_dsn(),
    )['db']


def get_collection(col):
    db = get_db()
    return db[col]


class MongoDBOnDemand:
    """
    Watches a MongoDB instances and kills the server when MongoDB dies.
    """

    def __init__(self, mongodb_proc: subprocess.Popen):
        self.mongodb_proc = mongodb_proc

    def wait(self):
        self.mongodb_proc.wait()

        logger.error('MongoDB has exited!')

        # Exit as soon as the redis server crashes.
        # Note: sys.exit() will not work here.
        os.kill(os.getpid(), signal.SIGINT)


def with_object_ids(obj):
    """
    Allows the user to use _id for queries.
    """
    if not isinstance(obj, dict):
        return obj
    for k, v in obj.items():
        if k == "_id":
            obj[k] = ObjectId(v)
        else:
            obj[k] = with_object_ids(v)
    return obj


@app.route('/insertOne', methods=['post'])
def insertOne():
    req = request.json
    col_name = req['collection']
    value = req['value']
    col = get_collection(col_name)
    res = col.insert_one(value)
    return jsonify({
        "insertedId": res.inserted_id,
        "acknowledged": res.acknowledged,
    })


@app.route('/insertMany', methods=['post'])
def insertMany():
    req = request.json
    col_name = req['collection']
    values = req['values']
    col = get_collection(col_name)
    res = col.insert_many(values)
    return jsonify({
        "insertedIds": res.inserted_ids,
        "acknowledged": res.acknowledged,
    })


@app.route('/findOne', methods=['post'])
def findOne():
    req = request.json
    col_name = req['collection']
    value = with_object_ids(req['query'])
    col = get_collection(col_name)
    return jsonify(col.find_one(value))


@app.route('/findMany', methods=['post'])
def findMany():
    req = request.json
    col_name = req['collection']
    value = with_object_ids(req['query'])
    col = get_collection(col_name)
    res = col.find(value)
    return jsonify([*res])


@app.route('/countDocuments', methods=['post'])
def countDocuments():
    req = request.json
    col_name = req['collection']
    query = with_object_ids(req['query'])
    col = get_collection(col_name)
    return str(col.count_documents(query))


def update_result(res):
    upserted_id = res.upserted_id
    if isinstance(upserted_id, ObjectId):
        upserted_id = str(upserted_id)
    return jsonify({
        "matchedCount": res.matched_count,
        "modifiedCount": res.modified_count,
        "upsertedId": upserted_id,
        "acknowledged": res.acknowledged,
    })


@app.route('/updateOne', methods=['post'])
def updateOne():
    req = request.json
    col_name = req['collection']
    query = with_object_ids(req['query'])
    value = req['value']
    upsert = req.get('upsert', False)
    col = get_collection(col_name)
    res = col.update_one(query, value, upsert)
    return update_result(res)


@app.route('/updateMany', methods=['post'])
def updateMany():
    req = request.json
    col_name = req['collection']
    query = with_object_ids(req['query'])
    value = req['value']
    upsert = req.get('upsert', False)
    col = get_collection(col_name)
    res = col.update_many(query, value, upsert)
    return update_result(res)


@app.route('/deleteOne', methods=['post'])
def deleteOne():
    req = request.json
    col_name = req['collection']
    query = with_object_ids(req['query'])
    col = get_collection(col_name)
    res = col.delete_one(query)
    return jsonify({
        "deletedCount": res.deleted_count,
        "acknowledged": res.acknowledged,
    })


@app.route('/deleteMany', methods=['post'])
def deleteMany():
    req = request.json
    col_name = req['collection']
    query = with_object_ids(req['query'])
    col = get_collection(col_name)
    res = col.delete_many(query)
    return jsonify({
        "deletedCount": res.deleted_count,
        "acknowledged": res.acknowledged,
    })


@app.route('/dropCollection', methods=['post'])
def dropCollection():
    req = request.json
    col_name = req['collection']
    col = get_collection(col_name)
    return str(col.drop())


@app.route('/listCollections', methods=['get'])
def listCollections():
    return jsonify(get_db().list_collection_names())


@app.route('/health', methods=['get'])
def health():
    # check whether the server is alive
    return get_db().command("ping")


def app_error(e):
    logger.error(traceback.format_exc())
    return jsonify({'message': repr(e)}), 400


if __name__ == '__main__':
    # If no creds were provided -> spawn self-hosted instance
    if os.getenv('MONGODB_URI') is None:
        logger.warning('Starting self hosted mongodb server...')
        p = subprocess.Popen(['mongod', '--config=/app/mongod.conf'])
        server = MongoDBOnDemand(p)
        t = threading.Thread(target=server.wait, daemon=True)
        t.start()

    app.register_error_handler(Exception, app_error)
    app.run(host='0.0.0.0', port=8000)
