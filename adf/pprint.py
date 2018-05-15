"""
Simply pretty print the adf
"""

class pprint:
    """
    class to pretty print the data structure behind adf
    """
    def __init__(self):
        """

        """
        self.data = {"c1": [1,2,3,4,5,6,7,8,9],
         "c2": [11,"dsfa",33,44,5,6,7,8,9],
         "c3": [11, 22, "afsd", "sadgsaafgfdhhfdshfdhkdghjlkdfjhdkl", 5, 6, 7, 8, "sdfa"]}
        self.n = len(self.data.keys())

    def show(self, d):
        """

        :param d:
        :return:
        """
        for row in zip(*([key] + value for key, value in sorted(d.items()))):
            print('+'+('-'*18+'+')*self.n)
            print("|", *[str(i).strip() + " "*(18-len(str(i))-1) + "|" if len(str(i)) < 18 else str(i)[0:14] + "...|" for i in row])

        print('+' + ('-' * 18 + '+')*self.n)

    def head(self, n=5):
        """

        :param n:
        :return:
        """
        print("Showing first " + str(n) + " rows - ")
        self.show({k: self.data[k][0:5] for k in self.data})

    def tail(self, n=5):
        """

        :param n:
        :return:
        """
        print("Showing last "+str(n)+" rows - ")
        self.show({k: self.data[k][len(self.data[k])-n+1:] for k in self.data})
