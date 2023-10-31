while True:
    try:
        s = input('C++ code here please: ')
        if not s:
            continue
    except EOFError:
        break
    parser.parse(s)