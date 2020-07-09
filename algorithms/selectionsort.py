
class Selectionsort:

    def sort(self, input_list):
        sorted_list = []
        while len(input_list) != 0:
            index = 0
            smallest = input_list[0]
            for i in range(len(input_list)):
                if input_list[i] < smallest:
                    smallest = input_list[i]
                    index = i

            input_list.pop(index)
            sorted_list.append(smallest)

        return sorted_list
