# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:26:04 2021

@author: xie
"""
# =============================================================================
# import pytest
# 
# 
# class TestAdd:
#     #@pytest.mark.a
#     def test_case1(self):
#         a=3+4
#         assert 7==a
#     @pytest.mark.run(oder=2)
#     def test_case2(self):
#         b=5
#         assert 4==b
#     @pytest.mark.run(order=1)   
#     def test_case3(self):
#         c=7
#         assert 7==c
#         
# if __name__=='__main__':
#         #"-k",满足表达式的都会执行
#         #pytest.main(['-s',"-k case1 or case2"])
#         #--collect-only，只负责收集测试用例而不执行
#         #pytest.main(['-s',"--collect-only"])
#         #-m,运行标记为a的用例
#         pytest.main(['-s',"-m a"])
#         #pytest.main(['test_pytest.py::TestAdd::test_case1','-s'])
#         
#         #pytest.main(["-s"])
# 
# =============================================================================


def a():
    for i in range(5):
      print("before")
      yield i
      print("after")

p=a()
print(next(p))
print(next(p))
print(next(p))

