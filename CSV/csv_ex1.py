# From csv.py

def next(self):
    if self.line_num == 0:
        # Used only for its side effect.
        self.fieldnames
        row = self.reader.next()
        self.line_num = self.reader.line_num

        # unlike the basic reader, we prefer not to return blanks,
        # because we will typically wind up with a dict full of None
        # values
    while row == []:
        row = self.reader.next()
    d = dict(zip(self.fieldnames, row))
    lf = len(self.fieldnames)
    lr = len(row)
    if lf < lr:
        d[self.restkey] = row[lf:]
    elif lf > lr:
        for key in self.fieldnames[lr:]:
            d[key] = self.restval
    return d
