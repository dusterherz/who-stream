from flask_restx import Namespace, Resource
from settings import TWITCH_CLIENT_ID
from twitch import TwitchHelix

api = Namespace('is_live', description='Live operation')
twitch_client = TwitchHelix(client_id=TWITCH_CLIENT_ID)


@api.route('/')
@api.response(200, "Return if live is on")
class IsLive(Resource):
    @api.doc('is_live')
    def post(self):
        ''' Check if Mister MV is live '''
        streams = twitch_client.get_streams(user_ids="mistermv")
        try:
            next(streams)
        except StopIteration:
            return {'fulfillment_text': "Non, Mister MV n'est pas en stream."}, 200
        return {'fulfillment_text': "Oui, Mister MV est en ligne !"}, 200
