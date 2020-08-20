import threading


def threaded_list(_list):
    # at max 4 chunks
    chunked = [_list[i:i + ceil(len(_list)/4)] for i in range(0, len(_list), ceil(len(_list)/4))]
    final = []

    def worker(l):
        for i, val in enumerate(l):
            if isinstance(val, list):
                l[i] = CustomList(val, True)
            elif isinstance(val, dict):
                l[i] = CustomDict(val, True)

        final.extend(l)

    threads = []
    for i, chunk in enumerate(chunked):
        threads.append(threading.Thread(target=worker, args=(chunk,)))
        threads[i].start()

    for thread in threads:
        thread.join()

    return final


class CustomList(list):
    def __init__(self, _list, threaded):
        if threaded:
            list.__init__(self, threaded_list(_list))
        else:
            for i, val in enumerate(_list):
                if isinstance(val, list):
                    _list[i] = CustomList(val, threaded)
                elif isinstance(val, dict):
                    _list[i] = CustomDict(val, threaded)

            list.__init__(self, _list)


class CustomDict(dict):
    def __init__(self, _dict, threaded):
        dict.__init__(self, _dict)

        for key in list(_dict):
            if isinstance(_dict[key], list):
                dict.__setitem__(self, key, CustomList(_dict[key], threaded))
            elif isinstance(_dict[key], dict):
                dict.__setitem__(self, key, CustomDict(_dict[key], threaded))
            else:
                dict.__setitem__(self, key, _dict[key])

    def __getattr__(self, name):  # CustomDict.a
        return dict.__getitem__(self, name)

    def __setattr__(self, name, value):  # CustomDict.a = 'something'
        return dict.__setitem__(self, name, value)

    def __delattr__(self, name):  # del CustomDict.a
        popped = dict.__getitem__(key)
        dict.__delitem__(self, key)
        return popped
