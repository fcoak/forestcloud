from bottle import Bottle, run, route, static_file,get,post,request,redirect
import sqlite3
conn = sqlite3.connect("fc.db")
c = conn.cursor()

_mates={}


app = Bottle()


def manageMates(action,parameters):
    if action =="newmate":
        if parameters["mate"]=="oak" and parameters["secret"]=="davinci2050":
            _mates[parameters["name"]]=parameters["password"]
        else:
            return "no so fast!"
    if action=="deletemate":
        _mates[parameters[0]].pop()
    if action=="checkmate":
        if _mates[parameters["name"]]==parameters["password"]:
            return True
        else:
            return False

def check_login(a,b):
    ans= manageMates("chekmate",{"name":a,"password":b})
    return ans

@app.route('/wellcome')
def login():
    return '''
    <a href="/static/html/fc.html">
    <img src="/static/img/forestcloud-logo.jpg" title="Forest Cloud" alt="Welcome to the Forest Cloud Berkeley" style="width: 80%;left: 10%;border: 0;">
    </a>
    '''


@app.route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        welcome="/mates/"+username
        redirect (welcome)
    else:
        return "<p>Login failed.</p>"

@app.route('/sendtree', method='POST')
def do_login():
    specie = request.forms.get('sp')
    latitude = request.forms.get('lat')
    longitude = request.forms.get('lon')
    altitude = request.forms.get('alt')
    mate = request.forms.get('mate')
    txt = "gracias " + mate +" your tree has been recorded as follows:\n"
    txt += "specie : "+ specie +"\n"
    txt += "longitude : "+ longitude +"\n"
    txt += "latitude : "+ latitude +"\n"
    txt += "altitude : "+ altitude +"\n"
    return txt


@app.route('/hello')
def hello():  
    return "Hello Mates!"


@app.route('/mates/<name>')
def showMate(name):
    return "hello " + name

@app.route('/trees')
def showTrees():
    return str(trees)




@app.route("/static/<filename:path>")
def server_static(filename):
     return static_file(filename, root='/Users/koldobika/DV/github/forestcloud/static/')


run(app, host='0.0.0.0', port=8090, debug=True)
