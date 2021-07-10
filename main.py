from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('Please Enter URL below?', validators=[DataRequired()])
    submit = SubmitField('Submit')
def get_id(ACTORS,name):
    for i in range(len(ACTORS)):
        if name==ACTORS[i]:
            return i

#
# def actor(ACTORS,id=0):
#     return "actor/"+str(ACTOTS[id])

@app.route('/', methods=['GET', 'POST'])
def index():
    names = ['ali','zafar','jameel','hukkah']
    ACTORS=['ali','zafar','jameel','hukkah']
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            # empty the form field
            form.name.data = ""
            id = get_id(ACTORS, name)
            # redirect the browser to another route and template
            # print(url_for('actor', id=id) )
            # hj()
            return redirect("/carousel/")
        else:
            message = "That actor is not in our database."
    return render_template('index.html', names=names, form=form, message=message)



@app.route('/carousel/',methods=['GET','POST'])
def carousel():
    import os
    import shutil
    import glob
    dir = os.path.join(app.static_folder, "imgs")
    # print(dir)
    # if os.path.exists(dir):
    #     shutil.rmtree(dir)
    # os.makedirs(dir)
    # ruta_imagenes = glob.glob("./*.jpg")
    images=glob.glob(dir+"/*")
    # images=glob.glob("static/imgs/*")

    # images=['./ugSeauWEAEDVpx.jpg', './dice.jpg', './random.jpg']
    print(images)
    return render_template('carousel.html',images=images)
