from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html") # must be in a file called templates

@app.route('/about/')
def about():
  return render_template("about.html") # must be in a file called templates

if __name__=="__main__":
  app.run(debug=True)
