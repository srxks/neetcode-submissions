class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: list of int, int
        # output: list of int
        # given the list and our k, return k more frequent occuring elements in the list

        # dict to keep track of the freq
        # dict will hold a tuple [freq, val] as its value 
        # we will have a heap that keeps will hold the tuples 
        # we will pop k times and grab the value from the tuples and append them to our result


        freq = {}
        heap = []
        res = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for key, val in freq.items():
            newVal = (val, key)
            heapq.heappush(heap, newVal)
            if len(heap) > k:
                heapq.heappop(heap)

        for _ in range(k):
            val = heapq.heappop(heap)
            res.append(val[1])
        
        return res

        # runtime: 0(n^2logn + m + klogk)
        # space: O(n)

        # n: # of unique elms in nums
        # m: # of elms in nums
        # k: the value k

            
