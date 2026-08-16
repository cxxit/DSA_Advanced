from _01_data_structures.referential_array import ArrayR
from _01_data_structures.adts.list_adt import List, T

class ArrayList(List[T]): 
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None: 
        """_summary_

        Args:
            max_capacity (int): _description_
        """
        List.__init__(self) 
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def __newsize(self):
        """Return the next capacity for the backing array when growth is needed.
        This helper was generated with the assistance of ChatGPT.
        This method calculates a larger array size based on the current capacity.
        The growth policy expands the array with a rate of 1.125 and a fixed extra
        amount, which helps avoid frequent resizing while keeping memory usage
        reasonable.

        Returns:
            int: The new capacity to allocate for the underlying array.
        """
        oldsize = len(self.array)

        if oldsize == 0:
            return 4

        newsize = oldsize + (oldsize // 8) + 6

        return newsize

    def __setitem__(self, index: int, item: T) -> None: 
        if index < 0 or len(self) <= index: 
            raise IndexError('Out of bounds access in array.')
        self.array[index] = item 


    def __getitem__(self, index: int) -> T: 
        if index < 0 or len(self) <= index: 
            raise IndexError('Out of bounds access in array.')
        return self.array[index]

    def append(self, item: T) -> None: 
        self.insert(self.length, item)

    def insert(self, index: int, item: T) -> None: 
        if len(self) ==len(self.array): 
            new_array = ArrayR(self.__newsize())
            for i in range(len(self)): 
                new_array[i] = self.array[i]
            self.array = new_array

        for i in range(self.length, index, -1): 
            self.array[i] = self.array[i-1]

        self.array[index] = item 
        self.length += 1


    def delete_at_index(self, index: int) -> T:
        item = self[index]
        self.length -= 1
        for i in range(index, self.length): 
            self.array[i] = self.array[i+1]
        return item


    def index(self, item: T) -> int: 
        for i in range(len(self)): 
            if item == self.array[i]: 
                return i 
        raise ValueError("item not in lsit")

