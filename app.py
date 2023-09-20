from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/add/comment")
def addComment():
	return render_template("addComment.html")

@app.route("/show/comments", methods=('GET', 'POST'))
def showComments():
	if request.method == 'POST':
		 email = request.form['email']
		 content = request.form['comment']
		 print(email)
	return render_template("showComments.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/services")
def services():
	return render_template("services.html")

@app.route("/contact")
def comments():
	return render_template("contacts.html")

if __name__ == '__main__':
	app.run(debug=True)