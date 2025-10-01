from collections import Counter

def count_matching_elements(arr1, arr2):
    freq1 = Counter(arr1)
    freq2 = Counter(arr2)
    common_elements = set(freq1.keys()) & set(freq2.keys())
    return sum(min(freq1[element], freq2[element]) for element in common_elements)

def count_min_in_range(arr, range_obj):
    if not arr:
        return 0
    
    start, end_index = range_obj.start, range_obj.stop
    subarray = arr[start:end_index]
    
    if not subarray:
        return 0
    
    min_val = min(subarray)
    return subarray.count(min_val)

def elements_in_range(arr, range_obj):
    range_set = set(range(range_obj.start, range_obj.stop))
    return [element for element in arr if element in range_set]

def positive_negative_elements(arr):
    positive = [element for element in arr if element > 0]
    negative = [element for element in arr if element < 0]
    return positive + negative

def count_sum_elements(arr):
    sums = set()
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            sums.add(arr[i] + arr[j])
    
    return len(set(arr) & sums)
