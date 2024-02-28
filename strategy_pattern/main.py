# Import necessary classes from modules
from sort_array import SortArray
from sorting_type import SortingType

# Initialize an array to be sorted
arr = [4, 3, 2, 1]

# Create an instance of SortArray class
sort = SortArray()

# Sort the array using the Bubble Sort algorithm
sort.sort(arr, SortingType.BUBBLE)

# Sort the array using the Quick Sort algorithm
sort.sort(arr, SortingType.QUICK)
