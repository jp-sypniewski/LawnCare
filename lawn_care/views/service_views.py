import flask

blueprint = flask.Blueprint('service', __name__, template_folder='templates')

@blueprint.route('/services/<str:service_name>')
def show_service(service_name: str):
    ret_dict = {'name': service_name}
    return flask.render_template('services/display.html', ret_dict)