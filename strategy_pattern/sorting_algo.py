from sorting import Sorting


class BubbleSort(Sorting):
    def sort(self,arr):
        arr.sort()
        print("BubbleSort")
        return arr

class QuickSort(Sorting):
    def sort(self,arr):
        arr.sort()
        print("QuickSort")
        return arr