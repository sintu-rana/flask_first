from flask import Flask, jsonify, request, session, redirect, url_for, escape, request
from flask import Flask, render_template
app = Flask(__name__)
from flask import request



# creating a Flask app

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})

@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):

	return jsonify({'data': num**2})


# driver function
if __name__ == '__main__':

	app.run(debug = True)
	


# ########## Text file ######

@app.route("/app/")
def index():
    return render_template('index.html')

@app.route('/getfile', methods=['GET','POST'])
def getfile():
    if request.method == 'POST':
        result = request.form['myfile']
    else:
        result = request.args.get['myfile']
    return result


############ Render the Html Page #####


@app.route('/welcome/')
def welcome():
   return render_template('home.html')



######################### Sessions ########


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/login/')
def login():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login/', methods=['GET', 'POST'])
def res():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout/')
def cms():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


#########################

 

@app.route('/sta/')
def sta():
    return render_template('sta.html')
 

