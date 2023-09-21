from flask import Flask, render_template,request,redirect,url_for,session

app = Flask(__name__)
app.secret_key = "qweac@2017"

myComments = [] #define array for store comments on the Memory

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/add/comment")
def addComment():
	return render_template("addComment.html")

@app.route("/show/comments", methods=['GET', 'POST'])
def showComments():
	if request.method == 'POST':
		#print(request.form)
		userEmail = request.form['email']#get values from form
		userContent = request.form['comment']#get values from form

		if request.form.get('storeMemory'):
			myComments.append((userEmail,userContent)) #Assiged values to myComments array. Store data until re run the application(Tempory)
			
		if request.form.get('storeDB'):
			print("stored on db") #Assiged values store on the DB permenetly

	return render_template("showComments.html" ,userFilledData = myComments)

@app.route("/redirectHome")
def redirectHome():
	return redirect(url_for("index"))

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/services")
def services():
	return render_template("services.html")

@app.route("/contact")
def comments():
	return render_template("contacts.html")


@app.route("/add/session/variable")
def addSession():
	return render_template("addSession.html")

@app.route("/add/session", methods=['POST'])
def addSessionPostMethod():
	sessionStoreParam = request.form['sessionStoreParam']#get values from form
	session["userParam"] =  sessionStoreParam #Store in the session storage.When browser close all data vanished from the session.
	return redirect(url_for("checkSession"))

@app.route("/show/session")
def checkSession():
	if "userParam" in session:
		userParam = session["userParam"] #get data form session. Access by the variable.
		return "<p>Session stored successfully. Stored parameter is below</p><h1>" + userParam +"</h1>"
	else:
		return "<p>Session parameter not stored or web browser closed and reopened.</p>"






if __name__ == '__main__':
	app.run(debug=True)

