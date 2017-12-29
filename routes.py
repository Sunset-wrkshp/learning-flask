from flask import Flask, render_template, request, url_for
import os
from models import db, User
from forms import SignupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)

app.secret_key = "development-key"

#URL CSS thing
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/form')
def student():
   return render_template('form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route("/signup", methods = ['POST', 'GET'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            #newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            #db.session.add(newuser)
            #db.session.commit()
            return "Success"
    elif request.method == 'GET':
        return render_template('signup.html', form = form )

if __name__ == "__main__":
    app.run(debug=True)
