def count_by_extension(paths):
    totals = {}
    for line in paths:
        if line.startswith('.') and line.count('.') == 1:
            key = ''
        else:
            parts = line.split('.')
            if len(parts) < 2:
                key = ''
            else:
                key = parts[-1].lower()
                
        totals[key] = totals.get(key, 0) + 1
    return totals

def deepest_path(paths):
    deepest_path = ''
    c = 0
    for line in paths:
        if line.count('/') > c:
            c = line.count('/')
            deepest_path = line
    return deepest_path

def human_size(n_bytes: int):
    for unit in ['Б', 'КБ', 'МБ', 'ГБ']:
        if n_bytes < 1024:
            return f"{n_bytes:.1f} {unit}"
        n_bytes /= 1024
    return f"{n_bytes:.1f} ТБ"
