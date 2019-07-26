from flask_restplus import Api
from flask import Blueprint, request

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.service.event_service import save_events

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
            data = {
                "request_path": request.path,
                "request_data": request.data,
                "request_method": request.method,
                "response_status": response.status,
                "response_data": response.data[:5000]
            }
            save_events(data)
    except Exception as e:
        pass
    return response
