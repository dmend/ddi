import unittest

from parameterized import parameterized

import port_tools


class TestPortExclusions(unittest.TestCase):
    @parameterized.expand([
        (
            [[80, 80], [22, 23], [8000, 9000]],
            [[1024, 1024], [8080, 8080]],
            [[22, 23], [80, 80], [8000, 8079], [8081, 9000]]
        ),
        (
            [[8000, 9000], [80, 80], [22, 23]],
            [[1024, 1024], [8080, 8080]],
            [[22, 23], [80, 80], [8000, 8079], [8081, 9000]]
        ),
        (
            [[1, 65535]],
            [[1000, 2000], [500, 2500]],
            [[1, 499], [2501, 65535]]
        ),
        (
            [[1, 1], [3, 65535], [2, 2]],
            [[1000, 2000], [500, 2500]],
            [[1, 499], [2501, 65535]]
        ),
        (
            [],
            [[8080, 8080]],
            []
        )
    ])
    def test_examples(self, include, exclude, expected):
        result = port_tools.apply_port_exclusions(include, exclude)
        self.assertEqual(expected, result)

    @parameterized.expand([
        (
            [[1, 1], [2, 2]],
            [[1, 2]]
        ),
        (
            [[1, 1], [3, 3]],
            [[1, 1], [3, 3]]
        ),
        (
            [[1, 4], [2, 3]],
            [[1, 4]]
        ),
        (
            [[1, 5], [1, 4]],
            [[1, 5]]
        ),
        (
            [[1, 4], [1, 5]],
            [[1, 5]]
        ),
        (
            [[2, 4], [1, 5]],
            [[1, 5]]
        ),
        (
            [[1, 1], [1, 1]],
            [[1, 1]]
        ),
        (
            [],
            []
        )
    ])
    def test_minimize(self, ports, expected):
        result = port_tools.minimized(ports)
        self.assertEqual(expected, result)

    def test_validate_malformed_pair(self):
        with self.assertRaises(ValueError):
            port_tools._validate([[2, 1]])

    def test_validate_non_integer(self):
        with self.assertRaises(TypeError):
            port_tools._validate([['a', 'b']])

    def test_minimzed_malformed_pair(self):
        with self.assertRaises(ValueError):
            port_tools.minimized([[2, 1]])

    def test_minimized_non_integer(self):
        with self.assertRaises(TypeError):
            port_tools.minimized([['a', 'b']])

    @parameterized.expand([
        ([[1, 1]], [[2, 1]]),
        ([[2, 1]], [[1, 1]])
    ])
    def test_port_exclusions_malformed_pairs(self, include, exclude):
        with self.assertRaises(ValueError):
            port_tools.apply_port_exclusions(include, exclude)

    @parameterized.expand([
        ([[1, 1]], [['a', 'b']]),
        ([['a', 'b']], [[1, 1]])
    ])
    def test_port_exclusions_non_integers(self, include, exclude):
        with self.assertRaises(TypeError):
            port_tools.apply_port_exclusions(include, exclude)
