import random
import time

import requests
from fake_useragent import UserAgent


def get_data(url, attempt=5):
    try:
        useragent = UserAgent().chrome
        headers = {
            "accept": "application/json, text/plain, */*",
            # "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
            # "accept-encoding": "gzip, deflate, br",
            "country-id": "12",
            "device": "pc",
            # "dnt": "1",
            "language": "ru_RU",
            # "authorization": "Bearer",
            "user-agent": f"{useragent}",
            # "user-hash": "dc194325-1682-48ba-a4a4-3901b2fb3c5d"
        }
        if attempt == 5:
            print(f'[INFO] start parsing -> {url} ... ', end='')
            time.sleep(random.randrange(1, 3))

        elif attempt != 5:
            print(f'[INFO] Attempt {attempt}: start parsing  -> {url} ... ', end='')
            time.sleep(random.randrange(10, 12))

        set_response = requests.get(url, headers=headers)
        st = set_response.json()
        if 'error' not in st:
            print('done!')
            return set_response

        else:
            print('Not done!')
            raise

    except Exception as _ex:
        if attempt != 1:
            return get_data(url=url, attempt=attempt - 1)
        else:
            return


def tree(url=None):
    url_default = "https://lalafo.kg/api/proxy/catalog/v3/categories/tree"
    if not url:
        url = url_default
    tree_info = get_data(url=url)
    return tree_info


def fullname(url=None):
    url_default = "https://lalafo.kg/api/proxy/catalog/categories/fullname"
    if not url:
        url = url_default
    fullname_info = get_data(url=url)
    return fullname_info


def katalog_id(katalogid, url=None):
    url_default = f"https://lalafo.kg/api/catalog/v32/categories/not-empty-links/{katalogid}"
    if not url:
        url = url_default
    katalog_info = get_data(url=url)
    return katalog_info


def get_page_data(katalogid, page_num, url=None):
    url_default = f"https://lalafo.kg/api/search/v3/feed/search?category_id={katalogid}&expand=url&page={page_num}"
    if not url:
        url = url_default
    katalog_info = get_data(url=url)
    return katalog_info


def main():
    # url = f"https://lalafo.kg/api/catalog/v32/categories/not-empppty-links/{1585}"
    func = tree()
    if type(func) == "str":
        pass
        # print(func.json())


if __name__ == '__main__':
    main()
