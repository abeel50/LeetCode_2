class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        def isContinuous(max_val, min_val):
            return abs(max_val - min_val) <= 2

        res = 0
        max_deque = deque()
        min_deque = deque()
        start = 0

        for end in range(len(nums)):
            while max_deque and nums[end] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[end])

            while min_deque and nums[end] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[end])

            while not isContinuous(max_deque[0], min_deque[0]):
                if nums[start] == max_deque[0]:
                    max_deque.popleft()
                if nums[start] == min_deque[0]:
                    min_deque.popleft()
                start += 1

            res += end - start + 1

        return res
