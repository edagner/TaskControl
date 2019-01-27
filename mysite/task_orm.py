from mysite import db, ma
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(25), nullable=False)
    db.relationship('TaskStep', backref='parent', lazy=True)

    def __repr__(self):
        return '<TaskName: {}>'.format(self.task_name)


class TaskStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    step_name = db.Column(db.String(25), nullable=False)
    step_start = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    step_end = db.Column(db.DateTime, nullable=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)

    def __repr__(self):
        return '<TaskStep: {}, TaskStart: {}, TaskParentId: {}>'.format(self.step_name, self.step_start, self.task_id)


class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id", "task_name")


class TaskStepSchema(ma.Schema):
    class Meta:
        fields = ("id", "task_id", "step_name", "step_start", "step_end")

