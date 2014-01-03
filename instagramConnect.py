from instagram.client import InstagramAPI


client_id = '54e559fad6dc4baf86127cc8baa9a0dd'
client_secret = 'ee8bb41e2f434f32934db68e379d7b91'
redirect_uri = 'http://localhost'
callback_url = 'http://myhost.com/test/start.php'

api = InstagramAPI(client_id=client_id, client_secret=client_secret)

tag = 'occupynigeria'
api.create_subscription(object='tag', object_id=tag, aspect='media', callback_url=callback_url)

access_token = 'MY ACCESS TOKEN'
api = InstagramAPI(access_token=access_token)



new_api = client.InstagramAPI(client_id='', client_secret='', redirect_uri='http://ontodjangoyo.herokuapp.com/oauth_callback')

new_api.create_subscription(object='tag', object_id='ed', aspect='media', callback_url='http://ontodjangoyo.herokuapp.com/instag/realtime_callback/')

api.create_subscription(object='tag', object_id='fox', aspect='media', callback_url='http://mydomain.com/hook/instagram')

api.create_subscription(object='location', object_id='1257285', aspect='media', callback_url='http://mydomain.com/hook/instagram')

api.create_subscription(object='geography', lat=35.657872, lng=139.70232, radius=1000, aspect='media', callback_url='http://mydomain.com/hook/instagram')


reactor = subscriptions.SubscriptionsReactor()
reactor.register_callback(subscriptions.SubscriptionType.USER, process_user_update)

api.list_subscriptions()
api.delete_subscriptions(id=342342)



