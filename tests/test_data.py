url = 'https://ya.ru/'


# Test 1 Checking the functionality of the search string

send_query_search_data = [
    ('картина'),
    ('корзина'),
    ('картонка'),
    ('маленькая собачонка')
]

# Test 2 Checking for elements on the page when changing the design
from selenium.common.exceptions import TimeoutException as ex

check_for_links_data = [
    (ex, 'Yandex Logo', '/html/body/main/div[1]/a'),
    (ex, 'Search Logo', '/html/body/main/div[2]/form/div[1]'),
    (ex, 'Voice request', '/html/body/main/div[2]/form/div[2]/div/div[1]'),
    (ex, 'Yandex Weather', '/html/body/main/div[2]/div/a[1]'),
    (ex, 'Yandex Traffic', '/html/body/main/div[2]/div/a[2]'),
    (ex, 'Other', '/html/body/main/div[2]/div/a[3]')
]

# Test 3 Verification of the transition on the link on the page

following_link_data = [
    ('Yandex Logo', '/html/body/main/div[1]/a', '/html/body'),
    ('Login', '/html/body/main/div[1]/div/a', '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]'),
    ('Yandex Weather', '/html/body/main/div[2]/div/a[1]', '/html/body/div[1]'),
    ('Yandex Traffic', '/html/body/main/div[2]/div/a[2]', '/html/body/div[1]/div[1]/ymaps/ymaps[1]/canvas'),
    ('Others', '/html/body/main/div[2]/div/a[3]', '/html/body/div[1]/div[2]/table')
]

