import requests
from bs4 import BeautifulSoup as bsp
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions



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