```python
from flask import Flask, render_template

# create a new Flask app
app = Flask(__name__)

# define a route and function to handle the request
@app.route('/main.py')
def index():
    # render the HTML file using the Jinja templating engine
   return render_template('main.py')

# start the app
if __name__ == '__main__':
    app.run(debug=True)
