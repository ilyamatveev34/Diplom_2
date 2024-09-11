from page_objects.password_recovery_page import PasswdRecoveryPage
from page_objects.main_page import MainPage
from conftest import *
import allure


class TestPasswdRecoveryPage:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_to_recovery_passwd_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        assert recovery_page.check_displaying_of_input_email()

    @allure.title('Проверка перехода к восстановлению пароля при вводе валидного email и нажатии кнопки "Восстановить"')
    def test_click_recovery_button_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        assert recovery_page.check_displaying_of_input_password()

    @allure.title('Проверка отображения пароля в поле ввода после клика на иконку с глазом')
    def test_click_on_eye_icon_makes_passwd_visible_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        recovery_page.send_password()
        recovery_page.click_on_eye_icon()
        assert recovery_page.check_displaying_password_value()

    @allure.title('Проверка маскировки пароля в поле ввода после двух кликов на иконку с глазом')
    def test_double_click_on_eye_icon_makes_passwd_invisible_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        recovery_page.send_password()
        recovery_page.click_on_eye_icon()
        recovery_page.click_on_eye_icon()
        assert recovery_page.check_not_displaying_password_value()
