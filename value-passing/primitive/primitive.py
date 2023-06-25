from flytekit import task, workflow


@task
def square(x: int) -> int:
    return x * x


@task
def format_number(x: int) -> str:
    return f'number {x}'


@workflow
def primitive():
    x = 2
    x2 = square(x=x)
    print(format_number(x=x2))


if __name__ == '__main__':
    primitive()
