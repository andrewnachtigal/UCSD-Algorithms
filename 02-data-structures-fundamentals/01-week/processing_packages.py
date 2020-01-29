#!/user/bin/python3

'''Network Packet Processing
Implement a program to simulate network packet processing.

Input:
The first line of the input contains the size 𝑆 of the buffer and the number 𝑛
of incoming network packets. Each of the next 𝑛 lines contains two numbers.
𝑖-th line contains the time of arrival 𝐴𝑖 and the processing time 𝑃𝑖
(both in milliseconds) of the 𝑖-th packet.


'''
# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        return Response(False, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
