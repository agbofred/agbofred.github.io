"""
File: algorithms.py
Project 10.10

Updates to profile heap sort.  The heap now needs a reference
to the profiler so it can record comparisons and exchanges.

Algorithms configured for profiling.

"""

from profiler import Profiler
from arrayheap import ArrayHeap

def heapSort(lyst, profiler):
#Your code here
