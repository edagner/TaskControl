from flask import render_template, jsonify, request
from mysite import app, db
from mysite.task_orm import Task, TaskStep, TaskSchema, TaskStepSchema

task_schema = TaskSchema(strict=True)
tasks_schema = TaskSchema(many=True, strict=True)
taskstep_schema = TaskStepSchema(strict=True)
tasksteps_schema = TaskStepSchema(many=True, strict=True)


@app.route("/view", methods=["GET"])
def home():
    tasks = Task.query.all()
    return tasks_schema.jsonify(tasks)
    # return render_template("home.html", title="Home")


# TASKS
@app.route("/tasks", methods=["GET", "POST"])
def get_add_tasks():
    if request.method == "GET":
        tasks = Task.query.all()
        return tasks_schema.jsonify(tasks)
    elif request.method == "POST":
        task_n = request.json['task_name']
        task = Task(task_name=task_n)
        db.session.add(task)
        db.session.commit()
        return task_schema.jsonify(task)


@app.route("/task/<tid>", methods=["GET", "PUT", "DELETE"])
def get_one_task(tid):
    if request.method == "GET":
        task = Task.query.get(tid)
        return task_schema.jsonify(task)
    elif request.method == "PUT":
        new_name = request.json['task_name']
        task = Task.query.get(tid)
        task.task_name = new_name
        db.session.commit()
        return task_schema.jsonify(task)
    elif request.method == "DELETE":
        task = Task.query.get(tid)
        db.session.delete(task)
        db.session.commit()
        return "Task Resource was deleted"


# TASK STEPS
@app.route("/task_step/<tsid>", methods=["GET", "PUT", "DELETE"])
def get_update_specific_taskstep(tsid):
    if request.method == "GET":
        # view specific task
        task_step = TaskStep.query.filter_by(id=tsid).first()
        return taskstep_schema.jsonify(task_step)
    elif request.method == "PUT":
        # completes a task_step
        task_step = TaskStep.query.filter_by(id=tsid).first()
        task_step.completed = 1
        db.session.commit()
        return taskstep_schema.jsonify(task_step)
    elif request.method == "DELETE":
        task_step = TaskStep.query.filter_by(id=tsid).first()
        db.session.delete(task_step)
        db.session.commit()
        return "Resource was deleted", 401


@app.route("/task/<tid>/task_steps", methods=["GET"])
def get_all_tasksteps_for_task(tid):
    task_step = TaskStep.query.filter_by(task_id=tid).all()
    return tasksteps_schema.jsonify(task_step)


@app.route("/task_steps", methods=["GET", "POST"])
def add_get_tasksteps():
    if request.method == "GET":
        # view all task steps
        task_steps = TaskStep.query.all()
        return tasksteps_schema.jsonify(task_steps)
    elif request.method == "POST":
        # add new task_step
        step_n = request.json['step_name']
        tid = request.json['task_id']
        task_step = TaskStep(step_name=step_n, task_id=tid)
        db.session.add(task_step)
        db.session.commit()
        return taskstep_schema.jsonify(task_step)
