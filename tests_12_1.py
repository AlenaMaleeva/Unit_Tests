import runner
import unittest

class RunnerTest (unittest.TestCase):
    def test_walk (self):
        walk = runner.Runner('Один')
        for i in range(10):
            walk.walk()
        self.assertEqual(walk.distance, 50)


    def test_run (self):
        run = runner.Runner('Два')
        for a in range (10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge (self):
        walk1 = runner.Runner ('Три')
        run1 = runner.Runner ('Четыре')
        for y in range (10):
            walk1.walk()
            run1.run()
        self.assertNotEqual(run1.distance, walk1.distance)

       







