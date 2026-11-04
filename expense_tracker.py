expenses = []

def safe_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: это не число. Попробуй еще раз.")

def add_expense(category, amount):
    expenses.append({"category": category, "amount": amount})

def show_expenses():
    if len(expenses) == 0:
        print("Расходов пока нет.")
        return
    for expense in expenses:
        print(f"{expense['category']}: {expense['amount']} руб.")

def get_stats():
    if len(expenses) == 0:
        print("Нет данных для статистики.")
        return
        
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
        
    average = total / len(expenses)
    
    print(f"Общая сумма: {total} рублей")
    print(f"Средний чек: {average} рублей")

def main():
    while True:
        print("\n--- Меню ---")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Статистика")
        print("4. Выход")
        
        choice = input("Выбери пункт (1-4): ")
        
        if choice == "1":
            category = input("На что потратил? ")
            amount = safe_float("Сколько? ")
            add_expense(category, amount)
            print("Расход добавлен!")
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            get_stats()
        elif choice == "4":
            print("Выход...")
            break
        else:
            print("Неверный ввод, выбери от 1 до 4.")

if __name__ == "__main__":
    main()