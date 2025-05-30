def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start_point, lesson_end_point = intervals["lesson"]
    pupil = intervals["pupil"]
    tutor = intervals["tutor"]
    pupil_interval = []
    tutor_interval = []

    for i in range(0, len(pupil), 2):
        start_point = max(pupil[i], lesson_start_point)
        end_point = min(pupil[i + 1], lesson_end_point)
        if start_point < end_point:
            pupil_interval.append((start_point, end_point))

    for i in range(0, len(tutor), 2):
        start_point = max(tutor[i], lesson_start_point)
        end_point = min(tutor[i + 1], lesson_end_point)
        if start_point < end_point:
            tutor_interval.append((start_point, end_point))

    crossed_intervals = []
    i = j = 0
    while i < len(pupil_interval) and j < len(tutor_interval):
        start_point_pupil, end_point_pupil = pupil_interval[i]
        start_point_tutor, end_point_tutor = tutor_interval[j]
        cross_start = max(start_point_tutor, start_point_pupil)
        cross_end = min(end_point_tutor, end_point_pupil)
        if cross_start < cross_end:
            crossed_intervals.append((cross_start, cross_end))
        if end_point_pupil < end_point_tutor:
            i += 1
        else:
            j += 1
    crossed_intervals = [list(i) for i in crossed_intervals]
    summ = 0
    for v in crossed_intervals:
        summ += v[1] - v[0]
    return summ


tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]

if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
