import requests
import random
import datetime
from concurrent import futures


worker_url = [
	'http://localhost:5000/work/asia/0',
	'http://localhost:5000/work/asia/1',
	'http://localhost:5000/work/emea/0',
	'http://localhost:5000/work/us/0',
	'http://localhost:5000/work/us/1']

def fetch_page(url):
	requests.get(url)

def fun(urls):
	with futures.ThreadPoolExecutor() as executor:
		responses = executor.map(fetch_page, urls)
		return responses

def round_robin_fun(no_requests):
	urls = []
	for i in range (0, no_requests):
		urls.append(worker_url[i%5])

	responses = fun(urls)
