'''
Status: Time limit exceeded / All cases passed.
https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2
'''
nums1 = [2, 1, 1, 0, 0, 5, 0, 3, 2, 0, 10]
nums2 = [2,3,1,1,4]
nums3 = [3,2,1,0,4]
nums_bad = [0]

def solution(nums):
    max_reach = [x+i for i,x in enumerate(nums)]
    def try_path(goal_id):
        if goal_id == 0:
            return True
        for id, reach in enumerate(max_reach[:goal_id]):
            if reach >= goal_id:
                if id == 0:
                    return True
                else:
                    return try_path(id)
        return False
    return try_path(len(nums)-1)

print(solution(nums1))
# print(solution(nums2))
# print(solution(nums3))
# print(solution(nums_bad))



