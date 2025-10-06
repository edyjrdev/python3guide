from libc.stdlib cimport qsort

cdef int compare(const void* a, const void* b) nogil:
   return (<int*>a)[0] - (<int*>b)[0]

def sort(int[:] values):
    qsort(&values[0], len(values), sizeof(int), compare)
