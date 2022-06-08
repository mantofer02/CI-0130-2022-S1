DECORATOR = "$"


def count_ocurrencies(element, sequence_a, sequence_b):
    if sequence_a == DECORATOR*len(sequence_a) and DECORATOR in sequence_b and sequence_b != DECORATOR*len(sequence_b):
        occurrency = sequence_b
    elif sequence_b == DECORATOR*len(sequence_b) and DECORATOR in sequence_a and sequence_a != DECORATOR*len(sequence_a):
        occurrency = sequence_a
    else:
        occurrency = sequence_a + sequence_b

    print(element)
    print(sequence_a)
    print(sequence_b)
    print(element.count(occurrency))
    input()
    return element.count(occurrency)
