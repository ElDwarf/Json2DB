# -*- coding: utf-8 -*-


class models():
    table = []

    def __init__(self, table_date):
        self.table = table_date

    def __unicode__(self):
        return self.table

    def filter(self, col, text):
        result = []
        for x in self.table:
            if x[col] == text:
                result.append(x)
        return result

    def get(self, col, text):
        for x in self.table:
            if x[col] == text:
                return x
        return None

    def count(self):
        return len(self.table)
