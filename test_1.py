# take two (int) lists as dictionary and find intersection
# of the lists

a = set([]) # convert list to set
b = set([])

def inter_list(a,b):
    c = a.intersection(b)
    return c

x = {1:2, 3:4, 5:6, 4:3}
y = set(x.keys())
z = set(x.values())

print(inter_list(y, z))