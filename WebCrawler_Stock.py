
## 建立股票類別
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time #計時暫停用


class Stock:
    def __init__(self, *stock_numbers): #利用*arg 來將引數收集到一個tuple中，為了後續利用 for迴圈對他進行迭代，**kwargs是來拆解參數鍵與值的dict

        self.stock_numbers = stock_numbers #使用類別自己的變數、函數都須要加上『 self.變數名稱 』才能使用！

    def date(self, year, month): #自定義函數date，包含股市年份及月份
        browser = webdriver.Chrome(ChromeDriverManager().install()) #用webdriver的chrome類別來建立瀏覽器物件，並以drivermanager去自動下載瀏覽器的對應版本
        browser.get("https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html") #用get方法來連到指定網站

        select_year = Select(browser.find_element_by_name("yy")) #利用selenium中的find_element_by_name來進行元素定位，並建立下拉選單的物件
        select_year.select_by_value(year)  # 選擇傳入的年份，由使用者傳入所需年份

        select_month = Select(browser.find_element_by_name("mm"))
        select_month.select_by_value(month)  # 選擇傳入的月份

        stockno = browser.find_element_by_name("stockNo")  # 定位股票代碼輸入框

        result = [] #創建空串列來儲存擷取到的資訊

        for stock_number in self.stock_numbers:
            stockno.clear()  # 清空股票代碼輸入框
            stockno.send_keys(stock_number) #來模擬輸入資料
            stockno.submit() #並呼叫submit方法來送出key

            time.sleep(2) #給網頁跑的空擋，暫停

            soup = BeautifulSoup(browser.page_source, "lxml")#page_source 網頁原始碼，從serve端的response進行解析

            #find()方法(Method)來進行定位
            table = soup.find("table", {"id": "report-table"}) #以find來進行定位

            #利用beautifulsoup套件的find_all()方法(Method)，取得表格(table)下所有的資料欄位
            elements = table.find_all("td", {"class": "dt-head-center dt-body-center"}) #以find_all方法來取得所有資料欄位

            #為了能夠區別每檔股票的資料，所以增加了股票代碼，並且與爬取的「日收盤價及月平均價」轉型為元組(Tuple)打包起來，儲存至result串列(List)中。
            data = (stock_number,) + tuple(element.getText() for element in elements)

            result.append(data) #以空串列去儲存每筆股市資料的結果依序存入

        print(result)

## 執行代碼
stock = Stock('2330', '2454', '0056')  # 建立Stock物件，並傳入想爬取的股票代碼
stock.date("2019", "9")  # 呼叫class內的的函數，來動態爬取指定的年月份中，股票代碼的每日收盤價
