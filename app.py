from flask import Flask
from datetime import datetime
import re
from flask import jsonify

app = Flask(__name__)

def read_userfile(fname):
    file_users = open(fname,'r', encoding = 'utf-8')
    lines = file_users.readlines()
    users = []
    inst_key_word ="s profile picture"
    special_char ="'"
    for line in lines:
        if(inst_key_word in line):
            trimmed_line = line.replace(special_char +'s profile picture','')
            users.append(trimmed_line.rstrip('\n'))
    return users


@app.route("/")
def home():
    followers = read_userfile('followers.txt')
    followings = read_userfile('followings.txt')
    not_follow_you_back = []
    not_follow_you_back = [x for x in followings if x not in followers]
    return jsonify(not_follow_you_back)
    

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # restrict to safe characters only
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    
    content = "Hello there, " + clean_name + "! It is " + formatted_now
    return content