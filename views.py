from flask import Flask, request, render_template, redirect
app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")
	

@app.route("/show_length/", methods= ["POST"])
def show_length():
	if request.method == "POST":
		words = request.form["text-box"]
		word_length = len(words.split())
		return "<h2>Words: </h2> " + words + "<p>Length: </p>" + str(word_length)


if __name__ == '__main__':
	app.run(debug= True)