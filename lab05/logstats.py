def parse_event(line: str) -> dict:
    
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("Пустая строка")
        
    
    parts = cleaned.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Некорректный формат строки")
        
    time, level, message = parts
    
    if level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:
        raise ValueError("Неизвестный уровень логирования")
        
    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    
    
    counts = {
        'BROKEN': 0,
        'DEBUG': 0,
        'ERROR': 0,
        'INFO': 0,
        'WARNING': 0
    }
    
    for line in lines:
        
        if not line or not line.strip():
            continue
            
        try:
            event = parse_event(line)
            counts[event['level']] += 1
        except ValueError:
            counts['BROKEN'] += 1
            
    return counts


def top_errors(lines, n: int) -> list[list]:
    
    error_counts = {}
    
    for line in lines:
        if not line or not line.strip():
            continue
            
        try:
            event = parse_event(line)
            if event['level'] == 'ERROR':
                msg = event['message']
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue
            
    
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    
    return [list(item) for item in sorted_errors[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
   
    report_lines = ["Отчёт по журналу", ""]
    
    for level in sorted(counts.keys()):
        report_lines.append(f"{level}: {counts[level]}")
        
    report_lines.append("")
    report_lines.append("Частые ошибки:")
    
    for msg, count in errors:
        report_lines.append(f"- {msg} - {count}")
        
    return "\n".join(report_lines) + "\n"
