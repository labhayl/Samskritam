#sandhi name

import sname.savarnadirgha_sandhi as svn
import sname.guna_sandhi as gun
import sname.vrddhi_sandhi as vrd
def sandhi_final(vowel1,vowel2):
    if(gun.guna_sandhi(vowel1,vowel2)):
        return "guṇa sandhi"
    if(svn.savarnadirgha_sandhi(vowel1,vowel2)):
        return "savarṇadīrgha sandhi"
    if(vrd.vrddhi_sandhi(vowel1,vowel2)):
        return "vṛddhi sandhi"