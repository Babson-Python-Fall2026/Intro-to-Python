
from load_data import load_data
from pprint import pprint as pp
from menu_print import menu_print

def pems():

    MENUS = load_data()

    stack = ["client_management"]

    '''
    Instead of hard-coding the starting menu, let's establish a convention:
    the first key in the menus dictionary identifies the starting menu.
    '''

    menu_names = list(MENUS.keys())
    stack = [menu_names[0]]
    state = {}

    while stack:

        cur_menu = MENUS[stack[-1]]
        menu_print(cur_menu)

        if len(stack) == 1:
            txt = "Choice (Enter to exit): "
        else:
            txt = "Choice (Enter to go back): "

        # keep asking until we get Enter or a valid choice
        while True:
            choice = input(txt).strip()
            if choice == '':
                break
            try:
                choice = int(choice)
                if 1 <= choice <= len(cur_menu['options']):
                    break
                else:
                    raise ValueError
            except ValueError:
                txt = 'Enter a valid choice: '

        # remove the last item on the stack if null string entered
        if choice == "":
            stack.pop()
            continue

        # get the option we chose. Remember cur_menu['options'] is a list (0 based)
        option = cur_menu["options"][choice - 1]

        # check if we have an action
        if option["action"] is not None:
            # if action returns False, stay on menu
            if option["action"](state) is False:
                continue

        # if option["next_menu"] != None append next_menu to stack
        if option["next_menu"] is not None:
            stack.append(option["next_menu"])

        # if option["next_menu"] is None, stay on menu
        else:
            print('\nNot Implemented - we go hungry\n')



    print("Logged off.")


if __name__ == "__main__":
    pems()
