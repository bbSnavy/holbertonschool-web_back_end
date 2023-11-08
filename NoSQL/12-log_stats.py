#!/usr/bin/env python3
""" log stats """
import pymongo


def main():
    """ main """
    client = pymongo.MongoClient("mongodb://localhost:27017")
    collection = client.logs.nginx
    print('%s logs' % (collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        find_len_display(collection, method)
    status = [
        v
        for v
        in collection.find({'method': 'GET', 'path': '/status'})
    ]
    print('%s status check' % (len(status)))


def find(collection, method):
    """ find """
    regex = method
    return collection.find({'method': {'$regex': regex}})


def find_len(collection, method):
    """ find len """
    return len([v for v in find(collection, method)])


def find_len_display(collection, method):
    """ find len display """
    print('\tmethod %s: %s' % (method, find_len(collection, method)))


if __name__ == '__main__':
    main()
