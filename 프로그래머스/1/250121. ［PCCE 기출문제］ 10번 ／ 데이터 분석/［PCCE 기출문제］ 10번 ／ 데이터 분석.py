def solution(data, ext, val_ext, sort_by):
    answer = []
    columns = ["code", "date", "maximum", "remain"]

    ext_index = columns.index(ext)
    sort_index = columns.index(sort_by)

    for row in data:
        if row[ext_index] < val_ext:
            answer.append(row)

    answer.sort(key=lambda row: row[sort_index])

    return answer