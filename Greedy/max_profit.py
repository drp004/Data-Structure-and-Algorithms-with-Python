def maxProfit(job):
    job = [[i, job[i][0], job[i][1]] for i in range(0, len(job))]
    job.sort(key=lambda x:x[2])

    jobs = []
    time = 0
    i = len(job)-1
    while i >= 0:
        if job[i][1] > time:
            jobs.append(job[i][0])
        i -= 1    
        time += 1 

    return jobs

job = [[4,20],[1,10],[1,40],[1,30]]
print(maxProfit(job))