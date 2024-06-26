from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    if my_int1 > my_int2:
        comparison_result = my_int1
    elif my_int1 < my_int2:
        comparison_result = my_int2
    else:
        comparison_result = 0

    return [Output(comparison_result, "comparison_output", party1)]
