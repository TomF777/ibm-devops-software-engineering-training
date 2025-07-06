"""
HTTP Routes for HitCounter Service
"""
from flask_restx import Api, Resource, fields
from hitcounter import app

hits = 0

api = Api(
    app,
    version="0.0.1",
    title="Hit Counter Service",
    description="This is service counts the number of hits to a URL",
    doc="/",
)

ns = api.namespace("hits", description="HitCounter Service")

hits_model = api.model("Hits", {"counter": fields.Integer})


@ns.route("/", strict_slashes=False)
class HitCounter(Resource):
    """Counts the number of hits"""

    @ns.doc("get_hits")
    @ns.marshal_with(hits_model)
    def get(self):
        """returns the current hit count"""
        # global hits
        return {"counter": hits}, 200

    @ns.doc("increment_hits")
    @ns.response(200, "Counter incremented successfully")
    def put(self):
        """increments the counter by 1"""
        global hits
        hits += 1
        return {"counter": hits}, 200
