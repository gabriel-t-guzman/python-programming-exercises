
def parseMDY(date):
    data = date.split("/")
    if len(data) < 3 : return (int(data[0]),0,0)
    return int(data[2]),int(data[0]),int(data[1])
    """Return (year, month, day) from date in MM/DD/YYYY format."""
    ...
def yearsBetween(date1, date2):
    """Return integer number of years between two (y, m, d) dates."""
    if date2[0] < date1[0] : 
        date3 = date1
        date1 = date2
        date2 = date3 
    d_y = abs(date2[0]-date1[0])
    if date2[1] > date1[1] : return d_y
    elif date2[1] == date1[1] : 
        if date2[2] >= date1[2] : return d_y
        else: return d_y-1
    else : return d_y-1

def main():
    # Test parseMDY
    print(f"{parseMDY('12/25/2024') = }")  # (2024, 12, 25)
    print(f"{parseMDY('4/25/1974') = }")   # (1974, 4, 25)
    print(f"{parseMDY('1755') = }")        # (1755, 0, 0)

    # Test yearsBetween
    print(f"{yearsBetween((1900, 6, 1), (1935, 5, 31)) = }")  # 34
    print(f"{yearsBetween((1900, 6, 1), (1935, 6, 1)) = }")   # 35
    print(f"{yearsBetween((1900, 6, 1), (1936, 5, 31)) = }")  # 35
    print(f"{yearsBetween((1900, 3, 7), (1971, 4, 9)) = }")
    print(f"{yearsBetween((1971, 4, 9), (1900, 3, 7)) = }")


# This program may be used as a module too
if __name__ == "__main__":
    main()

