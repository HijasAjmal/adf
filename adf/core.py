from collections import OrderedDict
from adf.pprint import pprint

class Adf:
    """
    The core class holding all operations related to transforming the dataframe
    """
    def __init__(self, yielder):
        """
        The constructor only needs a filename for now
        """
        self.yielder = yielder
        
        # Someday, somewhere, someone will try to use self.data as a dict without populating it
        # This will save them an exception
        self.data = {}
        self.pp = pprint(self.data)
        
    def read_file(self, filename):
        """
        The idea is that the read operation within the core dataframe library knows how to transform a dict style record to the
        desired data structure.
        
        Where the yielded records come from is not of any concern to the core
        """
        
        # Multiple reads should not append to self.data (or should it?)
        
        # As long as it can yield a dict, we can process it
        for record in self.yielder(filename):
            for column, value in record.items():
                # If the column already exists in self.data, it means this is not the first record
                if column in self.data.keys():
                    self.data[column].append(value)
                else:   # Initialize the data values as a list with only a single value from the first record
                    self.data[column] = [value]
        
        print(self.data)    # TODO Remove this once our testing is done

    def read(self, data):
        """
        Base read to read directly from a data
        :return:
        """
        length = len(data[list(data.keys())[0]])
        keys = list(data.keys())
        data_rows = (OrderedDict([(k, data[k][i]) for k in keys]) for i in range(length))
        for record in self.yielder(data_rows):
            for column, value in record.items():
                # If the column already exists in self.data, it means this is not the first record
                if column in self.data.keys():
                    self.data[column].append(value)
                else:   # Initialize the data values as a list with only a single value from the first record
                    self.data[column] = [value]




    def dim(self):
        """

        :return:
        """
        cols = len(self.data)
        rows = len(self.data[list(self.data.keys())[0]])
        return(cols, rows)

    def show(self):
        """
        """
        self.pp.show(self.data)

    def head(self, n=5):
        """

        :param n:
        :return:
        """
        self.pp.head(n)

    def tail(self, n=5):
        """

        :param n:
        :return:
        """
        self.pp.tail(n)
