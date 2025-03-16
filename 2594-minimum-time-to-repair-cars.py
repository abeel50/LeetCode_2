class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepair(time):
            repairedCars = 0
            for r in ranks:
                repairedCars += int(sqrt((time / r)))
                if repairedCars >= cars:
                    break
            return repairedCars >= cars

        left, right = 1, max(ranks) * cars * cars
        while left <= right:
            mid = (left + right) // 2
            if canRepair(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left   
