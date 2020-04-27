def deep_find_dfs(data, key):
    searching_in = data
    searched_in = []

    def dfs(data):
        print('searching in: ', searching_in)
        print('data: ', data)
        print('key: ', key)
        try:
            return data[key]
        except Exception:
            current = searching_in.pop(0)
            searched_in.append(current)
            if type(current) is dict and current not in searched_in:
                searching_in.extend(current)
            return dfs(current)

    return dfs(data)
