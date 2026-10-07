def parse_record(line: str) -> dict:
    
    fields = line.split(";")
    if len(fields) != 3:
        raise ValueError("Строка должна содержать ровно три поля, разделенных ';'")
    
    city, temperature_str, date = [f.strip() for f in fields]
    
    if not city or not date:
        raise ValueError("Название города и дата не могут быть пустыми")
        
    temperature_str = temperature_str.replace(",", ".")
    
    try:
        temperature = float(temperature_str)
    except ValueError:
        raise ValueError(f"Некорректный формат температуры: '{temperature_str}'")
        
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:

    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for r in records:
        city = r["city"]
        totals[city] = totals.get(city, 0.0) + r["temperatureerature"]
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)
    return averages

def warmest_city(records: list[dict]) -> str:

    if not records:
        return ""
        
    averages = average_by_city(records)
    
    best_city = None
    max_temperatureerature = float('-inf')
    
    for city, avg_temperatureerature in averages.items():
        if avg_temperatureerature > max_temperatureerature:
            max_temperatureerature = avg_temperatureerature
            best_city = city
        elif avg_temperatureerature == max_temperatureerature:
            
            if best_city is None or city < best_city:
                best_city = city
                
    return best_city

