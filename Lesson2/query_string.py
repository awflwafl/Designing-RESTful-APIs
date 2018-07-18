def sanitize(value):
    return str(value).replace(' ', '+')

def build_query_string(parameters):
    if len(parameters) == 0: return ''

    query = []
    for key, value in parameters.items():
        query.append('{}={}'.format(key, sanitize(value)))
    query_string = '&'.join(query)

    return query_string
