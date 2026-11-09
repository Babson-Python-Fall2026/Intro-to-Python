def menu_print(menu, client_name):
    title = menu["title"]
    if client_name:
        title += f" — {client_name}"
    print(f"\n{title}")
    for number, option in enumerate(menu["options"], start=1):
        print(f"{number}) {option['menu_item']}")
