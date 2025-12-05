# -*- coding: utf-8 -*-

from learn_mise_en_place.utils import add_two


def test_add_two():
    assert add_two(1, 2) == 3


if __name__ == "__main__":
    from learn_mise_en_place.tests import run_cov_test

    run_cov_test(
        __file__,
        "learn_mise_en_place.utils",
        preview=False,
    )
