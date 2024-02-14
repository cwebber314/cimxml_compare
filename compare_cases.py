"""Compare two cases
"""
import pypowsybl.network as pn
import pandas as pd

n1 = pn.load('case1/case1.xml')
n2 = pn.load('case2/case2.xml')

# TODO: Port over from compare_cases.ipynb