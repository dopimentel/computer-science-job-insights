from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("tests/mocks/jobs.csv", "full") == 3
