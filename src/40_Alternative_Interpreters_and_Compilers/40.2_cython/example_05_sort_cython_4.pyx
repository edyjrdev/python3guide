cdef extern from "<stdlib.h>" nogil:
    void qsort (void *array, size_t count, size_t size, int (*compare)(const void *, const void *))

cdef int compare(const void* a, const void* b) nogil:
   return (<int*>a)[0] - (<int*>b)[0]

def sort(int[:] values):
    qsort(&values[0], len(values), sizeof(int), compare)

