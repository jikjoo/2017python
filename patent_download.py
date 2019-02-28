from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import sqlite3


error_pages = []
url = "http://kpat.kipris.or.kr/kpat/searchLogina.do?next=MainSearch#page1"
keyword="텔레비전+텔레비전+티브이+티이브이+티-브이+티부이+티비+텔레비젼+테레비전+테레비젼+태레비젼+태레비전+텔레비+테레비+텔리비죤+텔레비죤+영상표기장치+방송수신기+방송수신장치+영상수신장치+영상수신기+tv+tv set+television+catv+broadcast+broadcast+televi"
conn = sqlite3.connect("..\database\patent.db")

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)
 
browser.get(url)
print("뚜뚜 검색 페이지에 접근합니다.")

form = browser.find_element_by_css_selector("input#queryText.keyword")
form.clear()
form.send_keys(keyword)

#search = browser.find_element_by_css_selector("#SearchPara > fieldset > span.input_btn > a")
#search.click()
search = browser.execute_script("DoSearch()")

print("검색을 시작합니다.")
try:
    element = WebDriverWait(browser,10).until(
        EC.presence_of_all_elements_located((By.ID,"iconStatus"))
    )
    print("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")

#page = Select(browser.find_element_by_id("opt28"))
#page.select_by_value("90")
#browser.find_element_by_css_selector("#pageSel > a ").click()
page = browser.execute_script("setNumPerPage('90')")
print("page = 90")

try:
    element = WebDriverWait(browser,10).until(
        EC.presence_of_all_elements_located((By.ID,"divRealContent30"))
    )
    print("Page by 90 is ready!")
except TimeoutException:
    print ("Loading took too much time!")
browser.save_screenshot("2.png")

def search_info(bro = webdriver.PhantomJS(), i=int()):
    statuses = []
    titles = []
    stitles = bro.find_elements_by_class_name("stitle")
    ssearches = bro.find_elements_by_class_name("search_info_list")
    for stitle in stitles:
        status = stitle.text[0:2]
        statuses.append(status)
        num = stitle.text.find("]")
        title = stitle.text[num+2:]
        titles.append(title)
    
    j=0
    for ssearch in ssearches:
        ssearch = ssearch.text
        num0 = ssearch.find("IPC :")
        num1 = ssearch.find("출원인 :")
        num2 = ssearch.find("출원번호 :")
        num3 = ssearch.find("출원일자 :")
        num4 = ssearch.find("등록번호 :")
        num5 = ssearch.find("등록일자 :")
        num6 = ssearch.find("공개번호 :")
        num7 = ssearch.find("공개일자 :")
        num8 = ssearch.find("대리인 :")
        num9 = ssearch.find("발명자 :")
        IPC = ssearch[num0+6:num1-3]
        applicant = ssearch[num1+6:num2-1]
        app_num = ssearch[num2+7:num3-1]
        app_date = ssearch[num3+7:num4-1]
        reg_num = ssearch[num4+7:num5-1]
        reg_date = ssearch[num5+7:num6-1]
        public_num = ssearch[num6+7:num7-1]
        public_date = ssearch[num7+7:num8-1]
        agent = ssearch[num8+6:num9-1]
        inventor = ssearch[num9+6:]
        
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO patent (title,status,IPC,applicant,app_num,app_date,reg_num,reg_date,public_num,public_date,agent,inventor) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (titles[j],statuses[j],IPC,applicant,app_num,app_date,reg_num,reg_date,public_num,public_date,agent,inventor))
            conn.commit()
        except sqlite3.Error:
            print("Error : "+ titles[j])
            
        j+=1
    next_page = i + 1
    bro.execute_script("SetPageAjax('%d')" % next_page)

for i in range(260,1188):
    try:
        search_info(browser, i)
        element = WebDriverWait(browser,20).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME,"current"),str(i+1))
        )
        print("Page %d is ready!" % i)
        
    except TimeoutException:
        print ("Page %d Loading took too much time!" % i)
        error_pages.append(i)
browser.quit()
print(error_pages)
