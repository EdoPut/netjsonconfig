class NetJsonConfigException(Exception):
    """
    Root netjsonconfig exception
    """
    def __str__(self):
        suberrors = ''
        for validator_value, error in zip(self.details.validator_value, self.details.context):
            suberrors += '\nAgainst schema %s\n%s\n' % (validator_value, error.message,)

        default_message = "%s %s\n" % (self.__class__.__name__, self.details,)

        return default_message + suberrors


class ValidationError(NetJsonConfigException):
    """
    Error while validating schema
    """
    def __init__(self, e):
        """
        preserve jsonschema exception attributes
        in self.details
        """
        self.message = e.message
        self.details = e
