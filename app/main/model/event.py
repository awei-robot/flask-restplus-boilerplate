from app.main import db
import datetime


class Events (db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_pid = db.Column(db.String(100))
    request_path = db.Column(db.String(100))
    request_data = db.Column(db.String(500))
    request_method = db.Column(db.String(100))
    response_status = db.Column(db.String(100))
    response_data = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Events '{}'>".format(self.id)
