class item:
    def __init__(self, id, mark, time):
        self.id = id
        self.mark = mark
        self.time = time

ids = [1, 2, 3, 4, 5]
marks = [4, 6, 5, 4, 3]
times = [2, 5, 4, 5, 6]
items = [item(num, mark, time) for num, mark, time in zip(ids, marks, times)]

def knapsack(items, maxtime):
    items = sorted(items, key=lambda item: item.mark / item.time, reverse=True)
    i = tot_time = tot_marks = 0
    while True:
        if tot_time + items[i].time < maxtime:
            tot_marks += items[i].mark
            tot_time += items[i].time
        else:
            ratio = (maxtime - tot_time) * items[i].mark / items[i].time
            tot_marks += ratio
            tot_time = maxtime
            print(ratio)
            break   
        print(items[i].mark)
        i += 1
    print(tot_marks)    

knapsack(items, 15)