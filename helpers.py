from decimal import Decimal


def to_lists(pasted, categorical=False):
    """Takes output pasted from Sheets and spits out a list of lists(one per column)"""
    lists = []
    lines = pasted.split('\n')
    for line in lines:
        pigs = line.split('\t')
        for i, value in enumerate(pigs):
            if len(lists) == len(pigs):
                try:
                    if categorical[i]:
                        pass
                    else:
                        value = value.replace('$', '').replace(',', '')
                        value = Decimal(value)
                except TypeError:
                    value = value.replace('$', '').replace(',', '')
                    value = Decimal(value)
                except IndexError:
                    print(
                        'categorical must be a subscriptable object with length equals number of columns.'
                    )
                lists[i].append(value)
            else:
                lists.append([value])
    return lists


def to_dicts(pasted, categorical=False):
    """Takes output pasted from Sheets and spits out a list of dicts(one per column)
    with the first row as the key of each dict.

    """
    lists = to_lists(pasted, categorical=categorical)
    d = {ls[0]: ls[1:] for ls in lists}
    return d
