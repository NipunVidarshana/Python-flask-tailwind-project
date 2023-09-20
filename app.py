from flask import Flask, render_template,request

app = Flask(__name__)



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

