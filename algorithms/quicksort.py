class Quicksort:

    @staticmethod
    def partition(input_list, low, high):
        i = (low - 1)
        pivot = input_list[high]
        for j in range(low, high):
            if input_list[j] <= pivot:
                i = i + 1
                input_list[i], input_list[j] = input_list[j], input_list[i]
        input_list[i + 1], input_list[high] = input_list[high], input_list[i + 1]
        return (i + 1), input_list

    def sort(self, input_list, low=0, high=None):
        if high == None:
            high = len(input_list) - 1
        if low < high:
            partition_index, input_list = self.partition(input_list, low, high)
            self.sort(input_list, low, partition_index - 1)
            self.sort(input_list, partition_index + 1, high)
        return input_list
