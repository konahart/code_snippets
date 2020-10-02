import unittest


class TestX(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestX)
    unittest.TextTestRunner(verbosity=2).run(suite)
