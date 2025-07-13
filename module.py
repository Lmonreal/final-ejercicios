import csv

def promedio_temperaturas(filename):
    try:
        with open(filename, 'r') as f:
            cities_dict = dict()
            csv_reader = csv.reader(f)
            next(csv_reader)

            for row in csv_reader:
                if row[0] not in cities_dict.keys():
                    cities_dict[row[0]] = [int(row[1])]
                else:
                    cities_dict[row[0]].append(int(row[1]))
            try:
                with open('promedio_temperaturas.csv', 'x', newline='') as fi:
                    writer = csv.writer(fi)
                    cities_items = list(cities_dict.items())
                    writer.writerow(['Ciudad', 'Promedio'])
                    for row in cities_items:
                        writer.writerow([row[0], sum(row[1])/len(row[1])])

            except FileExistsError:
                print("ERROR: promedio_temperaturas.csv File Exists")


    except FileNotFoundError:
        print("ERROR: File not found")


def count_words_per_line(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            countbuffer = 0
            for line in lines:
                countbuffer += 1
                words = line.count(' ') + 1
                print(f"Linea {countbuffer}: {words} palabras")

    except FileNotFoundError:
        print("ERROR: Archivo no encontrado")


def verificar_sesiones(user_file, session_file):
    try:
        with open(user_file, 'r') as f:
            file_names = f.readlines()
        
        try:
            with open(session_file, 'r') as f:
                file_sessions = f.read()
                for name in file_names:
                    if name in file_sessions:
                        print(f"Valid User: {name.strip()}")
                    else:
                        print(f"Invalid User: {name.strip()}")

        except FileNotFoundError:
            print(f"ERROR: File {session_file} not found")

    except FileNotFoundError:
        print(f"ERROR: File {user_file} not found")


def gastos_por_categoria(my_file):
    try:
        with open(my_file, 'r') as f:
            ind_expenses = f.readlines()
            concatenated_expenses = []
            filtered_expenses = []
            expense_dict = dict()
            for expense in ind_expenses:
                concatenated_expenses.append(expense.strip())
            for catandcost in concatenated_expenses:
                filtered_expenses.append(catandcost.split(':'))
            
            for sublist in filtered_expenses:
                if sublist[0] not in expense_dict.keys():
                    expense_dict[sublist[0]] = [float(sublist[1])]
                else:
                    expense_dict[sublist[0]].append(float(sublist[1]))

        try:
            with open('totales.txt', 'x') as f:
                for item in list(expense_dict.items()):
                    line = f"{item[0]}: ${sum(item[1])}\n"
                    f.write(line)

        except FileExistsError:
            print(f"ERROR: File already exists")

    except FileNotFoundError:
        print(f"ERROR: File {my_file} not found.")


def estadisticas_notas(csv_file):
    try:
        with open(csv_file, 'r') as f:
            students = dict()
            csv_reader = csv.reader(f)
            next(csv_reader)

            for row in csv_reader:
                if row[0] not in list(students.keys()):
                    students[row[0]] = [int(row[1])]
                else:
                    students[row[0]].append(int(row[1]))
        for tup in list(students.items()):
            print(f'{tup[0]}: promedio {sum(tup[1])/len(tup[1])}')



    except FileNotFoundError:
        print(f'ERROR: {csv_file} not found')


if __name__ == '__main__':
    promedio_temperaturas('temperaturas.csv')
    count_words_per_line('content.txt')
    verificar_sesiones('users.txt', 'sessions.txt')
    gastos_por_categoria('gastos.txt')
    estadisticas_notas('notas.csv')

