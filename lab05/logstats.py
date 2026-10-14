def parse_event(line: str) -> dict:
    cleaned = line.rstrip('\r\n')
    
    parts = cleaned.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Некорректный формат строки")
        
    time, level, message = parts
    if level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:
        raise ValueError("Неизвестный уровень логирования")
        
    return {"time": time, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {'BROKEN': 0, 'DEBUG': 0, 'ERROR': 0, 'INFO': 0, 'WARNING': 0}
    
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            counts[event['level']] += 1
        except ValueError:
            counts['BROKEN'] += 1
            
    return counts

