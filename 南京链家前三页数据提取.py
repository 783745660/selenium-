#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/6/22 16:05'
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()  #连接chorme
driver.get("https://nj.lianjia.com/") #进入目标url
driver.set_window_size(1366, 728) #窗口最大化
driver.find_element_by_link_text('二手房').click() #点击二手房
all_handles = driver.window_handles #获得当前已打开所有窗口的句柄
print(all_handles)
driver.switch_to.window(all_handles[-1]) #进入到二手房窗口
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(11) > div > div.list-more > dl:nth-child(1) > dd > a:nth-child(3) > span.name").click()
# driver.find_element(By.CSS_SELECTOR, ".hasmore:nth-child(1) a:nth-child(4) > .name").click()
driver.find_element(By.CSS_SELECTOR, ".hasmore:nth-child(2) a:nth-child(2) > .name").click()
driver.find_element(By.CSS_SELECTOR, "dl:nth-child(3) a:nth-child(2)").click()

# zongjias = driver.find_element(By.CSS_SELECTOR, "div.totalPrice > span")
ls_total_price = []
ls_areas = []
ls_unitprices = []

i = 1
while i < 4:
    time.sleep(5)
    '''01总价'''
    zongjias = driver.find_elements(By.XPATH, "//div[@class='totalPrice']/span")
    for zongjia in zongjias:
        #         print(zongjia.text)
        ls_total_price.append(zongjia.text)

    # mianji = driver.find_element(By.CSS_SELECTOR, "#content > div.leftContent > ul > li:nth-child(5) > div.info.clear > div.address > div").text
    # print(mianji.split('|')[2])
    '''02面积'''
    areas = driver.find_elements(By.XPATH, "//div[@class='address']/div")
    for area in areas:
        #         print(area.text.split('|')[2])
        ls_areas.append(area.text.split('|')[2])

    '''03均价'''
    # content > div.leftContent > ul > li:nth-child(1) > div.info.clear > div.priceInfo > div.unitPrice > span
    unitprices = driver.find_elements(By.XPATH, "//div[@class='unitPrice']/span")
    for unitprice in unitprices:
        #         print(unitprice.text[2:])
        ls_unitprices.append(unitprice.text[2:])

    driver.find_element_by_link_text('下一页').click()
    i += 1
print(ls_total_price)
print(ls_areas)
print(ls_unitprices)
ls = []
for i in range(len(ls_total_price)):
       dict1 = {}
       dict1['totalPrice'] = ls_total_price[i]
       dict1['area'] = ls_areas[i]
       dict1['utilPrice'] = ls_unitprices[i]
       ls.append(dict1)

xml = dicttoxml(ls,custom_root='Itemlist',attr_type=False,root=True) #dicttoxml接受可迭代对象并将它们视为列表

'''parseString方法创建一个XML解析器并解析xml字符串：DOM是Document Object Model的简称，
    它是以对象树来表示一个XML文档的方法，使用它的好处就是你可以非常灵活的在对象中进行遍历。
'''
dom = parseString(xml)
print(dom.toprettyxml())    #以xml的格式漂亮打印
file_name = '链家'
with open(file_name + ".xml", "w", encoding="utf8") as outfile:
    outfile.write(dom.toprettyxml())

# driver.get_screenshot_as_file('D:\\screenshot')