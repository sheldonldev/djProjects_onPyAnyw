# Really simple naturalsize that is missing from django humanize :(


def naturalsize(count):
    float_count = float(count)
    k = 1024
    m = k * k
    g = m * k

    if float_count < k:
        return str(count) + 'B'

    elif k <= float_count < m:
        return str(int(float_count / (k/10.0)) / 10.0) + 'KB'

    elif m <= float_count < g:
        return str(int(float_count / (m/10.0)) / 10.0) + 'MB'

    elif g <= float_count:
        return str(int(float_count / (m/10.0)) / 10.0) + 'GB'
