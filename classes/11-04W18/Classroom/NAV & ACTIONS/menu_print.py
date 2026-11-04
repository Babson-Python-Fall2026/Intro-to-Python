def menu_print(menu):
    title = menu["title"]
   
    print(f"\n{title}")
    for number, option in enumerate(menu["options"], start=1):
        print(f"{number}) {option['menu_item']}")
