"""Functions for organizing and calculating student exam scores."""
PASS_THRESHOLD = 40

def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    rounded = []
    for score in student_scores:
        rounded.append(round(score))

    return rounded

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    number_of_failures = 0
    for score in student_scores:
        if score <= PASS_THRESHOLD:
            number_of_failures += 1
    return number_of_failures

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """
    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    return best_scores

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    list_of_lower_thresholds = []
    interval_range = (highest - PASS_THRESHOLD) // 4
    for k in range(0, 4):
        list_of_lower_thresholds.append(PASS_THRESHOLD + 1 + interval_range * k)

    return list_of_lower_thresholds

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    student_ranks = []
    for index, name in enumerate(student_names, start = 1):
        student_ranks.append(f'{index}. {name}: {student_scores[index - 1]}')

    return student_ranks

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if student[-1] == 100:
            return student

    return []