from flask_restx import Namespace, Resource

api = Namespace('is_live', description='Live operation')


@api.route('/')
@api.response(204, "Ok.")
class IsLive(Resource):
    def get(self):
        ''' Check if Mister MV is live '''
        return api.response(204)
