from bson import json_util, ObjectId

from flask.json import JSONEncoder


class MongoDBJSONEncoder(JSONEncoder):
    """
    Allows to JSON-serialize objects with Mongo object ids.
    """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json_util.default(o,
                                 json_options=json_util.RELAXED_JSON_OPTIONS)
