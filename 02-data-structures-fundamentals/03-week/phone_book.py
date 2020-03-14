#!/usr/bin/python3

'''Phone Book

Implement a simple phone book manager that can process the following user
queries:

∙ add number name - add a person with name (name) and phone number (number) to
    the phone book. If the name and number exists already, the manager
    overwrites the corresponding name.
∙ del number - the manager erases the name with number (number) from the phone
    book. If there is no such name, it ignores the query.
∙ find number - look for a person with phone number (number). The manager
    replies with the appropriate name, or with string “not found".

'''

''' naive query
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
'''

class PhoneBook:
    def __init__(self):
        self.n = 0
        self.queries = []
        self.book = [None] * (10 ** 7)

    def add(self, number, name):
        self.book[number] = name

    def delete(self, number):
        self.book[number] = None

    def find(self, number):
        name = self.book[number]
        if not name:
            return 'not found'
        else:
            return name

    def solve(self):
        self.n = int(input())
        self.queries = [input() for i in range(self.n)]
        self.processQueries()

    def processQueries(self):
        for query in self.queries:
            q = query.split()
            command, number = q[0], int(q[1])
            if command == 'add':
                self.add(number, q[2])
            elif command == 'del':
                self.delete(number)
            else:
                print(self.find(number))

if __name__ == '__main__':
    x = PhoneBook()
    x.solve()
