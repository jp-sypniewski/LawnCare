import flask


class RequestDictionary(dict):
    def __init__(self, *args, default_val=None, **kwargs):
        self.default_val = default_val
        super().__init__(*args, **kwargs)

    def __getattr__(self, key):
        return self.get(key, self.default_val)


def create(default_val=None, **route_args) -> RequestDictionary:
    request = flask.request

    args = request.args
    form = request.form

    data = {
        **args,
        **request.headers,
        **form,
        **route_args
    }

    return RequestDictionary(data, default_val=default_val)
