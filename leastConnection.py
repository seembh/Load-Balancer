import requests
import random
import datetime
from concurrent import futures

worker_url = [
    'http://localhost:5000/work/asia/0',
    'http://localhost:5000/work/emea/0',
    'http://localhost:5000/work/us/0']

def fastestTime():
    
    resps = []
    
    resps.append(requests.get(worker_url[0]))
    min_latency = resps[0].json()["response_time"]
    min_url = 0
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

weights = [5, 2, 1]
sum_weight =sum (weights) 
def leastConnection(no_requests):
    urls = []
    fastest = fastestTime()
    for i in range(0, no_requests % sum_weight):
        urls.append(worker_url[fastest])
    no_requests -= no_requests % sum_weight
    x = 1
    while no_requests > 0:
        if(x % 50 == 0):
            fastest = fastestTime()
            for i in range(weights[1]):
                urls.append(worker_url[fastest])
            for i in range(weights[0]):
                urls.append(worker_url[2])
            for i in range(weights[2]):
                urls.append(worker_url[0])
            no_requests -= sum_weight
            x = 1

        else:
            x+=1
            for i in range(weights[0]):
                urls.append(worker_url[fastest])
            for i in range(weights[1]):
                urls.append(worker_url[2])
            for i in range(weights[2]):
                urls.append(worker_url[0])
            no_requests -= sum_weight

    responses = fun(urls)
    
    
