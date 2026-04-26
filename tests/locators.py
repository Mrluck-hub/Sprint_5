from selenium.webdriver.common.by import By

class TestLocators:
    # Регистрация
    REG_NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    REG_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    REG_PASS_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REG_ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")
    
    # Вход
    LOGIN_EMAIL_INPUT = (By.NAME, "name")
    LOGIN_PASS_INPUT = (By.NAME, "Пароль")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    
    #Страница профиля
    PROFILE_EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    PROFILE_LOGIN_INPUT = (By.XPATH, ".//label[text()='Логин']/following-sibling::input")

    # Навигация (кнопки входа)
    MAIN_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    HEADER_CABINET_BUTTON = (By.XPATH, ".//a/p[text()='Личный Кабинет']")
    REG_FORM_LOGIN_LINK = (By.LINK_TEXT, "Войти")
    FORGOT_PASS_LOGIN_LINK = (By.LINK_TEXT, "Войти")
    
    # Переходы
    HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    HEADER_LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    
    # Разделы конструктора
    TAB_BUNS = (By.XPATH, ".//span[text()='Булки']/parent::div")
    TAB_SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    TAB_FILLINGS = (By.XPATH, ".//span[text()='Начинки']/parent::div")