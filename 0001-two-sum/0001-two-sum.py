class Solution(object):
    def twoSum(self, nums, target):
        output = []
        for i in range(len(nums)) :
            i_val = nums[i]
            for j in range(len(nums)) :
                j_val = nums[j]
                if i == j :
                    break
                if i_val + j_val == target :
                    output.append(i)
                    output.append(j)
                    return output

        