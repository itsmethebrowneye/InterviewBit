class MaxSumContigiousArray:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        list_input = list(A)
        current_sum = 0
        max_sum = float('-inf')

        for num in list_input:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum