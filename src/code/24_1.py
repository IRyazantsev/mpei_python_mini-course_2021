def greet(username: str, ages: int = 21) -> None:
    print('{0} is {1}!'.format(username, ages))

greet(username='Helen')
