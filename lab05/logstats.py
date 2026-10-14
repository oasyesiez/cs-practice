def parse_event(line: str) -> dict:
    cleaned = line.rstrip('\r\n')
    
    parts = cleaned.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Некорректный формат строки")
        
    time, level, message = parts
    if level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:
        raise ValueError("Неизвестный уровень логирования")
        
    return {"time": time, "level": level, "message": message}