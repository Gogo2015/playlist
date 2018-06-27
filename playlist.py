from flask import Flask, render_template, redirect, request
app = Flask(__name__)

the_tweets = []
@app.route("/")
def welcome(name=None):
	return render_template('welcome.html', name=name)

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/faillogin')
def faillogin():
	return render_template('faillogin.html')
@app.route('/composetweet')
def composetweet():
	return render_template('composetweet.html')


@app.route("/submit", methods=["POST"])
def submit():
	username = request.form.get("admin")
	password = request.form.get("password")
	if username == 'admin' and password == 'password':
		return redirect("/composetweet")
	else:
		print ("Incorrect Login")
		return redirect("/faillogin")
@app.route("/index")
def index():
	return render_template("index.html")


@app.route("/view")
def view():
	return render_template("view.html", tweets=the_tweets)

def add_tweet(tweet):

	print(tweet)
	the_tweets.append(tweet)

@app.route("/submit_tweet", methods=["POST"])
def submit_tweet():
	tweet = request.form.get("tweet")
	add_tweet(tweet)
	return redirect("/view")


print("Starting Application")
app.run(debug=True)
