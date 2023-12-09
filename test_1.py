import time
import yaml
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from module import Site


class Selenium:
    pass


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

# site = Site(testdata["address"])

# def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_xpath):
#     input1 = site.find_element("xpath", log_xpath)
#     input1.send_keys("CotCat---")
#     input2 = site.find_element("xpath", pass_xpath)
#     input2.send_keys("d09da299ca---")
#     btn = site.find_element("xpath", btn_xpath)
#     btn.click()
#     errlable = site.find_element("xpath", result_xpath)
#     assert errlable.text == "401"
#
# def test_step2(site, log_xpath, pass_xpath, btn_xpath, blog_xpath):
#     input1 = site.find_element("xpath", log_xpath)
#     input1.send_keys(testdata["login"])
#     input2 = site.find_element("xpath", pass_xpath)
#     input2.send_keys(testdata["password"])
#     btn = site.find_element("xpath", btn_xpath)
#     btn.click()
#     blog = site.find_element("xpath", blog_xpath)
#     assert blog.text == "Blog"

    def test_step3(site, log_xpath, pass_xpath, btn_xpath, new_post_xpath, new_post_title_xpath, new_post_descr_xpath, new_post_content_xpath, new_post_save_xpath, new_post_save_fine_xpath):
        input1 = site.find_element("xpath", log_xpath)
        input1.send_keys(testdata["login"])
        input2 = site.find_element("xpath", pass_xpath)
        input2.send_keys(testdata["password"])
        btn = site.find_element("xpath", btn_xpath)
        btn.click()

        time.sleep(2)
        # wait = WebDriverWait(site.driver, 10)
        # wait.until(EC.element_to_be_clickable((By.XPATH, new_post_xpath)))

        new_post = site.find_element("xpath", new_post_xpath)
        new_post.click()

        time.sleep(2)

        input3 = site.find_element("xpath", new_post_title_xpath)
        input3.send_keys("Title_test")

        input4 = site.find_element("xpath", new_post_descr_xpath)
        input4.send_keys("Description_test")

        input5 = site.find_element("xpath", new_post_content_xpath)
        input5.send_keys("Content_test")

        new_post_save = site.find_element("xpath", new_post_save_xpath)
        new_post_save.click()

        time.sleep(2)

        new_post_fine = site.find_element("xpath", new_post_save_fine_xpath)
        assert new_post_fine.text == "Title_test"

    # x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    # input1 = site.find_element("xpath", x_selector1)
    # input1.clear()
    # input1.send_keys("CotCat")
    #
    # x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    # input2 = site.find_element("xpath", x_selector2)
    # input2.clear()
    # input2.send_keys("d09da299ca---")
    #
    # btn_selector = "button"
    # btn = site.find_element("css", btn_selector)
    # btn.click()
    #
    # x_selector3 = """// *[ @ id = "app"] / main / div / div / div[2] / h2"""
    # err_label = site.find_element("xpath", x_selector3)
    # assert err_label.text == "401"



# test_step1()













# print(err_label.text)




# css_selector = "span.mdc-text-field__ripple"
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("css", css_selector, "height"))
# print(site.get_element_property("xpath", xpath, "color"))
