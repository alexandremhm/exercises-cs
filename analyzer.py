def analyze(text):
    report = ""
    report += f"o número de palavras é {count_words(text)}\n"
    report += f"Ocorrencias por caracter é {char_counter(text)}"

    return report


def count_words(text):
    return len(text.split(" "))


def char_counter(text):
    char_counter = dict()
    for char in text:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter


text_to_analyze = "a vida é bela"

print(analyze(text_to_analyze))
