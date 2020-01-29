import time

from selenium import webdriver

def main():
    browser = webdriver.Chrome()
    browser.get('https://search.jd.com/Search?keyword=%E6%83%85%E5%95%86&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=3&s=60&click=0')
    js="var q=document.documentElement.scrollTop = 10000"
    browser.execute_script(js)
    time.sleep(1)
    browser.execute_script(js)
    time.sleep(1)

    div = browser.find_element_by_id('J_goodsList')
    e = div.find_element_by_tag_name('ul').find_elements_by_tag_name('li')
    print(len(e))
    for i in e:
        tag = i.find_element_by_tag_name('div')
        title = tag.find_element_by_class_name('p-name').find_element_by_tag_name('a').get_attribute('title')
        print(title)

    # browser.close()
    time.sleep(1000)

if __name__ == '__main__':
    main()