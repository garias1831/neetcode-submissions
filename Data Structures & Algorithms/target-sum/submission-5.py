class Solution:
    # Optimal leetcode solution
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Idea: ways[j] stores the number of ways to get to partial sum
        # j at index i in nums
        ways = defaultdict(int)
        ways[0] = 1

        
        for num in nums:
            next_dp = defaultdict(int)
            for total, count in ways.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            ways = next_dp
        
        return ways[target]
                

