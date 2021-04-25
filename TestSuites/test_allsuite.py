from unittest import TestLoader, TestSuite

from HtmlTestRunner import HTMLTestRunner

from Test.test_contact import ContactUs
from Test.test_login import TestLogin
from Test.test_login2 import Test_login2
from Test.test_order import test_order
from Test.test_productdetail import test_prodetail
from Test.test_search2 import search2Page
from Test.test_search_1 import search1Page
from Test.test_sendLetter import Send_Letter

# Get all test from Test
test1 = TestLoader().loadTestsFromTestCase(TestLogin)
test2 = TestLoader().loadTestsFromTestCase(Test_login2)

test3 = TestLoader().loadTestsFromTestCase(Send_Letter)
test4 = TestLoader().loadTestsFromTestCase(ContactUs)
test5 = TestLoader().loadTestsFromTestCase(search1Page)
test6 = TestLoader().loadTestsFromTestCase(search2Page)
test7 = TestLoader().loadTestsFromTestCase(test_order)
test8 = TestLoader().loadTestsFromTestCase(test_prodetail)

# Creating test suites
# Sanity test suite
masterTestSuite = TestSuite([test1, test2, test3, test4,test8,test5, test7])
runner = HTMLTestRunner(output=r'..\\Reports', combine_reports=True, report_title="Final Report").run(masterTestSuite)
