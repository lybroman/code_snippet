import math

class SegmentTreeRangeSum(object):
    def __init__(self, arr):
        self.arr = arr
        self.size = pow(2, int(math.ceil(math.log(len(arr), 2)))) * 2 - 1
        self.sgt = [0] * self.size
        self._build(0, 0, len(arr) - 1)

    def _build(self, idx, start, end):
        if start == end:
            self.sgt[idx] = self.arr[start]
        else:
            mid = (start + end) // 2
            self._build(2 * idx + 1, start, mid)
            self._build(2 * idx + 2, mid + 1, end)

            self.sgt[idx] = self.sgt[2 * idx + 1] + self.sgt[2 * idx + 2]

        return self.sgt[idx]


    def update(self, idx, val):
        self._update(idx, val - self.arr[idx], 0, len(self.arr) - 1)


    def _update(self, idx, diff, cs, ce):
        if  (ce < idx) | (idx < cs):
            return
        self.sgt[idx] += diff
        if cs != ce:
            mid = (cs + ce) // 2
            self._update(2 * idx + 1, diff, cs, mid)
            self._update(2 * idx + 1, diff, mid + 1, ce)


    def query(self, start, end):
        return self._query(0, start, end, 0, len(self.arr) - 1)


    def _query(self, idx, qs, qe, cs, ce):
        if (qs <= cs) & (qe >= ce):
            return self.sgt[idx]
        elif  qe < cs or qs > ce:
            return 0
        else:
            mid = (cs + ce) // 2
            return self._query(2 * idx + 1, qs, qe, cs, mid) + self._query(2 * idx + 2, qs, qe, mid + 1, ce)



sgt = SegmentTreeRangeSum([1,2,3,4,5,6,7,8,9])
print(sgt.query(0,9))
sgt.update(0, 1)
print(sgt.query(0,9))