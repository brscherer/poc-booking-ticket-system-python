from typing import List

class Node:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None
        self.total = 0
        self.mx = 0
        
class SegTree:
    def __init__(self, start, end, val):
        
        def build(l, r):
            if l > r:
                return None
            if l == r:
                node = Node(l, r)
                node.total = val
                node.mx = val
                return node
            node = Node(l, r)
            m = (l + r) // 2
            node.left = build(l, m)
            node.right = build(m+1, r)
            node.mx = max(node.left.mx, node.right.mx)
            node.total = node.left.total + node.right.total
            return node
        
        self.root = build(start, end)
    
    def update(self, index, val):
        
        def updateHelper(node):
            if node.s == node.e == index:
                node.total -= val
                node.mx -= val
                return
            m = (node.s + node.e) // 2
            if index <= m:
                updateHelper(node.left)
            elif index > m:
                updateHelper(node.right)
            node.mx = max(node.left.mx, node.right.mx)
            node.total = node.left.total + node.right.total
            return
            
        updateHelper(self.root)
        
    def maxQuery(self, k, maxRow, seats):
        
        def queryHelper(node):
            if node.s == node.e:
                if node.e > maxRow or node.total < k:
                    return []
                if node.e <= maxRow and node.total >= k:
                    return [node.e, seats - node.total]
            if node.left.mx >= k:
                return queryHelper(node.left)
            return queryHelper(node.right)
        
        return queryHelper(self.root)
                
    def sumQuery(self, endRow):
        
        def queryHelper(node, left, right):
            if left <= node.s and node.e <= right:
                return node.total
            m = (node.s + node.e) // 2
            if right <= m:
                return queryHelper(node.left, left, right)
            elif left > m:
                return queryHelper(node.right, left, right)
            return queryHelper(node.left, left, m) + queryHelper(node.right, m+1, right)
        
        return queryHelper(self.root, 0, endRow)
    
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m = m
        self.seg = SegTree(0, n-1, m)
        self.seats = [m] * n
        self.startRow = 0
        
    def gather(self, k: int, maxRow: int) -> List[int]:
        res = self.seg.maxQuery(k, maxRow, self.m)
        if res:
            row = res[0]
            self.seg.update(row, k)
            self.seats[row] -= k
        return res

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.seg.sumQuery(maxRow) < k:
            return False
        else:
            i = self.startRow
            total = 0
            while total < k:
                prevTotal = total
                total += self.seats[i]
                if total < k:
                    self.seg.update(i, self.seats[i])
                    self.seats[i] = 0
                    i += 1
                    self.startRow = i
                elif total >= k:
                    self.seg.update(i, k - prevTotal)
                    self.seats[i] -= k - prevTotal
            return True
        


obj = BookMyShow(5, 9)
obj.gather(10,1)
obj.scatter(3,3)
param_1 = obj.gather(9,1)
print("\nRESULT\n")
print(param_1)