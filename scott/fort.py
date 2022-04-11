import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from useful_functions import password_Generator, random_four_digit_PIN, switch_to


class Fort:

    def __init__(self, info, email):
        self.path = 'driver/chromedriver.exe'
        self.baseURL = 'http://fortscott.edu/'
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.get(self.baseURL)

        #########################################
        # FEEL FREE TO TWEAK WITH THESE PARAMETERS
        self.address = "2108 S Horton St"
        self.city = 'Fort Scott'
        self.zipcode = '66701'

        self.birth_date = "24"
        self.birth_month = "03"
        self.birth_year = "1997"
        #######################################
        self.firstname = info.get('firstname')
        self.lastname = info.get('lastname')
        self.ssn_number = info.get('ssn')
        self.fathername = info.get('fathername')
        self.phone_num = info.get('phone_num')
        self.parent_phone = info.get('parent_phone')
        self.phone_num = ''.join(self.phone_num.split('-'))
        self.parent_phone = ''.join(self.parent_phone.split('-'))
        self.sex = info.get('sex')
        self.email = email

        self.PIN = None
        self.password = None
        self.id_number = None
        self.fort_email = None
        self.accinfo = []

    def _select_location(self):
        select_location_ID = 'PREFLOCATION'
        self.set_select(select_location_ID, "HARLEY")

    def _name_feild(self):
        firstname_ID = 'FIRSTNAME'
        _middlename_ID = 'MIDDLENAME'
        lastname_ID = 'LASTNAME'

        self._set_input_by_id(firstname_ID, self.firstname)
        self._set_input_by_id(lastname_ID, self.lastname)

    def _set_other_info(self):
        birth_month_ID = 'BIRTHMM'
        birth_date_ID = 'BIRTHDD'
        birth_year_ID = 'BIRTHYYYY'

        street_ID = 'LEGALSTREET'
        city_ID = 'LEGALCITY'
        state_ID = 'LEGALSTATE'
        zipcode_ID = 'LEGALZIP'

        phone_ID = 'PRIMARYPHONE'
        phone_type_select_ID = 'PPHONETYPE'

        self.set_date_box(self.birth_month, self.birth_date, self.birth_year, birth_month_ID, birth_date_ID,
                          birth_year_ID)
        self._set_input_by_id(street_ID, self.address)
        self._set_input_by_id(city_ID, self.city)
        self.set_select(state_ID, "KS")
        self._set_input_by_id(zipcode_ID, self.zipcode)
        self._click_button_by_ID('SAMEADDRESS')

        self._set_input_by_id(phone_ID, self.phone_num)
        self.set_select(phone_type_select_ID, "C")

    def _set_email(self):
        email_ID = 'ALT_EMAIL'
        re_enter_email_ID = 'ALT_EMAIL_VERIFY'
        email = self.email
        self._set_input_by_id(email_ID, email)
        self._set_input_by_id(re_enter_email_ID, email)

    def _some_buttons(self):
        if self.sex == "M":
            self.driver.find_element_by_xpath('//*[@id="SEX"][@value="M"]').click()
        else:
            self.driver.find_element_by_xpath('//*[@id="SEX"][@value="F"]').click()

        # do not touch!
        self.driver.find_element_by_xpath('//*[@id="HISPANIC"][@value="N"]').click()
        self.driver.find_element_by_id('WHITE').click()
        self.driver.find_element_by_xpath('//*[@id="FELONY"][@value="N"]').click()
        self.driver.find_element_by_xpath('//*[@id="NATIVELANG"][@value="Y"]').click()
        self.driver.find_element_by_xpath('//*[@id="PARENTSBACH"][@value="Y"]').click()
        self.driver.find_element_by_xpath('//*[@id="SINGLEPARENT"][@value="N"]').click()
        self.driver.find_element_by_xpath('//*[@id="MILITARY"][@value="N"]').click()
        self.driver.find_element_by_xpath('//*[@id="VETERAN"][@value="N"]').click()
        self.driver.find_element_by_xpath('//*[@id="MILITARYCONN"][@value="U"]').click()

    def _press_continue(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.NAME, 'Continue'))
        ).click()

    def _click_apply_now(self):
        try:
            self._click_button_by_ID('superfish-1-toggle')
            WebDriverWait(self.driver, 8).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Apply Now'))
            ).click()
        except TimeoutException:
            self.driver.maximize_window()
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Apply Now'))
            ).click()


    def _enter_SSN(self):

        ssn1_ID = 'SSN1'
        ssn2_ID = 'SSN2'
        ssn3_ID = 'SSN3'

        # splitng ssn into '515'-'38'-'2672'
        ssn1 = self.ssn_number[:3]
        ssn2 = self.ssn_number[4:6]
        ssn3 = self.ssn_number[7:]

        self._set_input_by_id(ssn1_ID, ssn1)
        self._set_input_by_id(ssn2_ID, ssn2)
        self._set_input_by_id(ssn3_ID, ssn3)

        self._press_continue()

    def _verify_enter_SSN(self):
        ssn1_ID = 'VERIFYSSN1'
        ssn2_ID = 'VERIFYSSN2'
        ssn3_ID = 'VERIFYSSN3'

        ssn1 = self.ssn_number[:3]
        ssn2 = self.ssn_number[4:6]
        ssn3 = self.ssn_number[7:]

        self._set_input_by_id(ssn1_ID, ssn1)
        self._set_input_by_id(ssn2_ID, ssn2)
        self._set_input_by_id(ssn3_ID, ssn3)

        self._press_continue()

    def _set_demographic_page_info(self):
        self._select_location()
        self._name_feild()
        self._set_other_info()
        self._set_email()
        self._some_buttons()
        self._press_continue()

    def _set_residency_page_info(self):
        self._click_button_by_XPATH('//*[@id="KSRESIDENT"][@value="Y"]')
        self._press_continue()

    def _set_kanas_residency_status_page(self):
        residency_month_ID = 'RESDATEMM'
        residency_day_ID = 'RESDATEDD'
        residency_year_ID = 'RESDATEYYYY'

        legal_county_ID = 'COUNTY'

        county_month_ID = 'RESDATE_COMM'
        county_day_ID = 'RESDATE_CODD'
        county_year_ID = 'RESDATE_COYYYY'

        self.set_date_box(self.birth_month, self.birth_date, self.birth_year, residency_month_ID, residency_day_ID,
                          residency_year_ID)
        self.set_select(legal_county_ID, "JO")
        self.set_date_box(self.birth_month, self.birth_date, self.birth_year, county_month_ID, county_day_ID,
                          county_year_ID)

        self._press_continue()

    def _educational_plans_page(self):
        best_describe_you_XPATH_ID = '//*[@id="CUROBJ"][@value="2"]'
        major_box_ID = "MAJOR"
        degree_box_ID = "DEGREE"

        self._click_button_by_XPATH(best_describe_you_XPATH_ID)
        self.set_select(major_box_ID, "GS")
        self.set_select(degree_box_ID, "AA - Associate of Arts")
        self._press_continue()

    def _high_school_page(self):
        kansas_school_ID = 'HSTYPE'
        select_school_ID = 'HSCODE_KS'
        self._click_button_by_ID(kansas_school_ID)
        self.set_select(select_school_ID, "171020")
        self._press_continue()

    def _high_school_graduated(self):
        hs_graduated_month_ID = 'HSGRMM'
        hs_graduated_year_ID = 'HSGRYYYY'

        self.set_date_box("06", None, "2019", hs_graduated_month_ID, None, hs_graduated_year_ID)
        self._press_continue()

    def _prev_clg_exp(self):
        prev_class_XPATH_ID = '//*[@id="PREVFSCC"][@value="N"]'
        prev_attd_cls_XPATH = '//*[@id="PREVCOLLEGE"][@value="N"]'
        have_degee_XPATH = '//*[@id="CLASS"][@value="1"]'

        self._click_button_by_XPATH(prev_class_XPATH_ID)
        self._click_button_by_XPATH(prev_attd_cls_XPATH)
        self._click_button_by_XPATH(have_degee_XPATH)
        self._press_continue()

    def _why_choose_page(self):
        deciding_factor_XPATH_ID = '//*[@id="SELECTFACTOR"][@value="01"]'
        hear_about_us_XPATH_ID = '//*[@id="MARKETING_05"][@value="Y"]'

        self._click_button_by_XPATH(deciding_factor_XPATH_ID)
        self._click_button_by_XPATH(hear_about_us_XPATH_ID)
        self._press_continue()

    def parent_page(self):
        parent_firstname_ID = 'EMERGFIRST'
        parent_lastname_ID = 'EMERGLAST'
        street_address_ID = 'EMERGSTREET'
        city_ID = 'EMERGCITY'
        select_state_ID = 'EMERGSTATE'  # value 'KS'
        zipcode_ID = 'EMERGZIP'
        telephone_ID = 'EMERGPHONE'

        self._set_input_by_id(parent_firstname_ID, self.fathername)
        self._set_input_by_id(parent_lastname_ID, self.lastname)
        self._set_input_by_id(street_address_ID, self.address)
        self._set_input_by_id(city_ID, self.city)
        self.set_select(select_state_ID, "KS")
        self._set_input_by_id(zipcode_ID, self.zipcode)
        self._set_input_by_id(telephone_ID, self.parent_phone)

        self._press_continue()

    def tuberculosis_question(self):
        test_positive_radio_XPATH_ID = '//*[@id="TBSCREEN1"][@value="N"]'
        diagnosis_radio_XPATH_ID = '//*[@id="TBSCREEN2"][@value="N"]'
        travelled_cty_radio_XPATH_ID = '//*[@id="TBSCREEN5"][@value="N"]'

        self._click_button_by_XPATH(test_positive_radio_XPATH_ID)
        self._click_button_by_XPATH(diagnosis_radio_XPATH_ID)
        self._click_button_by_XPATH(travelled_cty_radio_XPATH_ID)
        time.sleep(2)
        select_box = self.driver.find_element_by_name('BIRTHCOUNTRY')
        select_country = Select(select_box)
        select_country.select_by_value("US")

        self._press_continue()

    def final_authorization(self):
        input_PIN_ID = 'PIN'
        input_password_ID = 'TEMPPASSWORD'
        final_radio_XPATH_ID = '//*[@id="FINALAUTH"][@value="Y"]'

        self.PIN = random_four_digit_PIN()
        self.password = password_Generator(9)

        self._set_input_by_id(input_PIN_ID, self.PIN)
        self._set_input_by_id(input_password_ID, self.password)

        self._click_button_by_XPATH(final_radio_XPATH_ID)
        self._press_continue()

    def login_page(self):
        time.sleep(5)
        input_username_ID = 'userName'
        input_password_ID = 'password'
        btn_login_ID = 'btnLogin'

        self._set_input_by_id(input_username_ID, self.id_number)
        self._set_input_by_id(input_password_ID, self.PIN)

        self._click_button_by_ID(btn_login_ID)

    def grab_info(self):
        # scapping  input like password and ID
        second_table = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/center/table/tbody/tr/td/table/tbody/tr[4]/td/p[1]/table')))
        all_rows = second_table.find_elements_by_tag_name('tr')
        for row in all_rows:
            if "Your" in row.text and ":" in row.text:
                self.accinfo.append(row.text.strip())

        self.id_number = self.accinfo[0].split(':')[1]
        self.PIN = self.accinfo[1].split(':')[1]
        self.fort_email = self.accinfo[2].split(':')[1]
        self.password = self.accinfo[3].split(':')[1]
        self._press_continue()

    def save_info(self):
        print("======================")
        print(f"ID Number ==> {self.id_number}")
        print(f"PIN number ==> {self.PIN}")
        print(f"Fort Scott emailID ==> {self.fort_email}")
        print(f"Password ==> {self.password}")
        print("=========================")
        print("all info are saved!")

        with open("accountinfo1.txt", "w") as txtFile:
            txtFile.writelines("ID Number ==> {}\n".format(self.id_number))
            txtFile.writelines("PIN number ==> {}\n".format(self.PIN))
            txtFile.writelines("Fort Scott emailID ==> {}\n".format(self.fort_email))
            txtFile.writelines("Password ==> {}\n".format(self.password))

    def refund_process(self):

        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'here'))).click()

        switch_to(self.driver, 'Premier Pay')
        time.sleep(3)
        choose_student_account_XPATH_ID = '//*[@id="student-choice-form"]/div[5]/div/div/div/label/span[1]'
        time.sleep(3)
        self._click_button_by_XPATH(choose_student_account_XPATH_ID)

        time.sleep(2)
        self._click_button_by_XPATH(
            '//*[@id="student-choice-form"]/div[6]/div/div[2]/div[2]/div/div/col-md-offset-3/button[2]')

    def final_process(self):
        switch_to(self.driver, 'fortscott')

        click_after_choice_ID = 'AfterChoice'
        click_all_correct_Checkbox_ID = 'ALL_CORRECT'
        final_btn_continue_XPATH = '//*[@id="question_response"]/table/tbody/tr[2]/td/input'
        self._click_button_by_ID(click_after_choice_ID)
        time.sleep(2)
        self._click_button_by_ID(click_all_correct_Checkbox_ID)
        time.sleep(2)
        self._click_button_by_XPATH(final_btn_continue_XPATH)

    def logout(self):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'here'))).click()
        print("Check your Gmail account for Acceptance letter")
        print("Wait 1 week for any response from Fort Scott")
        print("Don't cry if you don't get .Edu mail :D")
        print("bye! ;) ")
        self.driver.close()
        self.driver.quit()

    # some helpful functions!
    ########################################

    def set_date_box(self, month=None, day=None, year=None, month_id=None, day_id=None, year_id=None):

        if month_id != None:
            select_month_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, month_id)))
            select_month = Select(select_month_box)
            select_month.select_by_value(month)

        if day_id != None:
            select_day_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, day_id)))
            select_day = Select(select_day_box)
            select_day.select_by_value(day)

        if year_id != None:
            select_year_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, year_id)))
            select_year = Select(select_year_box)
            select_year.select_by_value(year)

    def _click_button_by_XPATH(self, button_XPATH):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, button_XPATH))).click()

    def _click_button_by_ID(self, button_ID):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, button_ID))).click()

    def _set_input_by_id(self, input_box_id, input_value):
        input_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, input_box_id))
        )
        input_box.send_keys(input_value)

    def set_select(self, select_ID, value):
        box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, select_ID)))

        option = Select(box)
        option.select_by_value(value)

    ###########################################################

    # main program
    def start_process(self):
        self._click_apply_now()
        time.sleep(2)
        self._press_continue()
        time.sleep(2)
        self._enter_SSN()
        time.sleep(2)
        self._verify_enter_SSN()
        time.sleep(2)
        self._set_demographic_page_info()
        time.sleep(2)
        self._set_residency_page_info()
        time.sleep(2)
        self._set_kanas_residency_status_page()
        time.sleep(2)
        self._educational_plans_page()
        time.sleep(2)
        self._high_school_page()
        time.sleep(2)
        self._high_school_graduated()
        time.sleep(2)
        self._prev_clg_exp()
        time.sleep(2)
        self._why_choose_page()
        time.sleep(2)
        self.parent_page()
        time.sleep(2)
        self.tuberculosis_question()
        time.sleep(2)
        self.final_authorization()
        time.sleep(2)
        self.grab_info()
        time.sleep(2)
        self.login_page()
        time.sleep(2)
        self.save_info()
        time.sleep(2)
        self.refund_process()
        time.sleep(2)
        self.final_process()
        time.sleep(5)
        self.logout()
