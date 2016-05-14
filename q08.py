def solve(problem):
    switches = (solve_one_case(search_engines, queries)
                for search_engines, queries in gather_cases(problem))
    return ['Case #{}: {}\n'.format(index, switch) 
            for index, switch in enumerate(switches, start=1)]

def gather_cases(problem):
    number_of_cases = int(next(problem))
    for i in range(number_of_cases):
        number_of_search_engines = int(next(problem))
        search_engines = [next(problem) for j in range(number_of_search_engines)]
        number_of_queries = int(next(problem))
        queries = [next(problem) for j in range(number_of_queries)]
        yield (search_engines, queries)

def solve_one_case(search_engines, queries):
    import pdb; pdb.set_trace()    
    switches = 0
    allowed_engines = search_engines.copy()
    for query in reversed(queries):
        if query in allowed_engines:
            allowed_engines.remove(query)
        if len(allowed_engines) == 0:
            switches += 1
            allowed_engines = search_engines.copy()
    return switches