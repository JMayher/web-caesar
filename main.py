from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form action = "/add" method = "post">
        Rotate by:<input type="text" name ="rot" value = 0 />
        <textarea name="text">{0}</textarea>
        <input type="submit" value = "Submit Query"/>
    </form>
    </body>
</html>


"""


@app.route("/")
def index():
    return form.format("")
@app.route("/add", methods = ['POST'])
def encrpyt():
    rot1 = request.form["rot"]
    rot1 = int(rot1)
    text1 = request.form["text"] 
    rotated = rotate_string(text1, rot1)
    return form.format(rotate_string(text1, rot1))



app.run()