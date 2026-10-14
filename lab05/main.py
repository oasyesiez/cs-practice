import logstats

def main():
    filename = input().strip()
    
    
    with open(filename, "r", encoding="utf-8") as f:
        counts = logstats.count_levels(f)
        

    total_parsed = sum(counts.values())
    error_count = counts.get('ERROR', 0)
    broken_count = counts.get('BROKEN', 0)
    
    
    print(total_parsed)
    print(error_count)
    print(broken_count)
    
    with open(filename, "r", encoding="utf-8") as f:
        errors = logstats.top_errors(f, 3)
        
    report_text = logstats.format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)

if __name__ == "__main__":
    main()
