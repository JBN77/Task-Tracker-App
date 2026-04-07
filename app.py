from flask import Flask, render_template, request, redirect, url_for
from models import Task, Habit, DeadlineTask
from manager import ItemManager

app = Flask(__name__)
manager = ItemManager()


@app.route("/")
def index():
    items = manager.get_all_items()
    return render_template("index.html", items=items)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        item_type = request.form.get("type")
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip() 

        if not title:
            return render_template("create.html", error="Title is required.")

        if item_type == "task":
            priority = request.form.get("priority", "Medium")
            item = Task(title, description, priority)

        elif item_type == "habit":
            item = Habit(title, description)

        elif item_type == "deadline":
            due_date = request.form.get("due_date", "")
            item = DeadlineTask(title, description, due_date)

        else:
            return render_template("create.html", error="Invalid item type.")

        manager.add_item(item)
        return redirect(url_for("index"))

    return render_template("create.html")


@app.route("/complete/<int:index>")
def complete(index):
    manager.mark_item_complete(index)
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    manager.delete_item(index)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)