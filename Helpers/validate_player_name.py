import re

class ValidatingPlayerName:
    def validate_name(name):
        return bool(re.match("^[a-zA-Z]+$", name))