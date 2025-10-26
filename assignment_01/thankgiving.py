import calendar as cal

def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)

    # jika minggu pertama ada hari Kamis
    if month[0][cal.THURSDAY] != 0:
        # minggu ke 4
        thankgiving = month[3][cal.THURSDAY]
    else:
        # minggu ke 5
        thankgiving = month[4][cal.THURSDAY]

    return thankgiving

def shopping_days(year):
    """
    year: a number <=1941
    returns the number of days between US Thankgiving and Christmas
    of the year
    """

    if year > 1941:
        return "ERROR! Input tahun sebelum 1941!"

    # get date thanksgiving
    date = find_thanksgiving(year)

    # get number date from thankgiving to 30 November and add 24 day before Christmast
    number_of_day = 30 - int(date) + 24

    return number_of_day

inputan = input("Masukkan tahun sebelum 1941 : ")
tahun = int(inputan)

print("In", tahun, "U.S. Thankgiving was on November", find_thanksgiving(tahun))
print("Shopping Day before Christmast: ", shopping_days(tahun))