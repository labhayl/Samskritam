#sandhi name

from scripts.sandhi.savarnadirgha import svn
from scripts.sandhi.guna import gun
from scripts.sandhi.vrddhi import vrd
def sandhi_final(vowel1,vowel2):
    if(gun(vowel1,vowel2)):
        return "guṇa sandhi"
    if(svn(vowel1,vowel2)):
        return "savarṇadīrgha sandhi"
    if(vrd(vowel1,vowel2)):
        return "vṛddhi sandhi"