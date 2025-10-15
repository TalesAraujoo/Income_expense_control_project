import csv, ast
from datetime import date, time, datetime, timedelta


def show_menu():
    print('\n------ Monthly Balance ------\n')
    print('1. Add Transaction')
    print('2. Change month')
    print('3. Reports')
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
    print('\n------ Transaction type ------\n')
    print('1. Income')
    print('2. Expense\n')
    chosen_option = input('Choose your option: ')
    
    if chosen_option == '1':
        return 'Income'
    elif chosen_option == '2':
        return 'Expense'
    

def get_amount():

    print('\n------ Amount ------\n')
    tmp_amount = input('Amount: ')
    print('\n')
    return float(tmp_amount)


def get_date():
    
    print('\n------ Choose a date ------\n')
    print('1. Today')
    print('2. Different date')
    print('')
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
 

def get_category(transaction_type):
    if transaction_type == 'Expense':
        file = 'expense'
    else:
        file = 'income'

    with open(f'.\Archive_manipulation\{file}_database_v2.csv') as csvfile:
        fnames = ['category', 'sub_category']
        reader = csv.DictReader(csvfile, fieldnames=fnames)

        tmp_list = []
        print('\n------ Choose a category ------\n')
        count = 1
        for item in reader:
            print(f'{count}. {item["category"]}')
            tmp_list.append(item['category'])
            count += 1

        print('')
        
        count = 1
        option = input('Choose an option: ')
        
        for item in tmp_list:
            if int(option) == count:
                return item
            else:
                count += 1


def get_sub_category(transaction_type, category):

    if transaction_type == 'Expense':
        file = 'expense'
    else:
        file = 'income'

    with open(f'.\Archive_manipulation\{file}_database_v2.csv') as csvfile:
        fnames = ['category', 'sub_category']
        reader = csv.DictReader(csvfile, fieldnames=fnames)

        print('\n------ Choose a sub-category ------\n')
        count = 1
        for item in reader:
            if category == item['category']:

                tmp_menu_list = ast.literal_eval(item['sub_category'])
            
                for item in tmp_menu_list:
                    print(f'{count}. {item}')
                    count += 1

                print('')
                count = 1
                option = input('Choose an option: ')
                for item in tmp_menu_list:

                    if int(option) == count:
                        return item
                    else:
                        count += 1 
                    

def get_transaction_id():
    with open('october.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        
        last = 0
        for item in reader:
            if item != None:
                last = item['transaction_id']
            
        return int(last)+1 


def create_dict():
    
    trans_id = get_transaction_id()
    trans_type = get_transaction_type()
    amount = get_amount()
    date = get_date()
    category = get_category(trans_type)
    sub_category = get_sub_category(trans_type, category)

    dict_data = {
        "transaction_id": trans_id,
        "transaction_type": trans_type,
        "amount": amount,
        "date": date,
        "category": category,
        "sub_category": sub_category
    }

    return dict_data


def dict_validation(tmp_dict):

    while True:
        print('\n------ Validate the info below ------\n')
    
        print(f'Amount: {tmp_dict['amount']}')
        print(f'Transaction Type: {tmp_dict['transaction_type']}')
        print(f'Date: {tmp_dict['date']}')
        print(f'Category: {tmp_dict['category']}')
        print(f'Sub-category: {tmp_dict['sub_category']}')

        print('\nShould we save it?\n')
        print('1. Yes')
        print('2. No')
        print('')
        validator = input('Choose your option: ')
        
        if validator == '1':
            print('\n****** SUCCESSFULLY SAVED! ******')
            return tmp_dict
            break
        else:
            print('\n****** Type it again ******')
            tmp_dict = create_dict()


def add_transaction():
    with open('october.csv', 'a', newline='') as csvfile: 
               
        tmp_dict = create_dict()
        final_dict = dict_validation(tmp_dict)
        tmp_fieldnames = ['transaction_id', 'transaction_type', 'amount', 'date', 'category', 'sub_category']
        writer = csv.DictWriter(csvfile, fieldnames= tmp_fieldnames)
        writer.writerow(final_dict)


def show_report():

    print('\n------ Report ------\n')
    print('1. Simple report')
    print('2. Detailed report')
    print('3. Report per specific periods\n')

    option = input('Choose your option: ')

    if option == '1':
        show_simple_report()
    elif option == '2':
        show_detailed_report()
    elif option == '3':
        show_per_period_report()


def show_simple_report():
    with open('october.csv', 'r', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        
        total_income = 0
        total_expenses = 0
        
        for row in reader:
            if row['transaction_type'] == 'Income':
                total_income += float(row['amount'])
            else:
                total_expenses += float(row['amount'])

        print('\n------ Report ------\n')
        print(f'Total income: {total_income:.2f}')
        print(f'Total expenses: {total_expenses:.2f}')
        print('--------------------')
        print(f'Profitability: {(total_income - total_expenses):.2f}')
        print('')  
        input('Press ENTER to procced...')


def show_detailed_report():
    with open('october.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        total_apps = 0
        total_uber = 0
        total_99 = 0
        total_indrive = 0
        total_concerts = 0
        total_market = 0
        total_gas = 0
        total_utilities = 0
        total_fixed_expenses = 0
        total_food_groceries = 0
        total_entertainment = 0
       
        for item in reader:
            if item['transaction_type'] == 'Income':
                
                if item['sub_category'] == 'Uber':
                    total_uber += float(item['amount'])
                elif item['sub_category'] == '99':
                    total_99 += float(item['amount'])
                elif item['sub_category'] == 'inDrive':
                    total_indrive += float(item['amount'])

                if item['category'] == 'Shows':
                    total_concerts += float(item['amount']) 

            else:
                if item['category'] == 'Food and Groceries':
                    total_food_groceries += float(item['amount'])
                    if item['sub_category'] == 'Supermarket':
                        total_market += float(item['amount'])
                elif item['category'] == 'Fixed Expenses':
                    total_fixed_expenses += float(item['amount'])
                    if item['sub_category'] == 'Gas':
                        total_gas += float(item['amount'])
                elif item['category'] == 'Utility':
                    total_utilities += float(item['amount'])
                elif item['category'] == 'Entertainment':
                    total_entertainment += float(item['amount'])

        total_apps = total_uber + total_99 + total_indrive

        print('\n--- INCOME ---\n')
        print(f'TOTAL APPs:  R$ {total_apps:.2f}')
        print(f'- Uber:    R$ {total_uber:.2f}')
        print(f'- 99:      R$ {total_99:.2f}')
        print(f'- inDrive: R$ {total_indrive:.2f}')
        print('')
        print(f'- Shows:   R$ {total_concerts:.2f}')
        print('')
        print(f'TOTAL INCOME: R$ {(total_apps + total_concerts):.2f}')
        print('\n--- EXPENSES ---\n')
        print(f'- Utilities:          R$ {total_utilities:.2f}')
        print(f'- Food and Groceries: R$ {total_food_groceries:.2f}')
        print(f'     - Supermarket:   R$ {total_market:.2f}')
        print(f'- Fixed Expenses:     R$ {total_fixed_expenses:.2f}')
        print(f'     - Gas:           R$ {total_gas:.2f}')
        print(f'- Entertainment:      R$ {total_entertainment:.2f}')
        print('')
        print(f'TOTAL EXPENSES:       R$ {(total_utilities + total_fixed_expenses + total_entertainment + total_food_groceries):.2f}')


def show_per_period_report():
    print('\n------ Choose a period ------\n')
    print('1. This week')
    print('2. This month')
    print('3. This year')
    print('4. Specific date')
    print('')

    option = input('Choose an option: ')

    if option == '1':
        get_weekly_report()
    elif option == '2':
        pass


def get_weekly_report():
    today = date.today()
    start_of_week = today - timedelta(days = today.weekday())
    print(start_of_week)
    

show_menu()
