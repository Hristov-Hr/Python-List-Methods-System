def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def handle_append(lst):

    lst.append(input('Enter a value to add the list:'))
    return print(lst)


def handle_extend(lst):

    values_for_add = input('Enter the values to extend the list(comma-separated):').split(',')
    lst.extend(values_for_add)
    return print(lst)


def handle_insert(lst):

    index_for_insert = int(input('Enter an index:'))
    value_for_insert = input('Enter a value to insert:')
    lst.insert(index_for_insert, value_for_insert)
    return print(lst)


def handle_remove(lst):

    value_for_remove = input('Enter a value to remove:')
    if value_for_remove in lst:
        lst.remove(value_for_remove)
    else:
        print('Invalid value!')
    return print(lst)


def handle_pop(lst):

    index_to_pop = int(input("Enter an index to pop or leave empty to pop last item:"))
    if index_to_pop < len(lst):
        lst.pop(index_to_pop)
    else:
        lst.pop()

    return print(lst)


def handle_clear(lst):

    answer = input("Please enter 'Yes' if realy want to clear the list:")
    if answer.lower() == 'yes':
        lst.clear()
    return print(lst)


def handle_index(lst):

    search_for_value = input('Enter the value:')
    if search_for_value in lst:
        return print(lst.index(search_for_value))
    else:
        return print('The value was not found.')


def handle_count(lst):

    value = input('Enter a value to count:')
    return print(lst.count(value))


def handle_sort(lst):

    return print(lst.sort())


def handle_reverse(lst):

    return print(lst.reverse())


def handle_copy(lst):

    copied_list = lst.copy()
    return print(copied_list)


def main():
    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(',')

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
