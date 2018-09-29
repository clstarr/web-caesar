from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """ <!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- 
      Now, fill out the body of the HTML string with a form that has these characteristics:

The form uses the POST method.
There are two inputs: a regular input with type="text" and a textarea.
Set name="rot" on the input element and name="text" on the textarea.
Has a label on the input element that looks something like the one in the screenshot above.
The input element has the default value of 0.
Has a submit button.
In the index function, return the form variable.-->
<form method="post">
<label for="rot"> Rotate by: </label>
<input type="text" name="rot" value="0">
<textarea name="text">
{}
</textarea>
<input type="submit">
</form>

    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot=int(request.form["rot"])
    text=request.form["text"]
    encrypted=rotate_string(text, rot)

    return form.format(encrypted)


app.run()