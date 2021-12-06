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

def fastestTime():
    
    resps = []
    
    resps.append(requests.get(worker_url[0]))
    min_latency = resps[0].json()["response_time"]

    for i in range(len(worker_url)):
        resps.append(requests.get(worker_url[i]))
        if resps[i].json()["response_time"] < min_latency:
            min_url = i
            min_latency = resps[i].json()["response_time"]

    return min_url

def fetch_page(url):
    requests.get(url)

def fun(urls):
    with futures.ThreadPoolExecutor() as executor:
        responses = executor.map(fetch_page, urls)
        return responses

def leastLatency(no_requests):
    urls = []
    fastest = fastestTime()

    while no_requests > 0:
        urls.append(worker_url[fastest])
        no_requests -= 1

    responses = fun(urls)