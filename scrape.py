from playwright.sync_api import sync_playwright
import json

# name
# description
# calories
# fats
# carbs
# proteins
# unsatured_fats
# sugar
# salt
# portion

file = open('mcDonaldsMenu.json', 'w')

def run(playwright):
    browser = playwright.chromium.launch(
        headless=True
    )
    page = browser.new_page()
    domain = "https://www.mcdonalds.com"
    page.goto(domain + "/ua/uk-ua/eat/fullmenu.html")
    
    links = page.locator('a.cmp-category__item-link').all()

    items_list_to_dump = [] # list to dump into json file

    for link in links:
        p = browser.new_page()
        p.goto(domain + link.get_attribute('href'))

        name = p.locator('span.cmp-product-details-main__heading-title').nth(1).text_content()
        try:
            description = p.locator('.cmp-product-details-main__description .cmp-text').text_content().strip()
            if description.find('\xa0') != -1:
                description = description.replace('\xa0', ' ')
        except Exception as e:
            print(e)
            description = ''

        p.click('span.cmp-accordion__icon')  # Open the details section
        first_row = p.locator('div.cmp-nutrition-summary--primary')
        second_row = p.locator('div.cmp-nutrition-summary--nutrition-table')

        # Primary nutrition values
        items = first_row.locator('li.cmp-nutrition-summary__heading-primary-item')
        calories = items.nth(0).locator('span.value span[aria-hidden="true"]').first.text_content().strip()
        fats = items.nth(1).locator('span.value span[aria-hidden="true"]').first.text_content().strip()
        carbs = items.nth(2).locator('span.value span[aria-hidden="true"]').first.text_content().strip()
        proteins = items.nth(3).locator('span.value span[aria-hidden="true"]').first.text_content().strip()

        # Secondary nutrition values
        def get_secondary_value(metric_name):
            title = second_row.locator(f'li.label-item:has(span.metric:has-text("{metric_name}")) span.value span[aria-hidden="true"]').first.text_content().strip()
            return title.split(' ')[0].strip()

        unsatured_fats = get_secondary_value("НЖК:")
        sugar = get_secondary_value("Цукор:")
        salt = get_secondary_value("Сіль:")
        portion = get_secondary_value("Порція:")

        # # Print values
        # print(f"Калорії: {calories}")
        # print(f"Жири: {fats}")
        # print(f"Вуглеводи: {carbs}")
        # print(f"Білки: {proteins}")
        # print(f"Ненасичені жири (НЖК): {unsatured_fats}")
        # print(f"Цукор: {sugar}")
        # print(f"Сіль: {salt}")
        # print(f"Порція: {portion}")

        item = {
            name: {
                "description": description,
                "calories": calories,
                "fats": fats,
                "carbs": carbs,
                "proteins": proteins,
                "unsatured_fats": unsatured_fats,
                "sugar": sugar,
                "salt": salt,
                "portion": portion
            }
        }

        items_list_to_dump.append(item)

        print(f"Scraped: {name}\n")

        p.close()

    with open('mcDonaldsMenu.json', 'a', encoding='utf-8') as f:
        json.dump(items_list_to_dump, f, ensure_ascii=False, indent=4)

with sync_playwright() as playwright:
    run(playwright)