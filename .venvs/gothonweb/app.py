#注释为练习50内容
##双注释为51内容
from flask import Flask,session,redirect,url_for,escape,request
from flask import render_template
from flask import request
from gothonweb import planisphere

app = Flask(__name__)

@app.route('/')
def index():
    #this is used to "setup" the session with starting value
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))

##@app.route('/hello')
#@app.route("/hello",methods=['POST','GET'])
@app.route("/game",methods=['POST','GET'])
def game():
    #str1 = " Hello， World123"
    #return render_template("index.html",greeting=str1)
    ##greet = "Hello"
    ##hello = "ZhiTao."   
    ##name = request.args.get('greet','hello')
    ##if name:
    ##    greeting = f'{greet}, {hello}'
    ##else:
    ##    greeting = "Hello world!"  
    ##return render_template("index.html",greeting = greeting)
    
    #greeting = "Hello World!"
    #if request.method == "POST":
    #    name = request.form['name']
    #    greet = request.form['greet']
    #    greeting = f'{greet},{name}'
    #    return render_template("index.html",greeting = greeting)
    #else:
        #return render_template("hello_form.html")
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html",room=room)
        else:
            #why is there here?do you need it?
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room
            else:
                session['room_name'] = planisphere.name_room
        return redirect(url_for("game"))

#YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'A0Zr98j/3yX r~xhh!jmN]lwx,?rt'

if __name__ == "__main__":
    app.run()