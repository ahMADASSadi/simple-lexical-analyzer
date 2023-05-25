KEYWORDS = [
    "let", "in", "end", "print", "if", "else", "while", "do", "and", "or", "not"
]
SYMBOLS = ["==", "<>", ">", ">=", "<", "<=", "+", "-", "*", "/", "**", "=", "(", ")", ",", ";"]
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

transition_table = dict()

transition_table[(0, "a")] = 1
transition_table[(0, "b")] = 1
transition_table[(0, "c")] = 1
transition_table[(0, "d")] = 1
transition_table[(0, "e")] = 1
transition_table[(0, "f")] = 1
transition_table[(0, "g")] = 1
transition_table[(0, "h")] = 1
transition_table[(0, "i")] = 1
transition_table[(0, "j")] = 1
transition_table[(0, "k")] = 1
transition_table[(0, "l")] = 1
transition_table[(0, "m")] = 1
transition_table[(0, "n")] = 1
transition_table[(0, "o")] = 1
transition_table[(0, "p")] = 1
transition_table[(0, "q")] = 1
transition_table[(0, "r")] = 1
transition_table[(0, "s")] = 1
transition_table[(0, "t")] = 1
transition_table[(0, "u")] = 1
transition_table[(0, "v")] = 1
transition_table[(0, "w")] = 1
transition_table[(0, "x")] = 1
transition_table[(0, "y")] = 1
transition_table[(0, "z")] = 1
transition_table[(0, ".")] = 4
transition_table[(0, "0")] = 5
transition_table[(0, "1")] = 5
transition_table[(0, "2")] = 5
transition_table[(0, "3")] = 5
transition_table[(0, "4")] = 5
transition_table[(0, "5")] = 5
transition_table[(0, "6")] = 5
transition_table[(0, "7")] = 5
transition_table[(0, "8")] = 5
transition_table[(0, "9")] = 5
transition_table[(0, "<")] = 8
transition_table[(0, ">")] = 8
transition_table[(0, "=")] = 8
transition_table[(0, "*")] = 9
transition_table[(0, "+")] = 10
transition_table[(0, "-")] = 10
transition_table[(0, "<")] = 10
transition_table[(0, ">")] = 10
transition_table[(0, "*")] = 10
transition_table[(0, "=")] = 10
transition_table[(0, "/")] = 10
transition_table[(0, ",")] = 10
transition_table[(0, ";")] = 10
transition_table[(0, "(")] = 10
transition_table[(0, ")")] = 10
transition_table[(0, "{")] = 10
transition_table[(0, "}")] = 10

transition_table[(1, "a")] = 1
transition_table[(1, "b")] = 1
transition_table[(1, "c")] = 1
transition_table[(1, "d")] = 1
transition_table[(1, "e")] = 1
transition_table[(1, "f")] = 1
transition_table[(1, "g")] = 1
transition_table[(1, "h")] = 1
transition_table[(1, "i")] = 1
transition_table[(1, "j")] = 1
transition_table[(1, "k")] = 1
transition_table[(1, "l")] = 1
transition_table[(1, "m")] = 1
transition_table[(1, "n")] = 1
transition_table[(1, "o")] = 1
transition_table[(1, "p")] = 1
transition_table[(1, "q")] = 1
transition_table[(1, "r")] = 1
transition_table[(1, "s")] = 1
transition_table[(1, "t")] = 1
transition_table[(1, "u")] = 1
transition_table[(1, "v")] = 1
transition_table[(1, "w")] = 1
transition_table[(1, "x")] = 1
transition_table[(1, "y")] = 1
transition_table[(1, "z")] = 1
transition_table[(1, "0")] = 1
transition_table[(1, "1")] = 1
transition_table[(1, "2")] = 1
transition_table[(1, "3")] = 1
transition_table[(1, "4")] = 1
transition_table[(1, "5")] = 1
transition_table[(1, "6")] = 1
transition_table[(1, "7")] = 1
transition_table[(1, "8")] = 1
transition_table[(1, "9")] = 1

transition_table[(4, "0")] = 6
transition_table[(4, "1")] = 6
transition_table[(4, "2")] = 6
transition_table[(4, "3")] = 6
transition_table[(4, "4")] = 6
transition_table[(4, "5")] = 6
transition_table[(4, "6")] = 6
transition_table[(4, "7")] = 6
transition_table[(4, "8")] = 6
transition_table[(4, "9")] = 6

transition_table[(5, "0")] = 5
transition_table[(5, "1")] = 5
transition_table[(5, "2")] = 5
transition_table[(5, "3")] = 5
transition_table[(5, "4")] = 5
transition_table[(5, "5")] = 5
transition_table[(5, "6")] = 5
transition_table[(5, "7")] = 5
transition_table[(5, "8")] = 5
transition_table[(5, "9")] = 5
transition_table[(5, ".")] = 4
transition_table[(5, "e")] = 7

transition_table[(6, "0")] = 6
transition_table[(6, "1")] = 6
transition_table[(6, "2")] = 6
transition_table[(6, "3")] = 6
transition_table[(6, "4")] = 6
transition_table[(6, "5")] = 6
transition_table[(6, "6")] = 6
transition_table[(6, "7")] = 6
transition_table[(6, "8")] = 6
transition_table[(6, "9")] = 6
transition_table[(6, "e")] = 7

transition_table[(7, ".")] = 11
transition_table[(7, "0")] = 12
transition_table[(7, "1")] = 12
transition_table[(7, "2")] = 12
transition_table[(7, "3")] = 12
transition_table[(7, "4")] = 12
transition_table[(7, "5")] = 12
transition_table[(7, "6")] = 12
transition_table[(7, "7")] = 12
transition_table[(7, "8")] = 12
transition_table[(7, "9")] = 12
transition_table[(7, "+")] = 14
transition_table[(7, "-")] = 14

transition_table[(8, "=")] = 10
transition_table[(9, "*")] = 10

transition_table[(10, "=")] = 10
transition_table[(10, "*")] = 10
transition_table[(10, ">")] = 10

transition_table[(11, "0")] = 13
transition_table[(11, "1")] = 13
transition_table[(11, "2")] = 13
transition_table[(11, "3")] = 13
transition_table[(11, "4")] = 13
transition_table[(11, "5")] = 13
transition_table[(11, "6")] = 13
transition_table[(11, "7")] = 13
transition_table[(11, "8")] = 13
transition_table[(11, "9")] = 13

transition_table[(12, "0")] = 12
transition_table[(12, "1")] = 12
transition_table[(12, "2")] = 12
transition_table[(12, "3")] = 12
transition_table[(12, "4")] = 12
transition_table[(12, "5")] = 12
transition_table[(12, "6")] = 12
transition_table[(12, "7")] = 12
transition_table[(12, "8")] = 12
transition_table[(12, "9")] = 12
transition_table[(12, "9")] = 12
transition_table[(12, ".")] = 13

transition_table[(13, "0")] = 13
transition_table[(13, "1")] = 13
transition_table[(13, "2")] = 13
transition_table[(13, "3")] = 13
transition_table[(13, "4")] = 13
transition_table[(13, "5")] = 13
transition_table[(13, "6")] = 13
transition_table[(13, "7")] = 13
transition_table[(13, "8")] = 13
transition_table[(13, "9")] = 13

transition_table[(14, ".")] = 11
transition_table[(14, "0")] = 12
transition_table[(14, "1")] = 12
transition_table[(14, "2")] = 12
transition_table[(14, "3")] = 12
transition_table[(14, "4")] = 12
transition_table[(14, "5")] = 12
transition_table[(14, "6")] = 12
transition_table[(14, "7")] = 12
transition_table[(14, "8")] = 12
transition_table[(14, "9")] = 12

final_states = {1, 4, 5, 6, 8, 9, 10, 11, 12, 13, }
num_states = [4, 5, 6, 11, 12, 13, ]
i = 0


def transitions(cur_state, value):
    if (cur_state, value) not in transition_table:
        return 0
    else:
        new_state = transition_table[(cur_state, value)]

        return new_state


def next_char(text):
    global i
    if i < len(text):
        char = text[i]
        i += 1
        return char


def dfa(start, final_state, text):
    token_list = []
    error_list = []
    new_lex = []
    final_token = ""
    s = start
    c = next_char(text)
    if c == " ":
        c = next_char(text)
    lexeme = ""
    while len(text) - 1:
        if c is None:
            for item in token_list:
                final_token += item
            with open(file="output.holo", mode="w") as res_file:
                # res_file.write(logo)
                res_file.write(final_token)
                res_file.write(f"\nUnacceptable lexemes are:\n{error_list}")
            print(final_token)
            # print(new_lex)
            print(f"\nUnacceptable lexemes are:\n{error_list}")
            return
        if not c == " ":
            lexeme += c
        s = transitions(s, c)
        c = next_char(text)
        is_error = False
        if s in final_state:
            if c == " ":
                if transitions(s, c) == 0:
                    if s in num_states:
                        token_list.append(f"[num({lexeme})]\n")
                        lexeme = ""
                    elif s in [8, 9, 10, ]:
                        token_list.append(f"[{lexeme}]\n")
                        lexeme = ""
                    else:
                        if lexeme in KEYWORDS:
                            token_list.append(f"[{lexeme}(keyword)]\n")
                            lexeme = ""
                        else:
                            token_list.append(f"[id({lexeme})]\n")
                            lexeme = ""
                else:
                    pass
            else:
                if transitions(s, c) == 0:
                    if s in num_states:
                        if transitions(s, c) == 1:
                            error_list.append(lexeme)
                            lexeme = ""
                            s = 0
                        else:
                            token_list.append(f"[num({lexeme})]\n")
                            lexeme = ""
                            s = 0

                    elif s in [8, 9, 10, ]:
                        if c == "=":
                            token_list.append(f"[{lexeme + c}]\n")
                            lexeme = ""
                            s = 0
                            c = ""
                        else:
                            token_list.append(f"[{lexeme}]\n")
                            lexeme = ""
                            s = 0
                    else:
                        if lexeme in KEYWORDS:
                            token_list.append(f"[{lexeme}(keyword)]\n")
                            lexeme = ""
                        else:
                            token_list.append(f"[id({lexeme})]\n")
                            lexeme = ""
                        s = 0

        elif s == 0:
            error_list += lexeme
            lexeme = ""

with open(file="input.txt", mode="r") as file:
    x = file.readlines()
    d = " ".join(x)
    d = d.replace('\n', " ")
    d = d.replace("     ", " ")
    d = d.replace("    ", " ")
    d = d.replace("   ", " ")
    d = d.replace("  ", " ")
    d = d.replace('\t', " ")

print(d)
dfa(0, final_states, d)
