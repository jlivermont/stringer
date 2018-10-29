import json

class AllLettersValidator(object):
    ENGLISH_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    def validate(self, string):
        char_dict = self._build_char_dict(string)
        return self._has_all_letters(char_dict)

    def _build_char_dict(self, string):
        char_dict = {}

        for char in list(string):
            char = char.lower()
            if self._is_lower_english_letter(char):
                char_dict[char] = 1

        return char_dict

    def _is_lower_english_letter(self, char):
        return char in self.ENGLISH_LETTERS

    def _has_all_letters(self, char_dict):
        return (len(char_dict.keys()) == 26)


def all_letters_validator_lambda(event, context):
    if not 'string' in event:
        raise KeyError("Parameter 'string' was not found")

    validator = AllLettersValidator()
    result = validator.validate(event['string'])

    return json.dumps({ "result": "{}".format(str(result).lower())})

