import numpy as np

def make_hours():
    hours = np.arange(0, 22, 3, dtype=np.int64)
    return hours.tolist()

def vector_report(values):
    dict_report = {
        "third": values[2],
        "last": values[-1],
        "middle": values[2:6],
        "every_second": values[::2],
        "reversed": values[::-1],
    }
    return dict_report

def change_vector(values):
    changed_values = np.array(values, copy=True)
    changed_values[2:5] = 99
    changed_values[::2] = -1
    return changed_values.tolist()

def cap_above(values, limit):
    capped_values = np.array(values, copy=True)
    capped_values[capped_values > limit] = limit
    return capped_values.tolist()

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit.tolist()
