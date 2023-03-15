from flask import Flask, render_template

from task_one import do_task_one
from task_two import do_task_two


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/task_one")
def call_task_one():
    return render_template("one.html", emp_data=do_task_one())


@app.route("/task_two")
def call_task_two():
    return render_template("two.html", get_data=do_task_two())


if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)