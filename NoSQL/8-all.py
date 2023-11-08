#!/usr/bin/env python3
""" list all """
import pymongo


def list_all(mongo_collection) -> list:
    """ list all """
    return mongo_collection.find()
