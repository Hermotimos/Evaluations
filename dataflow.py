import os.path
from collections import Counter


class Title:
    """Class providing unique instances as dict keys in Database.__str__"""
    def __init__(self, name):
        self.name = name


class Database:
    def __init__(self, sourcefile):
        self.sourcefile = sourcefile
        assert os.path.isfile(sourcefile), "No source file or invalid sourcefile for database provided!"
        self.openedfile = open(file=sourcefile, mode='r')
        self.db_dict = {}

    def __str__(self):
        """
        Class instances as dict keys allow storage of multiple evaluations (values) for seemingly identical keys
        (Title instances). Class instances are unique even if self.name attribute is identical across many instances.
        """
        return '\n'.join("{}: {}".format(k.name, v) for (k, v) in self.into_dict().items())

    def into_dict(self):
        """ Transform file into dict with possibly uniform titles within unique instances of 'Title' class"""
        for line in self.openedfile:
            k, v = line.strip().split(': ')
            self.db_dict[Title(k.strip('""'))] = int(v.strip())
        return self.db_dict

    def insert_eval(self, title, evaluation):
        """
        Reopen file in append mode to move cursor to end of file, write, reopen in read mode to move cursor to beginning
        """
        self.openedfile = open(file=self.sourcefile, mode='a')
        self.openedfile.write("\n\"{}\": {}".format(title, evaluation))
        self.openedfile = open(file=self.sourcefile, mode='r')

    def get_evals(self, title):
        evals = ''
        for k, v in self.into_dict().items():
            if k.name == title:
                evals += "{}: {}{}".format(k.name, v, '\n')
        return evals if evals else 'No evaluations found for given title.'

    def avg_evals(self, title):
        cnt = self.cnt_evals(title)
        s = sum(v for k, v in self.into_dict().items() if k.name == title)
        try:
            return round(s/cnt, 2)
        except ZeroDivisionError:
            return 'No evaluations found for given title.'

    def cnt_evals(self, title):
        n = (k.name for k in self.into_dict().keys() if k.name == title)
        return Counter(n)[title]


# c = Database()
# # c.insert_eval("The sth", 5)
# print(c)
# print()
# print(c.get_evals('The sth'))
# print(c.cnt_evals("The sth"))
# print(c.avg_evals('The Wire'))
