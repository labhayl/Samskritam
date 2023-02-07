def vrddhi_sandhi(first_vowel, second_vowel):
    sandhi_vowels = [
        ("अ", "ए"),
        ("अ", "ऐ"),
        ("अ", "ओ"),
        ("अ", "औ"),
        ("अ", "ऋ"),
        ("अ", "ॠ"),
        ("आ", "ए"),
        ("आ", "ऐ"),
        ("आ", "ओ"),
        ("आ", "औ"),
        ("आ", "ऋ"),
        ("आ", "ॠ"),
    ]    
    return (first_vowel, second_vowel) in sandhi_vowels

print(vrddhi_sandhi('अ', 'अ')) # False
print(vrddhi_sandhi('अ', 'ओ')) # True
print(vrddhi_sandhi('आ', 'ए')) # True
