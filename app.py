from chalice import Chalice

app = Chalice(app_name='chalice-testing')


@app.route('/')
def index():
    text = 'Hello World!'
    return text

