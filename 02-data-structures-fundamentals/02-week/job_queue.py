#!/usr/bin/python3

'''Parallel Processing

Parallelism is the process of processing several set of instructions
simultaneously. It reduces the total computational time.

Simulate a program that processes a list of jobs in parallel. Given a list of
𝑛 independent threads and 𝑚 jobs, threads take jobs in order.

Determine for each job which thread will process it and when will it start
processing. Apply a priority queue to simulate prcessing of thread events at
the start and completion of a job.

##################################

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()

'''
import heapq

class Thread:
    '''Thread

    Threads sorted by release time.
    '''

    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time



class JobQueue:

    def read_data(self):
        self.num_threads, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.size = len(self.jobs)
        assert m == len(self.jobs)

    def write_response(self):
        for thread_id, start_time in self.result:
            print(thread_id, start_time)

    def assign_jobs(self):
        '''
        Assign jobs to threads.

        '''
        self.result = []
        self.thread_queue = [Thread(i) for i in range(self.num_threads)]

        for job in self.jobs:
            thread = heapq.heappop(self.thread_queue)

            self.result.append((thread.thread_id, thread.release_time))

            thread.release_time += job
            heapq.heappush(self.thread_queue, thread)


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
