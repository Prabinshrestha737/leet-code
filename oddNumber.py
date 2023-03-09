class Solution:
    
    def countOdds(self, low: int, high: int) -> int:
        return (high-low)//2 + int(not(low % 2 == 0 and high % 2 == 0))
