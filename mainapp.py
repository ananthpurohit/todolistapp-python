todos = []

while True:
    user_action = input("Type add, show, edit, pop or exit: ")
    user_action = user_action.strip() # removes unwanted spaces after the required text

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print("Your todos are:")
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index + 1}. {item}") #f-strings allows customization
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number =-1
            new_todo = input("Type your preferred edit: ")
            todos[number] = new_todo
        case 'pop':
            number = int(input("Number of todo to pop: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:  #allows code to execute this case when none of the other case match
            print("Hey, you entered an unknown command!")

print("Bye")