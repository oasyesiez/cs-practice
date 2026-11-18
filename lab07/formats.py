import json


def csv_to_records(text: str) -> list[dict]:
    lines = [line for line in text.strip().splitlines() if line.strip()]
    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        records.append(dict(zip(headers, values)))

    return records


def parse_settings(lines: list[str]) -> dict:

    def cast_value(raw: str):
        val = raw.strip()
        lower = val.lower()

        if lower in ("true", "yes"):
            return True
        if lower in ("false", "no"):
            return False

        try:
            return int(val)
        except ValueError:
            pass

        try:
            return float(val)
        except ValueError:
            pass

        return val

    result = {}
    current_list_key = None

    for raw_line in lines:
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        stripped = line.lstrip()

        if stripped.startswith("- ") and current_list_key is not None:
            result[current_list_key].append(cast_value(stripped[2:]))
            continue

        if ":" in stripped:
            key, val = stripped.split(":", 1)
            key = key.strip()
            val = val.strip()

            if val == "":
                result[key] = []
                current_list_key = key
            else:
                result[key] = cast_value(val)
                current_list_key = None

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    merged_rows = []

    for row in rows:
        new_row = row.copy()
        lookup_val = row.get(key)

        if lookup_val is not None and lookup_val in extra:
            combined = {**extra[lookup_val], **new_row}
            merged_rows.append(combined)
        else:
            merged_rows.append(new_row)

    return merged_rows


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
