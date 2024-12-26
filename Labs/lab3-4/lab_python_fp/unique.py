class Unique(object):
    def __init__(self, items, **kwargs):
        ignore_case = kwargs["ignore_case"] if "ignore_case" in kwargs.keys() else False
        itm = {}
        if ignore_case:
            for el in items:
                if str(el).lower() not in itm.keys(): itm[str(el).lower()] = el
        else:
            for el in items:
                if str(el) not in itm.keys():itm[str(el)] = el
        self.data = [itm[a] for a in itm]
        self.val = 0
        self.size = len(self.data)

    def __next__(self):
        if self.val + 1 < self.size:
            self.val += 1
            return self.data[self.val]
        else:
            raise StopIteration

    def __iter__(self):
        self.val = 0
        return self