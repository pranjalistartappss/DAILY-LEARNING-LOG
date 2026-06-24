for i in range(10):
    print(i)


#iterable  range, tuple,set, dictionary,(collectin of data)
#iterator = it is object fetch value once at a time 
#iterator protocol:iter():return iterator object and next(): return next value
#__init__= thunder method

it = iter(list1)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break

#memory efficiency: instead of loading an entire dataset(like 10 gb file) into memory
# at once , an iterator calculates and yields one item at a time 

# uniform interface: loop through different kinds of data using for 

# decoupled traversal state:data object stores only the data

#store current value and move to next value 

#custom iterator  = __init__, iter() , next()
# counting iterator 
class counter:
    def __init__(self,start,end):
        self.current = start
        self.end = end

    def __iter__(self):
        if self.current> self.end:
            raise StopIteration
        
        value  = self.current
        self.current += 1

        return value 
    
c = counter(1,5)

for i in c:
    print(i)