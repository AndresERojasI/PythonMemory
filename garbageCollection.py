import ctypes
import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b:{1}'.format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

# We turn off the GC so we can see how reference counts are affected when the GC does not run and when it does (by running it manually).
gc.disable()

# Now we create an instance of A, which will, in turn, create an instance of B which will store a reference to the calling A instance.
my_var = A()

# As we can see A and B's constructors ran, and we also see from the memory addresses that we have a circular reference.
# 
# In fact `my_var` is also a reference to the same A instance:
print(hex(id(my_var)))

# Another way to see this:
print('a: \t{0}'.format(hex(id(my_var))))
print('a.b: \t{0}'.format(hex(id(my_var.b))))
print('b.a: \t{0}'.format(hex(id(my_var.b.a))))

a_id = id(my_var)
b_id = id(my_var.b)

# We can see how many references we have for `a` and `b`:
print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

# As we can see the A instance has two references (one from `my_var`, the other from the instance variable `b` in the B instance)
# 
# The B instance has one reference (from the A instance variable `a`)
# Now, let's remove the reference to the A instance that is being held by `my_var`:

my_var= None

print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

# As we can see, the reference counts are now both equal to 1 (a pure circular reference), and reference counting alone did not destroy the A and B instances - they're still around. If no garbage collection is performed this would result in a memory leak.
# Let's run the GC manually and re-check whether the objects still exist:

gc.collect()
print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

