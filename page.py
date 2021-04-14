from selenium import webdriver
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
    def test_01(self):
        self.driver.find_element_by_id("kw").send_keys("haha")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        title = self.driver.title
        self.assertIn("搜索",title)
if __name__ == '__main__':
    unittest.main()
