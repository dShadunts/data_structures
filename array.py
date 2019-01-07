class Array(list):
    # Find the second minimum element of an array with one traversal
    def second_min(self):
        minimum = float('inf')
        second = float('inf')
        for item in self:
            if item < minimum:
                second = min
                minimum = item
            elif item < second:
                second = item
        return second

    # Find first non-repeating integers in an array
    def first_unique(self):
        for item in self:
            if self.count(item) == 1:
                return item
        return None

    # Merge two sorted arrays
    def merge_sorted(self, other):
        len1 = len(self)
        len2 = len(other)
        result = []
        i = 0
        j = 0
        # while there are elements in both lists push lowest to the result
        while i < len1 and j < len2:
            if self[i] < other[j]:
                result.append(self[i])
                i += 1
            else:
                result.append(other[j])
                j += 1
        # reached the end of self => concat remaining part of other
        if i == len1:
            result = result + other[j:]
        # reached the end of other => concat remaining part of self
        elif j == len2:
            result = result + self[i:]
        return result

    # utility function which swaps two elements in the array
    def swap(self, i, j):
        tmp = self[i]
        self[i] = self[j]
        self[j] = tmp

    # Rearrange positive and negative values in an array
    # so that positives are on even indexes,
    # if there are more positives or negatives they appear at the end
    # time complexity: O(n)
    # extra space usage: O(1)
    def rearrange_postives_negatives(self):
        n = len(self)
        # first of all separate positives and negatives
        j = -1
        for i in range(n):
            if self[i] < 0:
                j += 1
                self.swap(i, j)
        # starting from j+1 all items are positive
        pos_index = j + 1
        neg_index = 0
        while n > pos_index > neg_index and self[neg_index] < 0:
            # swap each positive number with every other negative,
            # so that positives are on even indexes
            self.swap(pos_index, neg_index)
            pos_index += 1
            neg_index += 2
        return self
