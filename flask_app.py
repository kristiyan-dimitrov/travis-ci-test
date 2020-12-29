from flask import Flask # For Flask app; This class is used to create an instance of WSGI
from flask import request # Used to accept data from the web app (i.e. the user)
from flask import render_template # Used to render an HTML template
from flask import url_for # Used to get the url for a specific function # Docs: https://flask.palletsprojects.com/en/1.1.x/api/#flask.url_for
from werkzeug.utils import secure_filename # Used for uploading a file

app = Flask(__name__
			, static_folder='static' # Specify location of static files for CSS
			, template_folder="templates") # Specify location of HTML templates

@app.route('/')
def hello_world():
    return 'Hello, World! This is my first Flask App!'

# Need to add methods=['POST'] so you can accept data
# Need to add methods=['GET'] so you can access the page through the browser
@app.route('/add', methods=['GET','POST']) 
def addition():

	'''
	The <form> tag in the HTML template has this:

		 action="{{ url_for('addition') }}" # Docs for url_for function: https://flask.palletsprojects.com/en/1.1.x/api/#flask.url_for

	It specifies where to send the form-data when a form is submitted.

	In general, it appears that variables passed in from Python are encapsulated in {{}}
	'''

	if request.form.get('x') and request.form.get('y'):
		
		x = request.form['x']
		y = request.form['y']
		result = str(int(x) + int(y)) # It appears that forms take input as strings and output is also expected as string;
		# More specifically, if I don't wrap the return in str() I get error: "The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a int."
	
		return render_template('index.html', result=result) 
		
	return render_template('index.html')


# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
'''
You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. 
Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

This is very powerful! E.g. you can have a product page, which takes in URL parameters for the specific product_id you want to display
'''
@app.route('/display_number/<number>')
def display_number(number):
	return number


#######################
# UNDER CONSTRUCTION ##
#######################


# UPLOADING FILES

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))

    return "Waiting for file upload"
