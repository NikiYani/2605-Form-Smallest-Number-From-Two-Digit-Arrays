class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        for i in range(0, len(nums1)) :
            for j in range(0, len(nums2)) :
                if nums1[i] == nums2[j] :
                    return nums1[i]

        res = 0
        if nums1[0] >= nums2[0] :
            res = (nums1[0] + 10 * nums2[0])
        else :
            res = (nums2[0] + 10 * nums1[0])

        return res