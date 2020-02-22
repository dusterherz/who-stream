from flask_restx import Namespace, Resource

api = Namespace('is_live', description='Live operation')


@api.route('/')
@api.response(204, "Ok.")
class IsLive(Resource):
    @api.doc('is_live')
    def get(self):
        ''' Check if Mister MV is live '''
        return '', 204
