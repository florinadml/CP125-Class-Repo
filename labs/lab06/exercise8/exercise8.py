def analyze_scores(score_records):
    all_scores = []
    
    for student_id, score in score_records:
        all_scores.append(score)
    
    highest = max(all_scores)
    
    average = sum(all_scores) / len(score_records)
    
    above_average_count = 0
    for score in all_scores:
        if score > average:
            above_average_count += 1
    
    return (highest, average, above_average_count)
