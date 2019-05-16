import unittest
from client_server.task_server import *


class TestTaskServer(unittest.TestCase):

    def test_build_error_for_client(self):
        self.assertIsInstance(build_error_for_client(400, 'Oops'), str)

if __name__ == '__main__':
    unittest.main()