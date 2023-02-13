def gun(first_vowel, second_vowel):
    sandhi_vowels = [
        ("अ", "इ"),
        ("अ", "ई"),
        ("अ", "उ"),
        ("अ", "ऊ"),
        ("अ", "ऋ"),
        ("अ", "ॠ"),
        ("आ", "इ"),
        ("आ", "ई"),
        ("आ", "उ"),
        ("आ", "ऊ"),
        ("आ", "ऋ"),
        ("आ", "ॠ"),
    ]
    return (first_vowel, second_vowel) in sandhi_vowels

#print(guna_sandhi('अ', 'अ')) # False
#print(guna_sandhi('अ', 'आ')) # False
#print(guna_sandhi('आ', 'इ')) # True
