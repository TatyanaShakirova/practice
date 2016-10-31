# -*- coding: utf-8 -*-

if __name__ == '__main__':

    types_of_brackets = {1: "( )",
                         2: "{ }",
                         3: "[ ]"}

    methods_of_replacement = {"a": "first only",
                              "b": "all"}
    base_string = raw_input("input string\n")
    replace_string = raw_input("input string to replace to\n")
    brackets = input("choose type of brackets\n" + str(types_of_brackets)[1:-1] + "\n")
    method = raw_input("choose method of replacement\n" + str(methods_of_replacement)[1:-1] + "\n")

    # base_string = ")((()f()(1(3(5))))7(((9))a(13" # a***)7***)(13
    # replace_string = "***"
    # brackets = 1
    # method = "b"

    open_br, close_br = types_of_brackets.get(brackets, "( )").split()

    opens = []
    close = 0

    print "base string: " + base_string
    result_string = ""
    for i in range(len(base_string)):
        s = base_string[i]
        if s == open_br:
            if close == 0:
                opens.append(i)
            else:
                result_string += base_string[opens[0]:opens[-1]] + replace_string
                if method == "a":
                    result_string += base_string[close + 1:]
                    break
                else:
                    result_string += base_string[close + 1: i]
                    opens = [i]
                    close = 0
        elif s == close_br:
            if len(opens) > 0:
                if close != 0:
                    opens = opens[:-1]
                close = i
                if len(opens) == 1:
                    result_string += base_string[opens[0]:opens[-1]] + replace_string
                    if method == "a":
                        result_string += base_string[close + 1:]
                        break
                    else:
                        opens = []
                        close = 0
            else:
                result_string += s
        else:
            if close == 0 and len(opens) == 0:
                result_string += s
    if close == 0 and len(opens) != 0:
        result_string += base_string[opens[0]:]

    print "result string: " + result_string