import falcon
import json

from app.validators.all_letters import AllLettersValidator

class AllLettersValidationResource(object):
    def on_post(self, req, resp):
        """Validates whether the string contains all 26 English letters"""
        self._set_default_response(resp)

        string = req.media.get('string')
        if string is None:
            resp.body = """{ "result": "error: request payload must contain a JSON object with a 'string' attribute" }"""
        else:
            resp.status = falcon.HTTP_200
            result = "pass" if self._validate(string) else "fail"
            resp.body = json.dumps({'result': result})

    def _validate(self, string):
        validator = AllLettersValidator()
        return validator.validate(string)

    def _set_default_response(self, resp):
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_400
        resp.body = '{ "result": "error" }'

