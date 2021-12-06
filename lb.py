import requests
import argparse
from random_policyy import *
from round_robin import *
from reg_rr import *
from weight_rr import *
from leastLatency import *
from leastConnection import *
worker_url = [
	'http://localhost:5000/work/asia/0',
	'http://localhost:5000/work/asia/1',
	'http://localhost:5000/work/emea/0',
	'http://localhost:5000/work/us/0',
	'http://localhost:5000/work/us/1']

region_url = [
    'http://localhost:5000/work/us',
    'http://localhost:5000/work/asia',
    'http://localhost:5000/work/emea',
]

random_url = 'http://localhost:5000/work'

def main():
    parser = argparse.ArgumentParser(description='Select policy and number of requests')
    parser.add_argument('-p',
        '--policy',
        help='Select a policy',
        choices=[
            "random",
          	"round_robin",
          	"reg_rr",
          	"weight_rr",
          	"leastLatency",
          	"leastConnection"                  
        ],
        required=True,
    )

    parser.add_argument("-n",required=True, type=int, help='Number of requests')

    args = parser.parse_args()

    no_requests = args.n
    start = datetime.datetime.now()

    if args.policy == "random":
        	random_fun(no_requests)
    elif args.policy == "round_robin":
        	round_robin_fun(no_requests)

    elif args.policy == "reg_rr":
        	reg_rr(no_requests)

    elif args.policy == "weight_rr":
        	weight_rr(no_requests)
    elif args.policy == "leastLatency":
        	leastLatency(no_requests)
    elif args.policy == "leastConnection":
        	leastConnection(no_requests)

    stop = datetime.datetime.now()
    #print("stop counting")
    interval = stop - start
    #print("time:");
    print(interval.total_seconds());
    
if __name__ == "__main__":
    main()

