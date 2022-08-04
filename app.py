import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# In terminal use the following command to set env variable
# export APP_COLOR=powderblue
color = os.environ.get("APP_COLOR")


@app.route('/')
def hello_world():
    print(color)
    return render_template("./index.html", color=color)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
