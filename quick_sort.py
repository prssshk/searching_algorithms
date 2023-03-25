from wedding_class import wedding
import csv
import time



def quick_sort(array):
    if len(array) < 2:
        return array
    ch_elem = array[len(array) // 2]

    lt_ch_elem = list(filter(lambda x: x < ch_elem, array))
    eq_ch_elem = list(filter(lambda x: x == ch_elem, array))
    gt_ch_elem = list(filter(lambda x: x > ch_elem, array))

    return quick_sort(lt_ch_elem) + eq_ch_elem + quick_sort(gt_ch_elem)


tmp = []
with open('couples100000.csv', newline='') as state_file:
    reader = csv.reader(state_file)
    for i in reader:
        tmp.append(wedding(i[0], i[1], i[2], i[3], i[4], i[5]))

start = time.time()
out = quick_sort(tmp)
end = time.time() - start

with open('time_test.csv', 'a', newline='', encoding="windows-1251") as state_file:
    writer = csv.writer(state_file)
    writer.writerow(["{} elements: {} seconds".format(len(out), end)])

with open('couples100000_sorted.csv', 'a', newline='', encoding="windows-1251") as state_file:
    writer = csv.writer(state_file)
    for i in out:
        writer.writerow([i.male, i.male_bday, i.female, i.female_bday, i.wedding_date, i.zags_number])
