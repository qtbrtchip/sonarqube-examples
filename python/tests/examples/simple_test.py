import pytest
import time


def test_empty():
    """
    PyTest tests are callables whose names start with "test"
    (by default)

    It looks for them in modules whose name contains "test"
    (by default)
    """
    pass


def empty_test():
    """
    My name doesn't start with "test", so I won't get run.
    (by default ;-)
    """
    pass


def test_approximate_matches():
    """
    pytest.approx can be used to assert "approximate" numerical equality
    (compare UnitTest's "assertAlmostEqual")
    """
    assert (0.1 + 0.2) == pytest.approx(0.3)


def test_sleep():
    """
    pytest.approx can be used to assert "approximate" numerical equality
    (compare UnitTest's "assertAlmostEqual")
    """
    time.sleep(2)


@pytest.mark.timeout(4)
def test_specify_timeout():
    """
    pytest.approx can be used to assert "approximate" numerical equality
    (compare UnitTest's "assertAlmostEqual")
    """
    time.sleep(1)
