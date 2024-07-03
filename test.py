from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome to the Vulnerable XSS App</h1>
        <form method="GET" action="/search">
            <input type="text" name="query" placeholder="Search...">
            <input type="submit" value="Search">
        </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('query')
    return f'<h2>Search Results for: {query}</h2>'

if __name__ == '__main__':
    app.run(debug=True)
