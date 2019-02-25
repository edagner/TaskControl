from app import db, ma
from datetime import datetime
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


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
    step_end = db.Column(db.DateTime, nullable=True, onupdate=datetime.utcnow)
    completed = db.Column(db.Integer, nullable=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)

    def __repr__(self):
        return '<TaskStep: {}, TaskStart: {}, TaskParentId: {}>'.format(self.step_name, self.step_start, self.task_id)


# these dictate which fields will be returned when a get command is invoked on resource
class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id", "task_name")


class TaskStepSchema(ma.Schema):
    class Meta:
        fields = ("id", "task_id", "step_name", "step_start", "step_end", "completed")

