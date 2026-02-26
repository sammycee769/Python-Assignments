from diaries import Diaries

diaries = Diaries()
current_diary = None

def input_prompt(message):
    return input(message)

def print_message(message):
    print(message)

def main_menu():
    while True:
        print_message("\n=== DIARY APP ===")
        print_message("1 -> Create Diary")
        print_message("2 -> Open Diary")
        print_message("3 -> Delete Diary")
        print_message("4 -> Exit")
        choice = input_prompt("Select option: ").strip()

        if choice == '1':
            create_diary()
        elif choice == '2':
            open_diary()
        elif choice == '3':
            delete_diary()
        elif choice == '4':
            print_message("Goodbye!")
            break
        else:
            print_message("Invalid option")

def create_diary():
    username = input_prompt("Enter username (or 0 to go back): ")
    if username == "0":
        return
    password = input_prompt("Enter password: ")
    try:
        diaries.add(username, password)
        print_message("Diary created successfully")
    except Exception as e:
        print_message(str(e))

def open_diary():
    global current_diary
    username = input_prompt("Enter username (or 0 to go back): ")
    if username == "0":
        return
    password = input_prompt("Enter password: ")
    try:
        current_diary = diaries.find_diary_by_username(username)
        current_diary.validate_password(password)
        current_diary.un_lock(password)
        print_message("Diary opened successfully")
        diary_menu()
    except Exception as e:
        print_message(str(e))

def diary_menu():
    global current_diary
    while True:
        print_message("\n=== DIARY MENU ===")
        print_message("1 -> Create Entry")
        print_message("2 -> View Entry")
        print_message("3 -> Update Entry")
        print_message("4 -> Delete Entry")
        print_message("5 -> Lock Diary")
        print_message("0 -> Back")
        choice = input_prompt("Select option: ").strip()

        if choice == '1':
            create_entry()
        elif choice == '2':
            view_entry()
        elif choice == '3':
            update_entry()
        elif choice == '4':
            delete_entry()
        elif choice == '5':
            lock_diary()
            break
        elif choice == '0':
            current_diary = None
            break
        else:
            print_message("Invalid option")

def create_entry():
    title = input_prompt("Enter title (or 0 to cancel): ")
    if title == "0":
        return
    content = input_prompt("Enter content: ")
    try:
        current_diary.create_entry(title, content)
        print_message("Entry created successfully")
    except Exception as e:
        print_message(str(e))

def view_entry():
    try:
        entry_id = int(input_prompt("Enter Entry ID (or 0 to go back): "))
        if entry_id == 0:
            return
        entry = current_diary.find_entry_by_id(entry_id)
        print_message(entry)
    except Exception as e:
        print_message(str(e))

def update_entry():
    try:
        entry_id = int(input_prompt("Enter Entry ID (or 0 to go back): "))
        if entry_id == 0:
            return
        title = input_prompt("Enter new title (leave empty to keep old): ")
        content = input_prompt("Enter new content (leave empty to keep old): ")
        current_diary.update_entry(entry_id, title, content)
        print_message("Entry updated successfully")
    except Exception as e:
        print_message(str(e))

def delete_entry():
    try:
        entry_id = int(input_prompt("Enter Entry ID (or 0 to cancel): "))
        if entry_id == 0:
            return
        current_diary.delete_entry(entry_id)
        print_message("Entry deleted successfully")
    except Exception as e:
        print_message(str(e))

def lock_diary():
    global current_diary
    current_diary.lock()
    print_message("Diary locked")
    current_diary = None

def delete_diary():
    username = input_prompt("Enter username of diary to delete (or 0 to cancel): ")
    if username == "0":
        return
    password = input_prompt(f"Enter password for diary '{username}': ")
    try:
        diaries.delete_diary(username, password)
        print_message(f"Diary '{username}' deleted successfully!")
    except Exception as e:
        print_message(f"Error: {str(e)}")

if __name__ == "__main__":
    main_menu()