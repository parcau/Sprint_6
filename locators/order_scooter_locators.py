from selenium.webdriver.common.by import By

NAME_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Имя')]")
SURNAME_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Фамилия')]")
ADDRESS_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Адрес: куда привезти заказ')]")
METRO_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Станция метро')]")
PHONE_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]")
ORDER_BUTTON_UPPER = (By. XPATH, "//button[@class='Button_Button__ra12g']")
STATION_SOKOLNIKI = (By.XPATH, "//div[@class= 'Order_Text__2broi' and contains(text(), 'Сокольники')]")
STATION_OHOTNYI_RYAD = (By.XPATH, "//div[@class= 'Order_Text__2broi' and contains(text(), 'Охотный Ряд')]")
NEXT_BUTTON = (By.XPATH, "//button[contains(.,'Далее')]")
DATE_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Когда привезти самокат')]")
DATA1_CHOOSE = (By.XPATH, "//div[contains(@aria-label,'Choose воскресенье, 5-е мая 2024 г.')]")
DATA2_CHOOSE = (By.XPATH, "//div[contains(@aria-label,'Choose воскресенье, 12-е мая 2024 г.')]")
RENTAL_TIME_FIELD = (By.XPATH, "//div[@aria-haspopup='listbox']")
RENT_TWO_DAYS = (By.XPATH, "//div[@class= 'Dropdown-option' and contains(text(), 'двое суток')]")
RENT_FIVE_DAYS = (By.XPATH, "//div[@class= 'Dropdown-option' and contains(text(), 'пятеро суток')]")
BLACK_COLOR_SCOOTER = (By.XPATH, "//input[@id='black']")
GREY_COLOR_SCOOTER = (By.XPATH, "//input[@id='grey']")
COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
ORDER_BUTTON_LOWER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
ACCEPT_BUTTON = (By.XPATH, "//button[contains(.,'Да')]")
SEE_STATUS_BUTTON = (By.XPATH, "//button[@class= 'Button_Button__ra12g Button_Middle__1CSJM' and contains(text(), 'Посмотреть статус')]")