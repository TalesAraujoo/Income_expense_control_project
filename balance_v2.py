import csv
from datetime import date, time, datetime


def show_menu():
    print('------ Monthly Balance ------\n')
    print('1. Add Transaction')
    print('2. Expense')
    print('3. Report')
    print('4. Exit\n')
    option = input('Choose an option: ')
    get_option(int(option))


def get_option(chosen_option):

    match chosen_option:
        case 1:
            add_transaction()
            show_menu()

        case 2:
            show_menu()

        case 3: 
            show_report()
            show_menu()
            
        case 4:
            print('Exiting program...')
            print('Great job, keep shit updated!\n')


def get_transaction_type():
    print('\n------ Add transaction ------\n')
    print('1. Income')
    print('2. Expense\n')
    chosen_option = input('Choose your option: ')
    
    if chosen_option == '1':
        return 'Income'
    elif chosen_option == '2':
        return 'Expense'
    

def get_amount():

    tmp_amount = input('\nAmount: ')
    print('\n')
    return int(tmp_amount)


def get_date():
    
    print('\n------ Add transaction ------\n')
    print('1. Today')
    print('2. Different date')
    chosen_option = input('Choose your option: ')

    if chosen_option == '1':
        tmp_date = date.today().strftime("%d/%m/%Y")
        return tmp_date
    else:
        print('\n------ Different day ------\n')
        date_string = input('When was it (dd-mm-yyyy)? ')
        date_format = "%d-%m-%Y"
        parsed_date = datetime.strptime(date_string, date_format).date()
        tmp_date = parsed_date.strftime("%d/%m/%Y")
        return tmp_date
 

def get_category():
    with open('database_v2.csv') as csvfile:
        fnames = ['category', 'sub_category']
        reader = csv.DictReader(csvfile, fieldnames=fnames)
        

def create_dict():
    
    dict_data = {
        "transaction_id": 1,
        "transaction_type": get_transaction_type(),
        "amount": get_amount(),
        "date": get_date(),
        "category": 'normal',
        "sub_category": 'normal'
    }

    return dict_data


def add_transaction():
    with open('september.csv', 'a', newline='') as csvfile: 
               
        tmp_dict = create_dict()
        print(tmp_dict)
        # tmp_fieldnames = []
        # writer = csv.DictWriter(csvfile, fieldnames= tmp_fieldnames)
        # writer.writerow(tmp_dict)
        # print('\n')


def show_report():
    with open('september.csv', 'r', newline = '') as csvfile:
        csv_reader = csv.reader(csvfile)
        total_income = 0
        total_expenses = 0
        
        for row in csv_reader:
            if row[0] == 'Income':
                total_income += int(row[1])
            else:
                total_expenses += int(row[1])

        print('------ Report ------')
        print(f'Total income: {total_income:.2f}')
        print(f'Total expenses: {total_expenses:.2f}')
        print(f'Profitability: {(total_income - total_expenses):.2f}')    
        print('\n----------------------')
        input('Press any key to procced...')


show_menu()
