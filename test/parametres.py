#ДЛЯ API ТЕСТОВ----------------------------------

#корректный ID фильма
movie_id = 258687

#некорректный ID фильма
invalid_movie_id = 000000

#название фильма для API
params = {"name": "Шерлок Холмс"}


#ДЛЯ UI-ТЕСТОВ------------------

url = "https://www.kinopoisk.ru/"

#локатор строки поиска до нажатия
search_locator = "input.kinopoisk-header-search-form-input__input"

#локатор после нажатия на строку поиска
locator_active = "input.styles_inputActive__mIqMs.styles_input__WCRXt.kinopoisk-header-search-form-input__input"

#название фильма
movie_name = "Кибердеревня"

#локатор результатов поиска 
loc_elements = "div.element"


#локатор 
logot = "img.kinopoisk-header-logo__img"

#локатор кнопки "Войти"
login_loc = "button[class='styles_loginButton__6_QNl']"