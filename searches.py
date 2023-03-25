from wedding_class import wedding
import csv
import timeit
from collections import defaultdict
from quick_sort import quick_sort

def linear_search(array, elem):
    out = []
    for i in array:
        if i.wedding_date == elem:
            out.append(array.index(i))
    return out


def binary_search(array, elem, start, end):
    out = []
    if start > end:
        return []
    mid_pos = int((start + end) / 2)
    if array[mid_pos].wedding_date == elem:
        out.append(mid_pos)
    elif array[mid_pos].wedding_date > elem:
        out = binary_search(array, elem, start, mid_pos - 1)
    elif array[mid_pos].wedding_date < elem:
        out = binary_search(array, elem, mid_pos + 1, end)

    if len(out) == 0 or len(out) > 1:
        return out

    left_pos = out[0] - 1
    right_pos = out[0] + 1

    while (left_pos >= 0) and (right_pos < len(array)):
        if array[left_pos].wedding_date == elem:
            out.insert(0, left_pos)
            left_pos -= 1
        if array[right_pos].wedding_date == elem:
            out.append(right_pos)
            right_pos += 1
        else:
            return out

    return out

def bin_and_quick(array):
    out = quick_sort(array)
    s = binary_search(out, out[-1].wedding_date, 0, len(out) - 1)
    print(s)


tmp = []
with open('couples100000.csv', newline='') as state_file:
    reader = csv.reader(state_file)
    for i in reader:
        tmp.append(wedding(i[0], i[1], i[2], i[3], i[4], i[5]))

wdb = defaultdict(list)
for i in tmp:
    wdb[i.wedding_date].append(i)


t = timeit.Timer(lambda: wdb[tmp[-1].wedding_date])
tt = t.timeit(number = 1)
print(tt)

with open('time_test_multimap.csv', 'a', newline='', encoding="windows-1251") as state_file:
    writer = csv.writer(state_file)
    writer.writerow(["{} elements: {} seconds".format(len(tmp), tt)])




