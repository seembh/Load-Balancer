import requests
import random
import datetime
from concurrent import futures


worker_url = [
	'http://localhost:5000/work/asia',

	'http://localhost:5000/work/emea',

	'http://localhost:5000/work/us']

def fetch_page(url):
	requests.get(url)

def fun(urls):
	with futures.ThreadPoolExecutor() as executor:
		responses = executor.map(fetch_page, urls)
		return responses

def reg_rr(no_requests):
	urls = []
	for i in range (0, no_requests):
		urls.append(worker_url[i%3])

	responses = fun(urls)
