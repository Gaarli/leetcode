class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hm = {}

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i],0)+1
        
        maxfreq = 0
        for key,value in hm.items():
            if value>maxfreq:
                maxfreq = value
        
        count = 0
        for key,value in hm.items():
            if value==maxfreq:
                count+=1
        
        return count*maxfreq