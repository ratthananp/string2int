def string_to_int(value: str) -> int:
    filter_int = int(''.join(list(filter(str.isdigit, value))))
    print(filter_int)


if __name__ == '__main__':
    string_to_int('abc573')
    string_to_int('a5b7c3')

