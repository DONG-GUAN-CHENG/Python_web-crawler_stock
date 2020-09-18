# Python_web-crawler_stock
## 專案介紹
本專案以Yahoo奇摩股市為例，開發Python網頁爬蟲取得關注的股票當日行情，並且提供了四個方法(Method)， 包含：

* scrape() 
* save()
* export()
* gsheet()
* daily()

其中，'''js 
function myfunction(m1,m2) 
'''，scrape()方法(Method)為爬取關注的股票當日行情資料，而save()方法(Method)提供存入MySQL資料庫的功能，可以搭配[Python爬蟲教學]輕鬆學會Python網頁爬蟲與MySQL資料庫的整合方式部落格文章來進行學習。

另外，export()方法(Method)整合openpyxl套件，提供將Python網頁爬蟲所取得的股票當日行情資料，匯出成Excel檔案，並且在其中的漲跌欄位，客製化顯示儲存格的文字顏色，可以搭配[Python爬蟲教學]活用openpyxl套件將爬取的資料寫入Excel檔案部落格文章來進行學習。

而gsheet()方法(Method)則是透過Google Sheet API，將Python網頁爬蟲取得的股票當日行情資料，寫入雲端Google Sheet試算表中，可以搭配[Python爬蟲教學]解析如何串接Google Sheet試算表寫入爬取的資料部落格文章來進行學習。

最後，daily()方法(Method)整合Python的Selenium及BeautifulSoup套件，爬取台灣證券交易所的「個股日收盤價及月平均價」查詢式網頁，動態輸入查詢條件，並且爬取結果，可以搭配[Python爬蟲教學]想爬取查詢式網頁？你要學會使用Selenium及BeautifulSoup套件部落格文章來進行學習
