class DataCompany:
    """
    type of datas :

    0 : Ticker   1 : Date   2 : First   3 : High   4 : Low   5 : Close   6 : value   7 :
     Volume   8 : OpenInt   9 : Per   10
     : Open   11 : Last   12 : ID   13 : Name   14 : BigName
    10 : Open === price stop first     5 : Close === price stop the end
    """

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

    @staticmethod
    def get_down_shadow(row):
        return min(DataCompany.get_first(row), DataCompany.get_last(row)) - DataCompany.get_low(row)

    @staticmethod
    def get_up_shadow(row):
        return DataCompany.get_high(row) - max(DataCompany.get_first(row), DataCompany.get_last(row))

    @staticmethod
    def get_body(row):
        return abs(DataCompany.get_last(row) - DataCompany.get_first(row))
