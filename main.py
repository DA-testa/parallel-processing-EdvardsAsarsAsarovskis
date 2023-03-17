#Edvards Asars Asarovskis 221RDB328
from heapq import heappush, heappop

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    
    heap = []
    for i in range(n_workers):
        heappush(heap, (0, i))
    
    for i in range(n_jobs):
        started_at, worker = heappop(heap)
        print(worker, started_at)
        heappush(heap, (started_at + jobs[i], worker))

if __name__ == "__main__":
    main()
