from flask import Flask

from task_one import do_task_one
from task_two import do_task_two


app = Flask(__name__)


@app.route("/")
def welcome():
    return "<h1> Hello, Welcome to HRConnect Project </h1>"


@app.route("/one")
def call_task_one():
    return do_task_one()


@app.route("/two")
def call_task_two():
    return do_task_two()


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)