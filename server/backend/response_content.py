from backend.status import status

class ResponseContent(object):
    code = None
    data = {}
    error = None
    description = None
    mark = True

    def __init__(self, *args, **kwargs):
        self.refresh(**kwargs)

    def content(self):
        self.__set_params()
        content = {
            'code': self.code,
            'description': self.description,
        }

        if self.mark:
            content['error'] = self.error
        else:
            content['data'] = self.data
        return content

    def refresh(self, **kwargs):
        params = kwargs.items()
        for param in params:
            setattr(self, param[0], param[1])

    def __set_params(self):
        if self.code == 200:
            self.mark = False
        else:
            self.mark = True

        if self.description:
            self.description = status[str(self.description)]

        if isinstance(self.error, int):
            self.error = "{0}({1}): {2}".format(
                self.code,
                self.error,
                self.description
            )
