
def next_birthday(date, birthdays):
    '''
    Find the next birthday after the given date.

    @param:
    date - a tuple of two integers specifying (month, day)
    birthdays - a dict mapping from date tuples to lists of names, for example,
      birthdays[(1,10)] = list of all people with birthdays on January 10.

    @return:
    birthday - the next day, after given date, on which somebody has a birthday
    list_of_names - list of all people with birthdays on that date
    '''
    '''
    birthday = (1,1)
    list_of_names = []
    return birthday, list_of_names
    '''
    month, day = date
    while (month, day) not in birthdays:   # Counting month and day until we find it in birthdays
        day = day + 1
        if day > 31:                       # Easily 31 days month count
            day = 1
            month = month + 1
            if month > 12:                 # Easily 12 months next year count
                month = 1

    birthday = (month, day)                # Here (month, day) confirms birthday
    list_of_names = birthdays[birthday]
    return birthday, list_of_names
            