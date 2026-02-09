def match_filters(resume, job):
    if resume["location"] != job["location"]:
        return False
    if not (job["min_exp"] <= resume["experience"] <= job["max_exp"]):
        return False
    if resume["role"] != job["role"]:
        return False
    return True
