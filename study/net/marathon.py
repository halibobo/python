import bs4
from urllib import request
from bs4 import BeautifulSoup as bs
import xlwt
from xlwt import Workbook
from urllib.error import URLError, HTTPError
import threading, multiprocessing

def getRaceInfo(url):
    resp = request.urlopen(url)        
    html_data = resp.read().decode('utf-8')    
    soup = bs(html_data, 'html.parser')    

    race_list_div = soup.find_all('li',class_='race_detail_group')
    race_class_info = []

    for item in race_list_div:
        dicts = {}
        dicts['data-token'] = item['data-token']
        dicts['race-name'] = item.find_all('span')[0].text
        race_class_info.append(dicts)

    race_info_detail = []
    s = soup.title.text
    if len(s) > 6:
        title_dict = {}
        title_dict["race-name"] = s[0:-6]
        race_info_detail.append(title_dict)
    for item in race_class_info:
        if 'data-token' in item:
            race_dict = {}
            race_list_soup = soup.find_all('div',id=item['data-token'])
            race_dict['litle-race-name'] = item['race-name']
            for race_list_item in race_list_soup:
                race_soup = race_list_item.find_all('dl')
                for race_detail in race_soup:
                    race_dict[race_detail.dt.text] = race_detail.dd.text
            race_info_detail.append(race_dict)

    return race_info_detail

def wExcel():
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('马拉松', cell_overwrite_ok=True)
    row_index = 1

    for i in range(1,100):
        try:
            dicts = getRaceInfo('http://iranshao.com/races/%d' % i)
            for item in dicts:
                col = 0
                for race in item:
                    worksheet.write(row_index, col, item[race])
                    col = col +1
                    print(row_index,col)
                row_index = row_index +1
            row_index = row_index +1
        except HTTPError as e:
            print('Error code: ', e.code)
        except URLError as e:
            print('Reason: ', e.reason)
    workbook.save('marathon.xls')
wExcel()


# count = 1
# index = 1
# def main():
    
#     lock = threading.Lock()
#     workbook = xlwt.Workbook(encoding = 'utf-8')
#     worksheet = workbook.add_sheet('马拉松', cell_overwrite_ok=True)
#     def loop():
#         global count
#         global index
#         while count < 100:
#             try:
#                 dicts = getRaceInfo('http://iranshao.com/races/%d' % i)
#                 for item in dicts:
#                     col = 0
#                     for race in item:
#                         worksheet.write(index, col, item[race])
#                         col = col +1
#                     lock.acquire()
#                     index += 1
#                     lock.release()
#             except HTTPError as e:
#                 print('Error code: ', e.code)
#             except URLError as e:
#                 print('Reason: ', e.reason)
#             lock.acquire()
#             print(count)
#             count = count + 1
#             lock.release()
#         lock.acquire()
#         workbook.save('marathon.xls')
#         lock.release()
#         print('over-----------')
#     for i in range(8):
#         t = threading.Thread(target=loop)
#         t.start()
#         workbook.save('marathon.xls')
#         print('start-----------')
# main()
    
# getRaceInfo('http://iranshao.com/races/4078')
# getRaceInfo('http://iranshao.com/races/1745')

