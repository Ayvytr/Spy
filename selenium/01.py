from selenium import webdriver

def main():
    browser = webdriver.Chrome()
    browser.get('https://search.douban.com/book/subject_search?search_text=%E6%83%85%E5%95%86&cat=1001&start=0')
    # print(browser.page_source)
    # browser.close()
    # sc-bZQynM lfVmGy sc-bxivhb jDZFxE
    e = browser.find_elements_by_class_name('sc-bZQynM')
    print(len(e))
    print(e)
    for i in e:

        img = i.find_element_by_tag_name('a').find_element_by_tag_name('img')
        title = img.get_property('alt')
        photo = img.get_property('src')

        detail = i.find_element_by_css_selector('div.meta')
        print(detail.text)
        score = i.find_element_by_class_name('rating').find_element_by_class_name('rating_nums').text

        print(title, photo, score)

    browser.close()

if __name__ == '__main__':
    main()