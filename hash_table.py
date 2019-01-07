# Find symmetric pairs in an array
def symmetric_pairs(array):
    visited = {}
    symm = []
    for a, b in array:
        if visited.get(b) == a:
            symm.append((a, b))
        else:
            visited[a] = b
    return symm


# Find if an array is a subset of another array
def is_subset(arr1, arr2):
    # swap to hash the longer array
    if len(arr1) > len(arr2):
        arr2, arr1 = arr1, arr2
    hash = {}
    for a in arr2:
        hash[a] = True
    for b in arr1:
        # found other key
        if b not in hash:
            # the problem of disjoint arrays is the same function except
            # the condition is not negated
            return False
    return True


# Trace complete path of a journey
def path_of_journey(tickets):
    count = {}
    # count number of times each airport is visited
    for src in tickets:
        dest = tickets[src]
        count[src] = count.get(src, 0) + 1
        count[dest] = count.get(dest, 0) + 1
    # start and finish will be visited once
    start = (k for k in count if count[k] == 1).next()

    def find_path(v, path=[]):
        if v is None: return path
        return find_path(tickets.get(v), path + [v])

    print ' -> '.join(find_path(start))


if __name__ == '__main__':
    journey = {
        'A': 'B',
        'C': 'D',
        'B': 'C',
        'F': 'G',
        'E': 'F',
        'D': 'E',
        'G': 'H',
        'H': 'I'
    }
    path_of_journey(journey)
