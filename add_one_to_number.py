

class AddOneToNumber:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        list_input = list(A)
        is_all_nines = True

        for i, elem in enumerate(reversed(range(len(list_input)))):
            if list_input[elem] != 9:
                list_input[elem] += 1
                is_all_nines = False
                break
            else:
                list_input[elem] = 0

        if is_all_nines:
            list_input.insert(0, 1)

        return list_input