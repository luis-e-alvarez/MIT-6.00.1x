class Sort:
    def swap(self, array, smallIndex, bigIndex):
        temp = array[smallIndex]
        array[smallIndex] = array[bigIndex]
        array[bigIndex] = temp
    def partition(self, array, left, right):
        index = int((left + right)/2)
        i = left
        j = right
        pivot = array[index]
        while(i <= j):
            while(array[i] < pivot):
                i += 1
            while(array[j] > pivot):
                j -= 1
            if(i <= j):
                self.swap(array, i, j)
                i += 1
                j -= 1
        return i
    def quickSort(self, array, left, right):
        if(len(array) > 1):
            index = self.partition(array, left, right)
            if(left < index - 1):
                self.quickSort(array, left, index - 1)
            if(right > index):
                self.quickSort(array, index, right)
        print(array)
        return array