class Adf:
    """
    The core class holding all operations related to transforming the dataframe
    """
    def __init__(self, filename):
        """
        The constructor only needs a filename for now
        """
        self.filename = filename
        
        # Someday, somewhere, someone will try to use self.data as a dict without populating it
        # This will save them an exception
        self.data = {}
        
    def read(self, yielder):
        """
        The idea is that the read operation within the core dataframe library knows how to transform a dict style record to the
        desired data structure.
        
        Where the yielded records come from is not of any concern to the core
        """
        
        # Multiple reads should not append to self.data (or should it?)
        self.data = {}
        
        # As long as it can yield a dict, we can process it
        for record in yielder(self.filename):
            for column, value in record.items():
                # If the column already exists in self.data, it means this is not the first record
                if column in self.data.keys():
                    self.data[column].append(value)
                else:   # Initialize the data values as a list with only a single value from the first record
                    self.data[column] = [value]
        
        print(self.data)    # TODO Remove this once our testing is done
