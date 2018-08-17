"""
Simply pretty print the adf
"""

class pprint:
    """
    class to pretty print the data structure behind adf
    >>> pp = pprint()
    >>> pp.head()
    +------------------+------------------+------------------+
    | c1               | c2               | c3               |
    +------------------+------------------+------------------+
    | 1                | 11               | 11               |
    +------------------+------------------+------------------+
    | 2                | dsfa             | 22               |
    +------------------+------------------+------------------+
    | 3                | 33               | afsd             |
    +------------------+------------------+------------------+
    | 4                | 44               | sadgsaafgfdhhf...|
    +------------------+------------------+------------------+
    | 5                | 5                | 5                |
    +------------------+------------------+------------------+
    >>> pp.tail()
    Showing last 5 rows -
    +------------------+------------------+------------------+
    | c1               | c2               | c3               |
    +------------------+------------------+------------------+
    | 6                | 6                | 6                |
    +------------------+------------------+------------------+
    | 7                | 7                | 7                |
    | 9                | 9                | sdfa             |
    +------------------+------------------+------------------+
    | 8                | 8                | 8                |
    +------------------+------------------+------------------+
    +------------------+------------------+------------------+
    >>>
    """
    def __init__(self, data):
        """

        """
        # self.data = {"c1": [1,2,3,4,5,6,7,8,9],
        #  "c2": [11,"dsfa",33,44,5,6,7,8,9],
        #  "c3": [11, 22, "afsd", "sadgsaafgfdhhfdshfdhkdghjlkdfjhdkl", 5, 6, 7, 8, "sdfa"]}
        self.data = data
        self.n = len(self.data.keys())

    def show(self, d):
        """

        :param d:
        :return:
        """
        for row in zip(*([key] + value for key, value in sorted(d.items()))):
            print('+'+('-'*18+'+')*self.n)
            print("|", *[str(i).strip() + " "*(18-len(str(i))) + "|" if len(str(i)) < 18 else str(i)[0:14] + "...|" for i in row])

        print('+' + ('-' * 18 + '+')*self.n)

    def head(self, n=5):
        """

        :param n:
        :return:
        """
        print("Showing first " + str(n) + " rows - ")
        self.show({k: self.data[k][0:n] for k in self.data})

    def tail(self, n=5):
        """

        :param n:
        :return:
        """
        print("Showing last "+str(n)+" rows - ")
        self.show({k: self.data[k][len(self.data[k])-n+1:] for k in self.data})
