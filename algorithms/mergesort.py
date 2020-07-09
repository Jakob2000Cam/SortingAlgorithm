# borrowed some code for the merge method from https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea
# had similar logic before but couldn't be bothered to debug

class Mergesort:
    @staticmethod
    def merge(left, right):
        if len(left) == 0:
            return right
        elif len(right) == 0:
            return left

        index_left = index_right = 0
        list_merged = []
        list_len_target = len(left) + len(right)
        while len(list_merged) < list_len_target:
            if left[index_left] <= right[index_right]:
                list_merged.append(left[index_left])
                index_left += 1
            else:
                list_merged.append(right[index_right])
                index_right += 1

            if index_right == len(right):
                list_merged += left[index_left:]
                break
            elif index_left == len(left):
                list_merged += right[index_right:]
                break

        return list_merged

    @staticmethod
    def split(input_list):
        if len(input_list) > 1:
            middle = len(input_list) // 2
            return input_list[:middle], input_list[middle:]
        else:
            return input_list[0], None

    def sort(self, input_list):

        length = len(input_list)

        left, right = self.split(input_list)
        # print(left, right)
        if len(left) > 1:
            left = self.sort(left)

        if right != None:
            if len(right) > 1:
                right = self.sort(right)

        return self.merge(left, right)
