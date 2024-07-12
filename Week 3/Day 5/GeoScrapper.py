# import requests as req
# from bs4 import BeautifulSoup as bsp
# import pandas as pd
# import time
# from selenium import webdriver
# import requests
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.edge.options import Options as EdgeOptions
# info = {  # uninitialized dictionary to use for later
#         'Name': [],
#         'Price': [],
#         'Image': [],
#         'Link':[]
#     }
# url = 'https://arynews.tv/'
# # Getting the navbar of the website
# soup = bsp(req.get(url).text, 'lxml')
# # getting the navbar of the website which has a ul tag with class 't4s-nav__ul t4s-d-inline-flex t4s-flex-wrap t4s-align-items-center'
# navbar = soup.find('ul', id='menu-main-menu-2')
# # In the ul there are li tag each tag has a href in the a tag
# links = navbar.find_all('li', class_ = 'menu-item menu-item-type-post_type menu-item-object-page menu-item-home current-menu-item page_item page-item-585351 current_page_item tdb-cur-menu-item menu-item-first tdb-menu-item-button tdb-menu-item tdb-normal-menu menu-item-585395')
# import requests
# from bs4 import BeautifulSoup as bsp
# import pandas as pd




# def generateMenu(url) -> list:
# # Getting the navbar of the website
#     response = requests.get(url)
#     soup = bsp(response.text, 'lxml')
#     if not response.ok:
#             print("Server responded with exit code:", response.status_code) # if scrapping is not allowed
#     else:
#         # Getting the navbar of the website which has a ul tag with class 't4s-nav__ul t4s-d-inline-flex t4s-flex-wrap t4s-align-items-center'
#         navbar = soup.find('ul', class_='menu')

#         # Ensure navbar was found
#         if navbar:
#             # # In the ul there are li tags, each tag has a href in the a tag
#             links = [a['href'] for a in navbar.find_all('a',class_ = 'open-section', href = True)]
#             links = links[2:6]
#             return links
#         else:
#             print("Navbar not found")
#             return []
    

# def generateNews(url) -> list:
 
#     response = requests.get(url)
#     if not response.ok:
#         print("Server responded with exit code:", response.status_code) # if scrapping is not allowed
#         return []
#     else:
#         soup = bsp(response.text, 'lxml')
#         board = soup.find('div', class_ = 'row video-list laodMoreCatNews')
#         news = [a['href'] for a in board.find_all('a',class_ = 'open-section', href = True)]
#         return news
    
         

# def scrapeData(link, info):
#     info['Link'].append(link)
#     response = requests.get(link)
#     if not response.ok:
#         print("Server responded with exit code:", response.status_code) # if scrapping is not allowed
#     else:
#         soup = bsp(response.text, 'lxml')
#         board = soup.find('div', class_ = 'column-right')

#         try:
#             category = board.find('div', class_ ='breadcrumb').text.strip()
#             print(category)
#             info['Category'].append(category)
#         except:
#             print('No Category')
#             info['Category'].append(' ')

    


# if __name__ == '__main__':
#     info = {
#     'Header': [],
#     'Summary': [],
#     'Details': [[]],
#     'Creation Date': [],
#     'Link' : [],
#     'Category' : [],
#     'Image' : []
#     }
#     url = 'https://www.geo.tv/'
#     navs = generateMenu(url)
#     news = []
#     for nav in navs:
#         news.append(generateNews(nav))

import requests
from bs4 import BeautifulSoup as bsp
import pandas as pd


def generateMenu(url) -> list:
    response = requests.get(url)
    soup = bsp(response.text, 'lxml')
    if not response.ok:
        print("Server responded with exit code:", response.status_code)
        return []
    else:
        navbar = soup.find('div', class_='menu-area')
        if navbar:
            links = [a['href'] for a in navbar.find_all('a', class_='open-section', href=True)]
            newLinks = links[2:6] + links[10:12] + links[13:15]
            print(newLinks)
            return newLinks
        else:
            print("Navbar not found")
            return []


def generateNews(url) -> list:
    response = requests.get(url)
    if not response.ok:
        print("Server responded with exit code:", response.status_code)
        return []
    else:
        soup = bsp(response.text, 'lxml')
        board = soup.find('div', class_='row video-list laodMoreCatNews')
        if board:
            news = [a['href'] for a in board.find_all('a', class_='open-section', href=True)]
            return news
        else:
            print("News board not found")
            return []


def scrapeData(link, info):
    response = requests.get(link)
    if not response.ok:
        print("Server responded with exit code:", response.status_code)
    else:
        soup = bsp(response.text, 'lxml')

    try:
        board = soup.find('div', class_='column-right')
        receipt = board.find('div', class_='content-area')

        title = board.find('div', class_='heading_H').find('h1').text.strip() if board.find('div', class_='heading_H') else 'No Title'
        summary = board.find('div', class_='except').text.strip() if board.find('div', class_='except') else 'No Summary'
        category = board.find('div', class_='breadcrumb').text.strip() if board.find('div', class_='breadcrumb') else 'No Category'
        date = board.find('p', class_='post-date-time').text.strip() if board.find('p', class_='post-date-time') else 'No Date'
        image = receipt.find('img', src=True)['src'] if receipt.find('img', src=True) else 'No Image'
        paragraphs = [p.text.strip() for p in receipt.find_all('p')] if receipt else []

        info['Header'].append(title)
        info['Summary'].append(summary)
        info['Category'].append(category)
        info['Creation Date'].append(date)
        info['Image'].append(image)
        info['Link'].append(link)
        info['Details'].append(paragraphs)
    except Exception as e:
        print(f"An error occurred while scraping data: {e}")


if __name__ == '__main__':
    info = {
        'Header': [],
        'Summary': [],
        'Details': [],
        'Creation Date': [],
        'Link': [],
        'Category': [],
        'Image': []
    }
    url = 'https://www.geo.tv/'
    navs = generateMenu(url)
    news = []
    for nav in navs:
        news.extend(generateNews(nav))

    for link in news:
        scrapeData(link, info)

    # Write dictionary to CSV file
    df = pd.DataFrame(info)
    df.to_csv('Geo.csv', index=False)








# import requests
# from bs4 import BeautifulSoup as bsp
# import pandas as pd


# def generateMenu(url) -> list:
#     # Getting the navbar of the website
#     response = requests.get(url)
#     soup = bsp(response.text, 'lxml')
#     if not response.ok:
#         print("Server responded with exit code:", response.status_code)  # if scrapping is not allowed
#         return []
#     else:
#         # Getting the navbar of the website which has a ul tag with class 'menu'
#         navbar = soup.find('div', class_='menu-area')

#         # Ensure navbar was found
#         if navbar:
#             # In the ul there are li tags, each tag has a href in the a tag
#             links = [a['href'] for a in navbar.find_all('a', class_='open-section', href=True)]
#             newLinks = links[2:6]
#             newLinks += (links[10:12])
#             newLinks += (links[13:15])
#             print(newLinks)
#             return newLinks
#         else:
#             print("Navbar not found")
#             return []


# def generateNews(url) -> list:
#     response = requests.get(url)
#     if not response.ok:
#         print("Server responded with exit code:", response.status_code)  # if scrapping is not allowed
#         return []
#     else:
#         soup = bsp(response.text, 'lxml')
#         board = soup.find('div', class_='row video-list laodMoreCatNews')
#         news = [a['href'] for a in board.find_all('a', class_='open-section', href=True)]
#         return news


# def scrapeData(link, info, i):
#     response = requests.get(link)
#     if not response.ok:
#         print("Server responded with exit code:", response.status_code)  # if scrapping is not allowed
#     else:
#         soup = bsp(response.text, 'lxml')
        

#     try:
#         board = soup.find('div', class_='column-right')
#         receipt = board.find('div', class_ = 'content-area')

#         try:
#             title = board.find('div', class_= 'heading_H').find('h1').text.strip()
#             print(title)
#             info['Header'].append(title)
#         except:
#             print('No Title')
#             info['Header'].append(' ')



#         try:
#             summary = board.find('div', class_ = 'except').text.strip()
#             print(summary)
#             info['Summary'].append(summary)
#         except:
#             print('No Summary')
#             info['Summary'].append(' ')




#         try:
#             category = board.find('div', class_='breadcrumb').text.strip()
#             print(category)
#             info['Category'].append(category)
#         except:
#             print('No Category')
#             info['Category'].append(' ')



#         try:
#             date = board.find('p', class_ = 'post-date-time').text.strip()
#             print(date)
#             info['Creation Date'].append(date)
#         except:
#             print('No Date')
#             info['Creation Date'].append(' ')
        


#         try:
#             image = receipt.find('img', src = True)['src']
#             print(image)
#             info['Image'].append(image)
#         except:
#             print('No Image')
#             info['Image'].append(' ')

        
#         try:
#             print(link)
#             info['Link'].append(link)
#         except:
#             print('No Link')
#             info['Link'].append(' ')

#         try:
#             paragraphs = receipt.find_all('p')
#             for paragraph in paragraphs:
#                 paragraph = paragraph.text.strip()
#                 print(paragraph)
#                 info['Details'][i].append(paragraph)
#             i+=1
#         except:
#             print('No Details')
#             info['Details'][i].append(' ')
#             i+=1
#     except:
#         pass

            


        



# if __name__ == '__main__':
#     info = {
#         'Header': [],
#         'Summary': [],
#         'Details': [[]],
#         'Creation Date': [],
#         'Link': [],
#         'Category': [],
#         'Image': []
#     }
#     url = 'https://www.geo.tv/'
#     navs = generateMenu(url)
#     news = []
#     i = 0
#     for nav in navs:
#         news.extend(generateNews(nav))

#     for link in news:
#         scrapeData(link, info, i)

#     # Write dictionary to CSV file
#     df = pd.DataFrame(info)
#     df.to_csv('Geo.csv')    






#     for link in news:
#         scrapeData(link, info)
    # for link in links:
    #     link = link.find('a')['href']
    # # adding the url to the links

    # for link in links:
    #     print(link)
    # def get_valid_proxies():
    #     proxy_list_url = 'https://free-proxy-list.net/'
    #     response = requests.get(proxy_list_url)
    #     soup = bsp(response.text, 'html.parser')
    #     proxy_data = []
    #     rows = soup.find_all('tr')[1:]
#     for row in rows:
#         columns = row.find_all('td')
#         if len(columns) >= 8:
#             ip_address = columns[0].text.strip()
#             google_enabled = columns[5].text.strip().lower() == 'yes'
#             https_enabled = columns[6].text.strip().lower() == 'yes'
#             last_checked = columns[7].text.strip()
#             if (last_checked.endswith('mins ago') and int(last_checked.split(' ')[0]) < 15) or last_checked.endswith('hours ago'):
#                 if google_enabled or https_enabled:
#                     proxy_data.append({'ip_address': ip_address, 'google_enabled': google_enabled, 'https_enabled': https_enabled})

#     return proxy_data

# def rotate_user_agent(proxy):
#     if proxy:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#             'http': f'http://{proxy}',
#             'https': f'https://{proxy}'
#         }
#     else:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
#         }
#     return headers
# # Scrapping the links one by one
# for link in links:
#     # Getting the navbar of the website
#     response = req.get(link)
#     if not response.ok:
#         print("Server responded with exit code:", response.status_code) # if scrapping is not allowed
    # else:
#         soup = bsp(response.content, 'html.parser')
#         # scrolling the page to the bottom above the footer then back up to load all the items until the end
#         driver = webdriver.Chrome()
#         driver.get(link)
#         Previous_Height = driver.execute_script("return document.body.scrollHeight")
#         while True:
#             # It will scroll to right above the footer of the page then scoll to the top then back to the bottom untill there is no new items being loaded
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 1000);")
#             time.sleep(5)
#             driver.execute_script("window.scrollTo(0, 0);")
#             time.sleep(5)
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 1000);")
#             time.sleep(5)
#             New_Height = driver.execute_script("return document.body.scrollHeight")
#             if New_Height == Previous_Height:
#                 break
#             Previous_Height = New_Height
#             # if there is a popup press the close button
#             try:
#                 driver.find_element_by_class_name('modal-close').click()
#             except:
#                 pass
            


#         # getting the html content of the page
#         html = driver.page_source
#         driver.quit()
#         # parsing the html content
#         soup = bsp(html, 'html.parser')
#         pretty = soup.prettify() # increasing readability
#         with open('scrapped.html', 'w', encoding='utf-8') as htmlFile:  # specify encoding method
#             htmlFile.write(pretty)


#         # getting the div with class 't4s-section-inner t4s_nt_se_template--16016591585354__main t4s_se_template--16016591585354__main t4s-container-fluid'
#         try:
#             products = soup.find_all('div', class_='t4s-product-wrapper')
#             # print(products)
#             for product in products:
#                 try:
#                     # getting name in h3 tag of class 't4s-product-title'
#                     name = product.find('h3', class_='t4s-product-title').text.strip()
#                     print(name)
#                     info['Name'].append(name)
#                 except:
#                     info['Name'].append(' ')

#                 try:
#                     # getting price from div with class 't4s-product-price'
#                     price = product.find('div', class_='t4s-product-price').text.strip()
#                     print(price)
#                     info['Price'].append(price)
#                 except:
#                     info['Price'].append(' ')

#                 try:
#                     # getting the href from div with class 't4s-product-btns t4s-col-2 t4s-col-lg-5'
#                     link = product.find('div', class_='t4s-product-btns t4s-col-2 t4s-col-lg-5').find('a')['href']
#                     print(url + link)
#                     info['Link'].append(url+link)
#                 except:
#                     info['Link'].append(' ')

#                 try:
#                     # getting image from div with class 't4s-product-img t4s_ratio is-show-img2'
#                     image = product.find('div', class_='t4s-product-img t4s_ratio is-show-img2').find('img')['src']
#                     print(image)
#                     info['Image'].append(image)
#                 except:
#                     info['Image'].append(' ')
#         except:
#             pass
# # print(info)
# # Write dictionary to CSV file
# df = pd.DataFrame(info)
# df.to_csv('Sapphire.csv')