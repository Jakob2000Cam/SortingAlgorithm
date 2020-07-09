

class Bubblesort:

    #def __init__(self, integer_list):
     #   self.intlist = integer_list

    def sort(self, integer_list):
        n = len(integer_list)
        while n > 1:
            for i in range(n-1):
                if integer_list[i] > integer_list[i+1]:
                    integer_list[i], integer_list[i+1] = integer_list[i+1], integer_list[i]
            n -= 1

        #print("Finished for length " + str(len(integer_list)))
        return integer_list




