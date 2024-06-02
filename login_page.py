from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Login_Page:
    def __init__(self, driver):
        self.driver = driver

    def boot(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        password_input.send_keys(password)

        login_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")))
        login_input.click()

        if "dashboard" in self.driver.current_url:
            return True
        else:
            return False

    def logout(self):
        user_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[@class='oxd-userdropdown-name']")))
        user_dropdown.click()

        logout_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@class='oxd-userdropdown-link'][text()='Logout']")))
        logout_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))

    def error_msg(self):
        invalid_login_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")))
        text = invalid_login_msg.text
        print(text)

    def pim(self):
        pim = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()='PIM']")))
        pim.click()

    def add_employee(self):
        employee = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-item'])[2]")))
        employee.click()

        first_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))
        first_name.send_keys("Rohan")
        print("Added a New Employee:")
        print("First Name: Rohan")

        last_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Last Name']")))
        last_name.send_keys("Balaji")
        print("Last Name: Balaji")

        employee_id = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))

        employee_id.send_keys(Keys.CONTROL + "a")
        employee_id.send_keys(Keys.DELETE)
        employee_id.send_keys("00197")
        print("Employee Id: 00197")

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'oxd-form-loader')))
        search_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                               "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'][@type='submit']")))
        search_button.click()

        driver_license = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH,
                                                                                              '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')))
        driver_license.send_keys("45678")
        print("Driving License No: 45678")

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'oxd-form-loader')))
        nationality = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")))
        nationality.click()

        indian = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                                  '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]')))
        indian.click()
        print("Nationality: Indian")

        dob = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                     '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')))
        dob.send_keys("2003-03-02")
        print("Date of Birth: 02-03-2003")

        gender = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span')))
        gender.click()
        print("Gender: Male")

        save_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                           "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])[1]")))
        save_button.click()

    def edit_employee(self):
        employee_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")))
        employee_name.send_keys("Rohan Balaji")

        search_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                               "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'][@type='submit']")))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'oxd-form-loader')))
        search_button.click()

        self.driver.execute_script("window.scrollBy(0, 300);")

        edit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[2]")))
        edit.click()

        middle_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Middle Name']")))
        middle_name.send_keys("Ashok")
        print("Edit an Existing Employee: Rohan")
        print("Added Middle Name: Ashok")

        driver_license = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]")))
        driver_license.clear()
        driver_license.send_keys("694837")
        print("Edited License Number: 694837")

        dob = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                     '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')))
        dob.send_keys(Keys.CONTROL + "a")
        dob.send_keys(Keys.DELETE)
        dob.send_keys("2003-05-06")
        print("Edited Date of Birth: 06-05-2003")

        search_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                               "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'][@type='submit']")))
        search_button.click()

    def delete_employee(self):
        employee_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")))
        employee_name.send_keys("Rohan")

        search_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                               "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'][@type='submit']")))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'oxd-form-loader')))
        search_button.click()

        self.driver.execute_script("window.scrollBy(0, 300);")

        delete = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[1]")))
        delete.click()

        yes_delete = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                            "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")))
        yes_delete.click()

        print("Successfully Deleted An Existing Employee: Rohan Balaji")
