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

weights = [3, 2, 1]

def weight_rr(no_requests):
	urls = []

	#assign emea the highest weight
	for i in range(0, no_requests % 6):
		urls.append(worker_url[2])

	while no_requests > 0:
		for i in range(weights[0]):
			urls.append(worker_url[2])
		for i in range(weights[1]):
			urls.append(worker_url[3])
		for i in range(weights[0]):
			urls.append(worker_url[0])
		no_requests -= 6

	responses = fun(urls)
