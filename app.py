class BookMyShow(object):
    __n = 0
    __m = 0
    __booked = []

    def __init__(self, n, m):
        """
        :type n: int
        :type m: int
        """
        self.__n = n
        self.__m = m
        self.__booked = [[0 for _ in range(m)] for _ in range(n)]
        

    def gather(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: List[int]
        """
        first_seat = None
        result = []
        remaining = k
        for row, seats in enumerate(self.__booked):
            if row > maxRow:
                break
            if self.__m < k:
                break
            if remaining == 0:
                break

            for idx, seat in enumerate(seats):
                if seat == 0 and first_seat == None and self.__m - (idx + 1) >= k:
                    first_seat = idx
                    result = [row, first_seat]
                    self.__booked[row][idx] = 1
                    remaining -= 1
                elif seat == 0 and first_seat != None and idx <= (k - 1):
                    self.__booked[row][idx] = 1
                    remaining -= 1

        return result
        

    def scatter(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: bool
        """
        remaining = k
        for row, seats in enumerate(self.__booked):
            if row > maxRow:
                break
            if remaining == 0:
                return True

            for idx, seat in enumerate(seats):
                if seat == 0 and self.__m - (idx + 1) <= k:
                    first_seat = idx
                    result = [row, first_seat]
                    self.__booked[row][idx] = 1
                    remaining -= 1
                elif seat == 0 and idx <= (k - 1):
                    self.__booked[row][idx] = 1
                    remaining -= 1

        print(self.__booked, k, maxRow)
        return False
        


# Your BookMyShow object will be instantiated and called as such:
obj = BookMyShow(2, 5)
param_1 = obj.gather(4,0)
print(param_1)