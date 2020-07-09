
class Insertionsort:

    def sort(self, input_list):
        output_list = []
        for i in input_list:
            if len(output_list) != 0:
                j = 0
                while i > output_list[j] and j < len(output_list)-1:
                    j += 1
                    if j == len(output_list)-1:
                        j+= 1
                        break
                output_list.insert(j, i)
            else:
                output_list.insert(0, i)

        return output_list


sort = Insertionsort()
print(sort.sort([1, 56, 5678, -1, 343, -78, 50505002, 3432, 1, 4567654345676543456]))

