from cerberus import Validator


class VisualistValidator(Validator):
    def _validate_unique(self, unique, field, value):
        """ Test the uniqueness of a value.

        The rule's arguments are validated against this schema:
        {'unique': 'boolean'}
        """
        in_database = False
        if unique and in_database:
            self._error(field, "Value must not already be in database")
