class DBHandler:
    """
    Sample DB handler for testing purposes.
    """

    def save_age(self, age: int):
        print("saving age: ", age)


def validate_age(func):
    def wrapper(age: int):
        if not isinstance(age, int):
            raise ValueError(
                "Invalid age format: %s, expected int got %s" % (age, type(age))
            )
        func(age)

    return wrapper


@validate_age
def save_age_in_some_database(age: int):
    db_handler = DBHandler()
    db_handler.save_age(age)
