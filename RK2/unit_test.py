import main
import unittest

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.Computer = [
            main.Computer(1, "AComputer"),
            main.Computer(2, "AComputer1"),
            main.Computer(3, "BComputer"),
        ]
        self.Browser = [
            main.Browser(1, "Chrome", 1),
            main.Browser(2, "Firefox", 3),
            main.Browser(3, "Safari", 2),
        ]
        self.BrowserComputer = [
            main.BrowserComputer(1, 1, 1000),
            main.BrowserComputer(2, 4, 2000),
            main.BrowserComputer(3, 2, 1500),
        ]

        self.one_to_many = main.create_one_to_many(self.Computer, self.Browser)
        self.many_to_many = main.create_many_to_many(self.BrowserComputer, self.Browser, self.Computer)

    def test_first_task_method(self):
        result = [(i[2],i[0]) for i in main.task_1(self.one_to_many, 'A')]
        true_result = [('AComputer', 'Chrome'),
                       ('AComputer1', 'Safari')]
        self.assertEqual(result, true_result)

    def test_second_task_method(self):
        result = main.task_2(self.many_to_many)
        true_result = [('AComputer', 1000),
                       ('BComputer', 1500)]
        self.assertEqual(result, true_result)

    def test_third_task_method(self):
        result = [(i[1], i[0]) for i in main.task_3(self.many_to_many)]
        true_result = [('AComputer','Chrome'),
                       ('BComputer','Firefox')]
        self.assertEqual(result, true_result)


if __name__ == '__main__':
    unittest.main()