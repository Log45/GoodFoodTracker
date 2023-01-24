from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

day_number = int(datetime.now().strftime("%w"))
hour = int(datetime.now().strftime("%H"))


if day_number == 1:
    #This is Monday
    if hour >= 11 and hour < 14:
        print("RITz")
        map = os.path.join(app.config['UPLOAD_FOLDER'], 'ritz.png')
    else:
        print("Closed :(")
        map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
elif day_number == 2:
    if hour >= 11 and hour < 14:
        print("Crossroads")
        map = os.path.join(app.config['UPLOAD_FOLDER'], 'crossroads.png')
    else:
        print("Closed :(")
        map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
elif day_number == 3:
    if hour >= 11 and hour < 14:
        print("BCC")
        map = os.path.join(app.config['UPLOAD_FOLDER'], 'bcc.png')
    elif hour >= 16 and hour < 19:
        print("RITz")
        map = os.path.join(app.config['UPLOAD_FOLDER'], 'ritz.png')
    else:
        print("Closed :(")
        map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
elif day_number == 4:
    if hour >= 16 and hour < 19:
        print("Crossroads")
        map = os.path.join(app.config['UPLOAD_FOLDER'], 'crossroads.png')
    else:
        print("Closed :(")
        map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
else:
    print("Closed :(")
    map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
    
@app.route("/")
def home_page():
    full_filename = os.path.join(app.config["UPLOAD_FOLDER"], 'goodfood.jpg')
    return render_template("index.html", user_image=full_filename)

@app.route("/where")
def where():
    return render_template("map.html", user_image=map)

if __name__ == '__main__':
    app.run(debug=True)


