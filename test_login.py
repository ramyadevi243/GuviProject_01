import pytest
from pages.login_page import Login_Page


# Successful Employee Login validation to OrangeHRM portal
@pytest.mark.parametrize("username, password, expected_result", [
    ("Admin", "admin123", True)
])
def test_valid_login(driver, username, password, expected_result):
    login_page = Login_Page(driver)
    login_page.boot()

    result = login_page.login(username, password)

    assert result == expected_result, f"Valid Login Test Failed for Username: {username} and Password: {password}"

    if result:
        login_page.logout()
        print("Successful employee Login to OrangeHRM portal")


# Invalid Employee Login validation to OrangeHRM Portal
@pytest.mark.parametrize("username, password, expected_result", [
    ("Admin", "InvalidPassword", False)
])
def test_invalid_login(driver, username, password, expected_result):
    login_page = Login_Page(driver)
    login_page.boot()

    result = login_page.login(username, password)

    assert result == expected_result, f"Invalid Login Test Failed for Username: {username} and Password: {password}"

    if not result:
        login_page.error_msg()


# Added One New Employee In The PIM Module
@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123")
])
def test_add_new_employee(driver, username, password):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.login(username, password)
    login_page.pim()
    login_page.add_employee()
    login_page.logout()


# Edited An Existing Employee In PIM Module
@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123")
])
def test_edit_employee_information(driver, username, password):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.login(username, password)
    login_page.pim()
    login_page.edit_employee()
    login_page.logout()


# Deleted An Existing Employee In PIM Module
@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123")
])
def test_delete_employee(driver, username, password):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.login(username, password)
    login_page.pim()
    login_page.delete_employee()
    login_page.logout()
