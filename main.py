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

        return redirect("/carousel/"+str(name.split("/")[-1]).replace("?","*@").replace("=","^()"))
    return render_template('index.html', names=names, form=form, message=message)

import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

@app.route('/carousel/<url>',methods=['GET','POST'])
def carousel(url):
    import os
    import shutil
    import glob
    from pytube import YouTube
    # misc
    import os
    import shutil
    import math
    import datetime
    # plots
    from frame_extractor import FrameExtractor
    # image operation
    import cv2
    print(url)
    # url=url.replace("*-*!","/")
    if "watch" in url:
        new_url=url.replace("*@","?").replace("^()","=")
        new_url="https://www.youtube.com/"+new_url
    else:
        new_url="https://www.youtu.be/"+url
    url=new_url
    print(url)


    return_images=[]
    #
    yt = YouTube(url)
    yt.streams.filter(progressive=True).order_by('resolution')[-1].download("static/videos/")
    name_video=yt.title+"."+yt.streams.filter(progressive=True).order_by('resolution')[-1].mime_type.split("/")[-1]
    fe= FrameExtractor("static/videos/"+name_video)
    fps=fe.fps
    title=yt.title
    clear_title=''.join(e for e in yt.title if e.isalnum())
    fe.get_n_images(every_x_frame=fps*2)
    # finding output directory
    fe.extract_frames(every_x_frame=fps*2,
                  img_name='a_',
                  dest_path='static/'+clear_title)
    # dir = os.path.join('static/', yt.title)
    dir="static/"+clear_title
    dir_im=os.path.join(app.static_folder, clear_title)
    print(dir)
    # hj()
    # dir="static/imgs/"
    images=glob.glob(dir+"/*")
    images.sort(key=natural_keys)
    print(images)
    for im in images:
        # return_images.append("/static/imgs/"+im.split("\\")[-1])
        # return_images.append(dir_im+im.split("\\")[-1])
        return_images.append("/"+dir+"/"+im.split("\\")[-1])

    # return_images.append(url)
    # images=glob.glob("static/imgs/*")

    # images=['./ugSeauWEAEDVpx.jpg', './dice.jpg', './random.jpg']
    print(return_images)
    return render_template('carousel.html',images=return_images)
