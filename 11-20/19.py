weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct",
            "nov", "dec"]

monthsdict = {"jan":31, "feb":28, "mar":31, "apr":30, "may":31, "jun":30, "jul":31,
            "aug":31, "sep":30, "oct":31, "nov":30, "dec":31}


years = range(1900, 2001)

sundaycount = 0

currentday = weekdays[0]

dayspast = 0

for currentyear in years:

    for currentmonth in months:

        if currentmonth == "feb" and currentyear % 4 == 0\
        and currentyear % 100 != 0:

            monthsdict["feb"] = 29
        elif currentyear == 2000:

            monthsdict["feb"] = 29

        else:

            monthsdict["feb"] = 28

        for currentdate in range(1, monthsdict[currentmonth]+1):

            dayspast += 1

            currentday = weekdays[dayspast % 7 - 1]

            if currentday == "sun" and currentyear > 1900 and currentdate == 1:

                sundaycount += 1

print(sundaycount)
