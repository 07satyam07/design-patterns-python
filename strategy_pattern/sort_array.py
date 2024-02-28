from sorting_algo import BubbleSort,QuickSort
from sorting_type import SortingType

class SortArray:
    def get_algorithme(self,algo_name):
        if algo_name==SortingType.BUBBLE:
            return BubbleSort()
        elif algo_name==SortingType.QUICK:
            return QuickSort()
    
    def sort(self,arr,algo_name):
        return self.get_algorithme(algo_name).sort(arr)
        

