# -*- coding: utf-8 -*-
__author__ = "1041641 林子淇, 1041716 林裕翔"

from bs4 import BeautifulSoup
import requests
import json


def stock2330():
		doc = requests.get("https://tw.finance.yahoo.com/q/q?s=2330")
		soup = BeautifulSoup(doc.text, 'html.parser')

		mainTable = soup("table")[5]
		a = mainTable.findAll('td')[0]
		stockName = a.findAll('a')[0].string
		time = mainTable.findAll('td')[2].string
		deal = mainTable.findAll('td')[3].string
		buy = mainTable.findAll('td')[4].string
		sell = mainTable.findAll('td')[5].string
		fontSource = mainTable.findAll('font')[1]
		fontSource = str(fontSource)
		diff = fontSource[22:26]
		sellNumber = mainTable.findAll('td')[6].findAll('td')[0].string
		closingPrice = mainTable.findAll('td')[6].findAll('td')[1].string
		OpenPrice = mainTable.findAll('td')[6].findAll('td')[2].string
		Maximum = mainTable.findAll('td')[6].findAll('td')[3].string
		Minimum = mainTable.findAll('td')[6].findAll('td')[4].string

		stock2330 = [stockName, time, deal, buy, sell, diff, sellNumber, closingPrice, OpenPrice, Maximum, Minimum]

		return stock2330


def stock():
		doc2 = requests.get("https://www.wantgoo.com/stock")
		soup2 = BeautifulSoup(doc2.text, 'html.parser')
		
		price = soup2.find_all(class_='price')[0].string
		chg = soup2.find_all(class_='chg')[0].string
		pricePercent = soup2.find_all(class_='chg')[1].string
		vol = soup2.find_all(class_='vol')[0]
		final = vol.find('b').string

		stock = [price, chg, pricePercent, final]

		return stock