from cmath import sqrt
import heapq

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distant(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2).real

    def __lt__(self, other):
        return self.distant(Position(0, 0)) < other.distant(Position(0, 0))

    def __repr__(self):
        return f"Position({self.x}, {self.y})"


def hieu_truong_tham_ktx(k, vi_tri, ds_ktx):
    pq = []
    for ktx in ds_ktx:
        heapq.heappush(pq, ktx)
    res = []
    for i in range(k):
        res.append(heapq.heappop(pq))
    return res


if __name__ == "__main__":
    list_ktx = [Position(1, 0), Position(2, 1), Position(3, 6), Position(-5, 2), Position(1, -4)]
    res = hieu_truong_tham_ktx(3, Position(0, 0), list_ktx)
    print(res)
