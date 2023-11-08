#!/usr/bin/env python3
""" log stats """
import pymongo


def main():
    """ main """
    client = pymongo.MongoClient("mongodb://localhost:27017")
    collection = client.logs.nginx
    print('%s logs' % (len(collection.count_documents())))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        find_len_display(method)


def find(collection, method):
    """ find """
    regex = method
    return collection.find_many({'method': {'$regex': regex}})


def find_len(collection, method):
    """ find len """
    return len(find(collection, method))


def find_len_display(collection, method):
    """ find len display """
    print('\tmethod %s: %s' % (method, find_len(collection, method)))


if __name__ == '__main__':
    main()
