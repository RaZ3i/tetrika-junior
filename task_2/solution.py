import time

from playwright.sync_api import sync_playwright, expect
import re

animal_arr = []
char_arr = []
char_dict = ()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=Африканские+линзанги#mw"
        "-pages"
    )

    try:
        while (
            expect(
                page.get_by_role("link")
                .and_(page.get_by_text("Следующая страница"))
                .first
            ).to_be_visible()
            is None
        ):

            all_columns = page.locator("#mw-pages > div.mw-content-ltr")
            column = all_columns.locator(".mw-category-group").all_inner_texts()
            count = 0
            for i in column:
                temp = i.split(sep="\n")
                for j in temp:
                    print(len(j))
                    if len(j) == 1 and j not in char_arr:
                        char_arr.append(j)
                    else:
                        count += 1
            page.get_by_role("link").and_(
                page.get_by_text("Следующая страница")
            ).first.click(delay=1)
        time.sleep(3)
        # print(set(char_arr))
    except Exception:
        print("БУКАВЫ", char_arr)
        time.sleep(3)

    # all_char = page.locator(
    #     "#mw-pages > div.mw-content-ltr > div > div > ul > li"
    # ).all()
    # i = 0
    # for i in all_char:
    #     char_arr.append(i.text_content()[0])
    #     print(i.text_content())

    # try:
    #     while (
    #         expect(
    #             page.get_by_role("link")
    #             .and_(page.get_by_text("Следующая страница"))
    #             .first
    #         ).to_be_visible()
    #         is None
    #     ):
    #
    #         all_char = page.locator(
    #             "#mw-pages > div.mw-content-ltr > div > div > ul > li"
    #         ).all_text_contents()[0]
    #
    #         for i in all_char:
    #             j
    #             if i!= all_char[-1]:
    #                 if i == i[+1]:
    #                     char_dict.update({i: })
    #             char_arr.append(i[0])
    #
    #         length = len(char_arr)
    #
    #         page.get_by_role("link").and_(
    #             page.get_by_text("Следующая страница")
    #         ).first.click(delay=1)
    #     time.sleep(3)
    #     print(char_arr)
    # except Exception:
    #     time.sleep(3)
