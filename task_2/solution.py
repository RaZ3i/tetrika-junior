import csv
from playwright.sync_api import sync_playwright, expect


def get_file():
    with sync_playwright() as p:
        char_dict = {}
        new_arr = []
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")

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

                for i in column:
                    temp = i.split(sep="\n")
                    for j in temp:
                        new_arr.append(j)

                page.get_by_role("link").and_(
                    page.get_by_text("Следующая страница")
                ).first.click(delay=1)

        except Exception:
            cursor = 1
            for i in new_arr:
                if len(i) == 1:
                    count = 0
                    for j in range(cursor, len(new_arr)):
                        if len(new_arr[j]) != 1:
                            count += 1
                        else:
                            cursor = j + 1
                            break
                    if char_dict.get(i):
                        char_dict[i] += count
                    else:
                        char_dict.update({i: count})

            with open("animals.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                for k, v in char_dict.items():
                    writer.writerow([f"{k}, {v}"])


if __name__ == "__main__":
    get_file()
