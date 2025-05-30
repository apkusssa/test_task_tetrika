def merge_intervals(intervals):
    """Объединяет пересекающиеся интервалы."""
    intervals = sorted(zip(intervals[::2], intervals[1::2]))
    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

def get_intersection(a, b):
    """Возвращает общее время пересечения двух списков интервалов."""
    i = j = total = 0
    while i < len(a) and j < len(b):
        start = max(a[i][0], b[j][0])
        end = min(a[i][1], b[j][1])
        if start < end:
            total += end - start
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return total

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    # Ограничим интервалы учеников и учителей временем урока
    lesson_interval = [[lesson[0], lesson[1]]]

    pupil_merged = merge_intervals(pupil)
    tutor_merged = merge_intervals(tutor)

    # Пересекаем интервалы с временем урока
    pupil_limited = [
        [max(p[0], lesson[0]), min(p[1], lesson[1])]
        for p in pupil_merged if p[1] > lesson[0] and p[0] < lesson[1]
    ]
    tutor_limited = [
        [max(t[0], lesson[0]), min(t[1], lesson[1])]
        for t in tutor_merged if t[1] > lesson[0] and t[0] < lesson[1]
    ]

    return get_intersection(pupil_limited, tutor_limited)
