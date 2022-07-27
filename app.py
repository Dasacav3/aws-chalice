from chalice import Chalice

app = Chalice(app_name='chalice_testing')


@app.route('/')
def index():
    return Response('''
    Welcome to Chalice REST API.
    ''', status_code=200)
