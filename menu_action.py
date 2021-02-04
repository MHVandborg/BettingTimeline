import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt


def plot_betting_timeline():
    # Read data and processes it to earnings vs time
    data = read_data()
    data = process_data(data)

    # Plot betting history
    fig1 = plt.figure(1)
    x = [data.Date[i][0:5] for i in range(len(data))]
    y = [data.Total[i] for i in range(len(data))]
    plt.plot(x, y)
    plt.ylabel('Earnings (DKK)')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.title("Current total: %0.1f (DKK)" % data.Total[len(data)-1])
    plt.show()
    plt.draw()
    fig1.savefig("Betting_timeline.png")


def process_data(data):

    # Bet total is 100 (DKK) on the first day (day before first bet)
    total = 100
    first_date = data.iloc[0].Date.split('/')
    first_date = str(int(first_date[0])-1)+"/"+first_date[1]+"/"+first_date[2]

    # New dateframe for plots
    plot_data = pd.DataFrame({"Total": total, "Date": first_date},
                        columns=['Total', 'Date'], index=[0])

    old_date = data.iloc[0].Date

    for x in range(len(data)):
        # If new day, then store new total for day in between
        if data.iloc[x].Date != old_date:
            old_day = old_date.split('/')
            new_day = data.iloc[x].Date.split('/')
            d0 = dt.date(2000+int(old_day[2]), int(old_day[1]), int(old_day[0]))
            d1 = dt.date(2000+int(new_day[2]), int(new_day[1]), int(new_day[0]))
            delta = d1 - d0
            for y in range(delta.days):
                date_data = pd.DataFrame({"Total": total, "Date": d0.strftime("%d/%m/%y")},
                                         columns=['Total', 'Date'], index=[0])
                plot_data = plot_data.append(date_data, ignore_index=True)
                d0 += dt.timedelta(days=1)

        # Update total depending on win or loss
        if data.iloc[x].WL != "-":
            if data.iloc[x].WL == "L":
                total = total - data.iloc[x].Amount
            elif data.iloc[x].WL == "W":
                total = total + data.iloc[x].Amount * (data.iloc[x]["Odds win"] - 1)

        if x == len(data)-1:
            date_data = pd.DataFrame({"Total": total, "Date": data.iloc[x].Date},
                                     columns=['Total', 'Date'], index=[0])
            plot_data = plot_data.append(date_data, ignore_index=True)

        old_date = data.iloc[x].Date

    return plot_data


def add_bet():
    # Read database
    database = pd.read_csv('BetData.csv', delimiter=',')

    # Get user inputs
    match = input("Match: ")
    odds_win = input("Odds win: ")
    amount = input("Amount: ")
    WL = input("Win/Loss (blank = TBD): ")
    date = input("Date (dd/mm/yy) (blank = today): ")

    # If blank user inputs
    if not WL:
        WL = "-"
    if not date:
        today = dt.date.today()
        date = today.strftime("%d/%m/%y")

    # Formatting new data
    data = pd.DataFrame({"Match": match, "Odds win": odds_win,
                         "Amount": amount, "WL": WL, "Date": date},
                        columns=['Match', 'Odds win', 'Amount', 'WL', 'Date'], index=[0])

    # Combine new data to database with sort by date
    database = database.append(data, ignore_index=True)
    database = database.sort_values(by=['Date'])

    # Save csv file with combined data
    database.to_csv(r'BetData.csv', index=False, header=True)


def read_data():
    database = pd.read_csv(r'BetData.csv')
    return database


def confirm_WL():
    data = read_data()
    rem_input = []

    for x in range(len(data)):
        if data.iloc[x].WL == "-":
            print(data[x:x+1])
            rem_input.append(x)

    temp = -1
    while temp == -1:
        user = int(input("Press game number to edit W/L.\nPress 0 to exit (has to be an int):"))
        WorL = int(input("1: Win.\n2: Loss.\n3: To Be Decided.\nPress 0 to cancel (has to be an int):"))
        if WorL == 0:
            break
        for x in rem_input:
            if x == user:
                if WorL == 1:
                    data.loc[x, "WL"] = "W"
                elif WorL == 2:
                    data.loc[x, "WL"] = "L"
                elif WorL == 3:
                    data.loc[x, "WL"] = "-"
                temp = 0
                break

    # Save csv file with combined data
    data.to_csv(r'BetData.csv', index=False, header=True)


def table():
    data = read_data()
    print(data)


def menu_active(menu):
    # Go to active for the given menu

    if menu == "Plot":
        plot_betting_timeline()
        return 1
    if menu == "Add bet":
        add_bet()
        return 1
    if menu == "Confirm WL":
        confirm_WL()
        return 1
    if menu == "Table history":
        table()
        return 1
    elif menu == "Exit":
        # Stops the program
        return 0
    else:
        return 1
