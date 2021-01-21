class Solution:
    def twoSum(self, nums , target) :
        
        
        # a python dictionary(hash)
        # key is number
        # value is index of list: nums
        number_dictionary = dict()
        
        for index, number in enumerate(nums):
            
            # put every number into dictionary with index
            number_dictionary[ number ] = index
            
        # a list for index storage for i, index_of_dual that nums[i] + nums[index_of_dual] = target
        solution = list()
        
        for i in range( len(nums) ):
            
            value = nums[i]
            
            # compute the dual that makes value + dual = target
            dual = target - value
            
            index_of_dual =  number_dictionary.get( dual, None)

            if index_of_dual is not None and index_of_dual != i:
                # Note: we can't use the same element twice, thus return empty list
            
                # make a list for solution list
                solution = list([i, index_of_dual])
                
                break

            else:
                # if index_of_dual is None, keeps going to next iteration
                # Problem description says that each input would have exactly one solution
                continue
                

        # return index of nums that makes the sum equal to target
        return solution