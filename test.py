import os
import subprocess


users=[1,10,50,100,300,500,1000,1500]
policies=[#'random',
    #'round_robin',
    #'reg_rr',
    #'weight_rr',
    'leastLatency',
    'leastConnection'
    ]

def some_func():
    for i in range(len(policies)):
        for j in range(6,7):
            meanSum = 0
            for k in range(0,4):
                string = "python3 lb.py -p " + policies[i] + " -n " + str(users[j])
                #os.system(string)
                timePolicy = float(subprocess.check_output(string, shell=True))
                meanSum += timePolicy

            meanPolicy = meanSum / 5
            solution = "%s, %s, %d" % (str(meanPolicy), policies[i], users[j])
            print(solution)

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    some_func()