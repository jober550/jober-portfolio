from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/projects/novareels")
def project_novareels():
    return render_template("project_novareels.html")

@app.route("/projects/sol-advanced-ai")
def project_sol():
    return render_template("project_sol.html")

@app.route("/projects/music")
def project_music():
    return render_template("project_music.html")

if __name__ == "__main__":
    app.run(debug=True)

#this is a test