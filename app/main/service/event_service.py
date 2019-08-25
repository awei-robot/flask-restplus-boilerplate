from flask import request
from app.main import db, celery
from app.main.model.event import Events
from app.main.service.auth_helper import Auth


@celery.task
def save_events(event_data):
    event = Events(
        user_pid=event_data['user_pid'],
        request_path=event_data['request_path'],
        request_data=event_data['request_data'],
        request_method=event_data['request_method'],
        response_status=event_data['response_status'],
        response_data=event_data['response_data']

    )
    db.session.add(event)
    db.session.commit()


