#Q8. Why does __iter__() usually return self in most custom iterator implementations?

#Because the object itself is acting as the iterator.
def __iter__(self):
    return self

#Flow:
# for i in obj
#        ↓
# iter(obj)
#        ↓
# obj.__iter__()
#        ↓
# returns self
#        ↓
# next(obj)
#        ↓
#obj.__next__()

#If __iter__() doesn't return an iterator object, iteration will fail.
