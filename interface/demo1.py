import unittest,os
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(os.getcwd(), "*test.py")
suite.addTest(tests)
f = open("报告.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    verbosity = 1,
    title="报告"
)

runner.run(suite)