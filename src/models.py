# -*- coding: utf-8 -*-


class models():
    table = []

    def __init__(self, table_date):
        self.table = table_date

    def __unicode__(self):
        return self.table

    def __str__(self):
        return self.table

    def __repr__(self):
        return str(self.table)

    def filter(self, *args, **kwargs):
        result = []
        for query in kwargs:
            if '__icontains' in query:
                col = query.replace('__icontains', '')
                for x in self.table:
                    if kwargs[query] in x[col]:
                        result.append(x)
            else:
                col = query
                for x in self.table:
                    if kwargs[query] == x[col]:
                        result.append(x)
        result1 = models(result)
        return result1

    def get(self, col, text):
        for x in self.table:
            if x[col] == text:
                return x
        return None

    def count(self):
        return len(self.table)
