class DataCompany:
    """

    type of datas :

    0 : Ticker   1 : Date   2 : First   3 : High   4 : Low   5 : Close   6 : value   7 :
     Volume   8 : OpenInt   9 : Per   10
     : Open   11 : Last   12 : ID   13 : Name   14 : BigName
    10 : Open === price stop first     5 : Close === price stop the end

    """

    def __init__(self):
        self.row = None

    @staticmethod
    def get_first(row):
        return float(row[2])

    @staticmethod
    def get_last(row):
        return float(row[11])

    @staticmethod
    def get_low(row):
        return float(row[4])

    @staticmethod
    def get_high(row):
        return float(row[3])

    @staticmethod
    def get_open(row):
        return float(row[10])

    @staticmethod
    def get_close(row):
        return float(row[5])

    @staticmethod
    def get_volume(row):
        return int(row[7])

    @staticmethod
    def get_date(row):
        return int(row[1])

    def get_down_shadow(self, row):
        return min(self.get_first(row), self.get_last(row)) - self.get_low(row)

    def get_up_shadow(self, row):
        return self.get_high(row) - max(self.get_first(row), self.get_last(row))

    def get_body(self, row):
        return abs(self.get_last(row) - self.get_first(row))
