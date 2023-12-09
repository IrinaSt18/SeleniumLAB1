import pytest
from module import Site
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def log_xpath():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def pass_xpath():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def btn_xpath():
    return """//*[@id="login"]/div[3]/button"""


@pytest.fixture()
def result_xpath():
    return """// *[ @ id = "app"] / main / div / div / div[2] / h2"""


@pytest.fixture()
def blog_xpath():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def new_post_xpath():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def new_post_title_xpath():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture()
def new_post_descr_xpath():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def new_post_content_xpath():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def new_post_save_xpath():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""

@pytest.fixture()
def new_post_save_fine_xpath():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def site():
    my_site = Site(testdata["address"])
    yield my_site
    my_site.close()
