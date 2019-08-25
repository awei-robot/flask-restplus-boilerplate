from flask_restplus import Api
from flask import Blueprint, request

from app.main.controller.user_controller import api as user_ns
from app.main.controller.auth_controller import api as auth_ns
from app.main.service.event_service import save_events
from app.main.service.auth_helper import Auth

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/api/user')
api.add_namespace(auth_ns, path='/api/auth')

@api.blueprint.after_request
def after(response):
    try:
        if request.path.startswith('/api'):
            data, status = Auth.get_logged_in_user(request)
            if status == 200:
                user_public_id = data['data']['public_id']
            else:
                user_public_id = ''
            data = {
                "user_pid": user_public_id,
                "request_path": request.path,
                "request_data": request.data,
                "request_method": request.method,
                "response_status": response.status,
                "response_data": response.data[:5000]
            }
            save_events.delay(data)
    except Exception as e:
        pass
    return response
