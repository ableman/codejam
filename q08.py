def solve(problem):
    return_lines = []
    number_of_test_cases = int(next(problem))
    for i in range(number_of_test_cases):
        switches = 0
        number_of_search_engines = int(next(problem))
        search_engines = []
        for j in range(number_of_search_engines):
            search_engines.append(next(problem))
        number_of_queries = int(next(problem))
        queries = []
        for j in range(number_of_queries):
            queries.append(next(problem))
        allowed_engines = search_engines[:]
        for query in queries[::-1]:
            if query in allowed_engines:
                allowed_engines.remove(query)
            if len(allowed_engines) == 0:
                switches += 1
                allowed_engines = search_engines[:]
        return_lines.append('Case #{}: {}\n'.format(i+1, switches))
    return return_lines