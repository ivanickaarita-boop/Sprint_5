from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Личный Кабинет» в шапке сайта
    PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    # Кнопка «Оформить заказ» после авторизации
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    # Кнопка «Конструктор» в шапке сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")

    # Логотип Stellar Burgers в шапке сайта
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

    # Вкладка «Булки» в конструкторе
    BUNS_SECTION_BUTTON = (By.XPATH, ".//span[text()='Булки']/parent::*")

    # Вкладка «Соусы» в конструкторе
    SAUCES_SECTION_BUTTON = (By.XPATH, ".//span[text()='Соусы']/parent::*")

    # Вкладка «Начинки» в конструкторе
    FILLINGS_SECTION_BUTTON = (By.XPATH, ".//span[text()='Начинки']/parent::*")

    # Заголовок раздела «Булки»
    BUNS_HEADER = (By.XPATH, ".//h2[text()='Булки']")

    # Заголовок раздела «Соусы»
    SAUCES_HEADER = (By.XPATH, ".//h2[text()='Соусы']")

    # Заголовок раздела «Начинки»
    FILLINGS_HEADER = (By.XPATH, ".//h2[text()='Начинки']")


class LoginPageLocators:
    # Заголовок формы входа
    LOGIN_TITLE = (By.XPATH, ".//h2[text()='Вход']")

    # Поле ввода email на странице входа
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/parent::*/input")

    # Поле ввода пароля на странице входа
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/parent::*/input")

    # Кнопка «Войти» на странице входа
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # Ссылка «Зарегистрироваться» на странице входа
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")

    # Ссылка «Восстановить пароль» на странице входа
    RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")


class RegisterPageLocators:
    # Поле ввода имени на странице регистрации
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/parent::*/input")

    # Поле ввода email на странице регистрации
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/parent::*/input")

    # Поле ввода пароля на странице регистрации
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/parent::*/input")

    # Кнопка «Зарегистрироваться» на странице регистрации
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    # Ссылка «Войти» на странице регистрации
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

    # Ошибка при вводе некорректного пароля
    PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")


class ForgotPasswordPageLocators:
    # Ссылка «Войти» на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")


class ProfilePageLocators:
    # Ссылка «Профиль» в личном кабинете
    PROFILE_TEXT = (By.XPATH, ".//a[text()='Профиль']")

    # Ссылка «История заказов» в личном кабинете
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[text()='История заказов']")

    # Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")