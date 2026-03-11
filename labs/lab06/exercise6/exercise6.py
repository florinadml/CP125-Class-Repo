def manage_roster(enrolled, drop_requests, waitlist):
    for student in drop_requests :
        if student in enrolled :
            enrolled.remove(student)

    if len(enrolled) < 5 :
        while len(enrolled) < 7 and waitlist:
            enrolled.add(waitlist.pop())

    return len(enrolled)