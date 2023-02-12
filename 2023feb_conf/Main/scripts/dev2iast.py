def iast(src):
    consonants = {
        'क': 'k',
        'ख': 'kh',
        'ग': 'g',
        'घ': 'gh',
        'ङ': 'ṅ',
        'च': 'c',
        'छ': 'ch',
        'ज': 'j',
        'झ': 'jh',
        'ञ': 'ñ',
        'ट': 'ṭ',
        'ठ': 'ṭh',
        'ड': 'ḍ',
        'ढ': 'ḍh',
        'ण': 'ṇ',
        'त': 't',
        'थ': 'th',
        'द': 'd',
        'ध': 'dh',
        'न': 'n',
        'प': 'p',
        'फ': 'ph',
        'ब': 'b',
        'भ': 'bh',
        'म': 'm',
        'य': 'y',
        'र': 'r',
        'ल': 'l',
        'व': 'v',
        'श': 'ś',
        'ष': 'ṣ',
        'स': 's',
        'ह': 'h'}
    vowel_marks = {
        'ा': 'ā',
        'ि': 'i',
        'ी': 'ī',
        'ु': 'u',
        'ू': 'ū',
        'ृ': 'ṛ',
        'ॄ': 'ṝ',
        'ॢ': 'ḷ',
        'ॣ': 'ḹ',
        'े': 'e',
        'ै': 'ai',
        'ो': 'o',
        'ौ': 'au'}
    others = {
        'अ': 'a',
        'आ': 'ā',
        'इ': 'i',
        'ई': 'ī',
        'उ': 'u',
        'ऊ': 'ū',
        'ऋ': 'ṛ',
        'ॠ': 'ṝ',
        'ऌ': 'ḷ',
        'ॡ': 'ḹ',
        'ए': 'e',
        'ऐ': 'ai',
        'ओ': 'o',
        'औ': 'au',
        'ं': 'ṃ',
        'ः': 'ḥ',
        'ँ': 'ṁ',
        '।': '.',
        '॥': '..',
        'ऽ': '\'',
        '०': '0',
        '१': '1',
        '२': '2',
        '३': '3',
        '४': '4',
        '५': '5',
        '६': '6',
        '७': '7',
        '८': '8',
        '९': '9'}
    tgt = ''
    inc = 0
    while inc < len(src):
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else None
        if now in consonants:
            tgt += consonants[now]
            if nxt == '':
                inc += 1
            elif nxt not in vowel_marks:
                tgt += 'a'
        elif now in vowel_marks:
            tgt += vowel_marks[now]
        elif now in others:
            tgt += others[now]
        else:
            tgt += now
        inc += 1
    return tgt
