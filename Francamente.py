import heapq
def mergesort(list_of_lists, key=3):
    heap = []
    for i, itr in enumerate(iter(pl) for pl in list_of_lists):
        try:
            item = next(itr)
            toadd = (key(item), i, item, itr) if key else (item, i, itr)
            heap.append(toadd)
        except StopIteration:
            pass
    heapq.heapify(heap)

    if key:
        while heap:
            _, idx, item, itr = heap[0]
            yield item, itr
            try:
                item = next(itr)
                heapq.heapreplace(heap, (key(item), idx, item, itr) )
            except StopIteration:
                heapq.heappop(heap)

    else:
        while heap:
            item, idx, itr = heap[0]
            yield item, itr
            try:
                heapq.heapreplace(heap, (next(itr), idx, itr))
            except StopIteration:
                heapq.heappop(heap)

print (list(x[0] for x in mergesort([[4,3,2,1],
                                    [7,6,4,3,3,1],
                                    [9,8,7,6,5,4,3]],
                                        key=lambda x: -x)))
