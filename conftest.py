# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 22:32:00 2021

@author: xie
"""
import pytest 

def pytest_collection_modifyitems(items):
    print(items)
    print(type(items))
    for item in items:
        if "case" in item.nodeid:
            item.add_marker(pytest.mark.a)
   