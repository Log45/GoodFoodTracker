from flask import Flask, render_template
import os
from datetime import datetime
import time

app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER


while True:
    day_number = int(datetime.now().strftime("%w"))
    hour = int(datetime.now().strftime("%H"))

    @app.route("/")
    def home_page():
        full_filename = os.path.join(app.config["UPLOAD_FOLDER"], 'goodfood.jpg')
        return render_template("index.html", user_image=full_filename)

    @app.route("/tandoor")
    def tandoor():
        if day_number == 1:
            if hour >= 11 and hour < 14:
                print("Crossroads")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'crossroads.png')
            elif hour >= 16 and hour < 19:
                print("RITz")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'ritz.png')
            else:
                print("Closed")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 2:
            if hour >= 11 and hour > 14:
                print("RITz")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'ritz.png')
            elif hour >= 16 and hour < 19:
                print("Crossroads")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'crossroads.png')
            else:
                print("Closed")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 4:
            if hour >= 11 and hour < 14:
                print("BCC")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'bcc.png')
            else:
                print("Closed")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        else:
            print("Closed")
            map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        return render_template("tandoor.html", tandoor_map=map)

    @app.route("/sushi")
    def sushi():
        if day_number == 1:
            if hour >= 16 and hour < 19:
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            else:
                print("Closed")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 3:
            if hour >= 11 and hour < 14:
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            else:
                print("Closed")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 5:
            if hour >= 11 and hour < 14:
                print("BCC")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'bcc.png')
            else:
                print("Closed")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        else:
            print("Closed")
            map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        return render_template("sushi.html", sushi_map=map)

    @app.route("/lowandslow")
    def lowslow():
        "Low and Slow Schedule"
        if day_number == 2:
            if hour >= 16 and hour < 19:
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 3:
            if hour >= 16 and hour < 19:
                print("Crossroads")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'crossroads.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 5:
            if hour >= 11 and hour < 14:
                print("RITz")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'ritz.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        else:
            print("Closed :(")
            map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        return render_template("slow.html", slow_map=map)

    @app.route("/revolution")
    def revolution():
        if day_number == 2:
            if hour >= 11 and hour < 14:
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            elif hour >= 16 and hour < 19:
                print("RITz")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'ritz.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 3:
            if hour >= 16 and hour < 19:
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            else:
                print("Closed")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 6:
            if (hour >= 11 and hour < 14) or (hour >= 16 and hour < 19):
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            else:
                print("Closed")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 7:
            if hour >= 16 and hour < 19:
                print("Crossroads")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'crossroads.png')
            else:
                print("Closed")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        else:
            print("Closed")
            map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        return render_template("revolution.html", rev_map=map)

    @app.route("/phouse")
    def phouse():
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
        return render_template("map.html", user_image=map)
    
    @app.route("/mangu")
    def mangu():
        if day_number == 1:
        #This is Monday
            if hour >= 11 and hour < 14:
                print("BCC")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'bcc.png')
            elif hour >= 16 and hour < 19:
                print("Crossroads")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'crossroads.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 3:
            if hour >= 11 and hour < 14:
                print("RITz")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'ritz.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 4:
            if hour >= 16 and hour < 19:
                print("RITz")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'ritz.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 5:
            if hour>= 11 and hour < 14:
                print("Crossroads")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'crossroads.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        else:
            print("Closed :(")
            map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png') 
        return render_template("mangu.html", mangu_map=map)

    @app.route("/chicken")
    def chicken():
        if day_number == 1:
        #This is Monday
            if hour >= 16 and hour < 19:
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 2:
            if hour >= 11 and hour < 14:
                print("BCC")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'bcc.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 3:
            if hour >= 11 and hour < 14:
                print("Crossroads")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'crossroads.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 4:
            if hour >= 11 and hour < 14:
                print("RITz")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'ritz.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 5:
            if hour >= 11 and hour < 14:
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        else:
            print("Closed :(")
            map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        return render_template("chicken.html", chicken_map=map)

    @app.route("/macarollin")
    def macarollin():
        "Macarollin Schedule"
        if day_number == 4:
            if hour >= 11 and hour < 14:
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        elif day_number == 7:
            if hour >= 16 and hour < 19:
                print("Commons")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'commons.png')
            else:
                print("Closed :(")
                map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        else:
            print("Closed :(")
            map = os.path.join(app.config['UPLOAD_FOLDER'], 'closed.png')
        return render_template("macarollin.html", mac_map=map)

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080)
