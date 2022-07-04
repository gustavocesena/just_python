from unittest import TestCase


class TestAgeValidator(TestCase):
    def setUp(self) -> None:
        from decorators.examples.age_validator import save_age_in_some_database

        self.age_validator = save_age_in_some_database

    def test_validate_age_decorator_with_a_valid_age_not_raise_a_ValueError_Exception(
        self,
    ):
        age = 30
        self.age_validator(age)

    def test_validate_age_validator_with_an_string_age_format_raise_a_ValueError_Exception(
        self,
    ):
        age = "Gus"
        with self.assertRaises(ValueError):
            self.age_validator(age)

    def test_validate_age_validator_with_an_float_age_format_raise_a_ValueError_Exception(
        self,
    ):
        age = 30.5
        with self.assertRaises(ValueError):
            self.age_validator(age)
