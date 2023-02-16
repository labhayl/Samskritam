def savarnadirgha_sandhi(first_vowel, second_vowel):
  sandhi_vowels = [('अ', 'अ'), ('अ', 'आ'), ('आ', 'अ'), ('आ', 'आ'),
                    ('इ', 'इ'), ('इ', 'ई'), ('ई', 'इ'), ('ई', 'ई'),
                    ('उ', 'उ'), ('उ', 'ऊ'), ('ऊ', 'उ'), ('ऊ', 'ऊ'),
                    ('ऋ', 'ऋ'), ('ऋ', 'ॠ'), ('ॠ', 'ऋ'), ('ॠ', 'ॠ')]
  return (first_vowel, second_vowel) in sandhi_vowels

#print(savarnadirgha_sandhi('अ', 'अ')) # True
#print(savarnadirgha_sandhi('अ', 'आ')) # True
#print(savarnadirgha_sandhi('आ', 'इ')) # False
