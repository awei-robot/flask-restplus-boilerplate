from flask import request

from app.main import db
from app.main.model.event import Events
from app.main.service.auth_helper import Auth


def save_events(event_data):
    data, status = Auth.get_logged_in_user(request)
    if status == 200:
        user_public_id = data['data']['public_id']
    else:
        user_public_id = ''
    event = Events(
        user_pid=user_public_id,
        request_path=event_data['request_path'],
        request_data=event_data['request_data'],
        request_method=event_data['request_method'],
        response_status=event_data['response_status'],
        response_data=event_data['response_data']

    )
    db.session.add(event)
    db.session.commit()


