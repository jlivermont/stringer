import falcon

from app.resources.all_letters_validation import AllLettersValidationResource

app = falcon.API()
all_letters_validator_resource = AllLettersValidationResource()
app.add_route('/all-letters-validator', all_letters_validator_resource)
