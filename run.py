from BeautifulReport import BeautifulReport
import unittest
suit = unittest.defaultTestLoader.discover("./","page.py")
runner = BeautifulReport(suit)
runner.report(description="描述",filename="./rep.html",log_path="./")
