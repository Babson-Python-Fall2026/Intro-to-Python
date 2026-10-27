def hello(name):
    print(f"Hello, {name}")


actions = {
    'hello': hello
}

options={'action': 'hello'}

action = actions[options['action']]

action('bob')