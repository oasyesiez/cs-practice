def parse_record(line: str) -> dict:
    
    fields = line.split(";")
    if len(fields) != 3:
        raise ValueError("Строка должна содержать ровно три поля, разделенных ';'")
    
    city, temp_str, date = fields
    
    if not city.strip() or not date.strip():
        raise ValueError("Название города и дата не могут быть пустыми")
        
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректный формат температуры: '{temp_str}'")
        
    return {"city": city, "temp": temp, "date": date}

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
