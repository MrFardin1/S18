from unittest import TestCase, main
from chargement_buggy import charger_catalogue, _CATALOGUE_JSON
from livre_s18_squelette import Livre, LivreNumerique, LivreAudio



class TestBuggy(TestCase):
    
    def test_garde_fou(self):
        Catalogue_charge = charger_catalogue(_CATALOGUE_JSON)
        livre = Catalogue_charge[0]
        livre1 = Catalogue_charge[1]
        livre2 = Catalogue_charge[2]
        self.assertIs(type(livre), Livre)
        self.assertIs(type(livre1), LivreNumerique)
        self.assertIs(type(livre2), LivreAudio)


if __name__ == "__main__":
    main()
