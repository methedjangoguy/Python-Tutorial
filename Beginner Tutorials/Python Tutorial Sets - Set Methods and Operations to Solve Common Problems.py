# Create a set with numbers 1 through 10
# Sets are unordered collections of unique elements
s1 = {1,2,3,4,5,6,7,8,9,10}
print(s1)

# Add single element 11 to the set
# add() method adds a single element to the set
s1.add(11)
print(s1)

# Add multiple elements 12-15 using update()
# update() method adds multiple elements from an iterable to the set
s1.update([12,13,14,15])
print(s1)

# Create another set s2 and update s1 with elements from s2
# update() can also add elements from another set
s2 = {2,3,4,5,99}
s1.update(s2)
print(s1)

# Remove element 99 using remove() - raises error if element not found
# remove() will raise KeyError if element is not found in set
s1.remove(99)
print(s1)

# Remove element 990 using discard() - no error if element not found
# discard() removes element if found, does nothing if not found
s1.discard(990)
print(s1)

# Remove and return an arbitrary element using pop()
# pop() removes and returns random element since sets are unordered
s1.pop()
print(s1)

# Create three sets for demonstrating set operations
set1 = {1,2,3}
set2 = {2,3,4}
set3 = {3,4,5}

# union() returns a set containing all unique elements from all sets
s4 = set1.union(set2, set3)
print(s4)
# intersection() returns a set containing elements common to all sets
s4 = set1.intersection(set2, set3)
print(s4)
# difference() returns elements in first set that are not in second set
s4 = set1.difference(set2)
print(s4)
# symmetric_difference() returns elements in either set but not in both
s4 = set1.symmetric_difference(set2)
print(s4)

# isdisjoint() returns True if two sets have no elements in common
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
# issubset() returns True if first set is a subset of second set
print(set1.issubset(set2))
print(set1.issubset(set3))

employees = ['James', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'James', 'John']
developers = ['Judy','James', 'Jane', 'April', 'Steven']
result = set(gym_members).intersection(developers)
print(result)
result = set(employees).difference(gym_members, developers)
print(result)
result = set(developers).union(gym_members)
print(result)

if 'James' in employees:
    print('James is an employee')
else:
    print('James is not an employee')

# Congratulations! You have completed Sets.
