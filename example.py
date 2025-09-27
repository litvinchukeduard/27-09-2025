example_dict = {'value': 100, 'title': 'Test'}

def example(title: str, value: int):
    print(f'Title: {title}')
    print(f'Value: {value}')

# example(example_dict['title'], example_dict['value'])
# title, value, _ = example_dict

example(**example_dict)
