# -*- encoding: utf8 -*-

import unittest
import hashlib


from zadania import *


class TestKolokwium1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(hashlib.md5(open("test_all.py",'rb').read()).hexdigest())


    def test01(self):
        self.assertEqual(czy_parzysta(2), True)
        self.assertEqual(czy_parzysta(1), False)

    def test02(self):
        self.assertEqual([], przepisz([14]), [])
        self.assertEqual([1,2], przepisz([1,2,14,15]))

    def test03(self):
        self.assertEqual("7", podzielne_7_nie_5(7,7))
        self.assertEqual("", podzielne_7_nie_5(29, 35))

    def test04(self):
        self.assertEqual(podzielne_7_nie_5(2000, 3201), "2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199")

    def test05(self):
        self.assertEqual(przesuniecia([]), [])
        self.assertEqual(przesuniecia([1]), [[1]])

    def test06(self):
        self.assertEqual(przesuniecia([3,2,1]), [[3,2,1],[2,1,3],[1,3,2]])
        self.assertEqual(przesuniecia([10, 10]), [[10, 10], [10, 10]])

    def test07(self):
        self.assertTrue(wybrakowana_klawiatura("abc","ab"))
        self.assertFalse(wybrakowana_klawiatura("ab", "abc"))
        self.assertTrue(wybrakowana_klawiatura("abc","aabbcc"))
        self.assertTrue(wybrakowana_klawiatura("aaaabbbccc", "cc"))

    def test08(self):
        self.assertTrue(wybrakowana_klawiatura("",""))
        self.assertTrue(wybrakowana_klawiatura("ABC","abc"))
        self.assertTrue(wybrakowana_klawiatura("Ma", "mAMaMAma"))

    def test09(self):
        self.assertTrue(bezpieczne_haslo("qwe123!@#"))
        self.assertTrue(bezpieczne_haslo("qwe123!@#"))
        self.assertFalse(bezpieczne_haslo("a!1"))
        self.assertFalse(bezpieczne_haslo("123"))

    def test10(self):
        self.assertFalse(bezpieczne_haslo("1234567890"))
        self.assertFalse(bezpieczne_haslo("abcdefghij"))
        self.assertFalse(bezpieczne_haslo("abcdefghijklm1!"))
        self.assertFalse(bezpieczne_haslo("12345678!a"))
        self.assertFalse(bezpieczne_haslo("!!!!!!!!!a1"))

    def test11(self):
        self.assertEqual(2, palec_ksiegowej([1,2,3]))
        self.assertEqual(2, palec_ksiegowej([1, 3]))
        self.assertEqual(2, palec_ksiegowej([3, 1]))
        self.assertEqual(1, palec_ksiegowej([2, 1]))
        self.assertEqual(1, palec_ksiegowej([8, 9]))
        self.assertEqual(2, palec_ksiegowej([6, 4]))
        self.assertEqual(4, palec_ksiegowej([6, 4, 6]))
        self.assertEqual(5, palec_ksiegowej([4, 6, 4, 5]))

    def test12(self):
        self.assertEqual(1, palec_ksiegowej([7, 4]))
        self.assertEqual(1, palec_ksiegowej([5, 8]))
        self.assertEqual(1, palec_ksiegowej([6, 3]))
        self.assertEqual(1, palec_ksiegowej([2, 5]))
        self.assertEqual(2, palec_ksiegowej([2,5,8]))
        self.assertEqual(2, palec_ksiegowej([8,5,2]))
        self.assertEqual(3, palec_ksiegowej([7, 1, 4]))
        self.assertEqual(4, palec_ksiegowej([8, 2, 8]))

    def test13(self):
        self.assertEqual(2, palec_ksiegowej([1, 5]))
        self.assertEqual(2, palec_ksiegowej([4, 8]))
        self.assertEqual(2, palec_ksiegowej([8, 6]))
        self.assertEqual(2, palec_ksiegowej([7, 5]))
        self.assertEqual(4, palec_ksiegowej([7, 3]))

    def test14(self):
        self.assertEqual(8, palec_ksiegowej([1, 7, 9, 3, 1]))
        self.assertEqual(12, palec_ksiegowej([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual(12, palec_ksiegowej([9, 8, 7, 6, 5, 4, 3, 2, 1]))
        self.assertEqual(8, palec_ksiegowej([1, 2, 3, 6, 9, 8, 7, 4, 5]))
        self.assertEqual(8, palec_ksiegowej([9, 6, 3, 2, 1, 4, 7, 8, 5]))
        self.assertEqual(13, palec_ksiegowej([7, 5, 3, 6, 8, 4, 2, 6]))

    def test15(self):
        self.assertEqual(8, palec_ksiegowej([1, 7, 5, 9, 3]))
        self.assertEqual(4, palec_ksiegowej([1, 9]))
        self.assertEqual(4, palec_ksiegowej([7, 3]))
        self.assertEqual(7, palec_ksiegowej([3, 7, 6]))
        self.assertEqual(0, palec_ksiegowej([3]))

    def test16(self):
        self.assertTrue(wiecej_ujemnych([-1, -2, 1]))
        self.assertTrue(wiecej_ujemnych([-3, 1, -3]))
        self.assertFalse(wiecej_ujemnych([-3, 1, -3, 5]))
        self.assertFalse(wiecej_ujemnych([]))

    def test17(self):
        self.assertEqual([0, 2, 1], sprzatanie([3, 1, 2]))
        self.assertEqual([5, 4, 3, 2, 1, 0], sprzatanie([1, 2, 3, 4, 5, 6]))
        self.assertEqual([3, 4, 5, 2, 6, 1, 7, 0], sprzatanie([1, 3, 5, 8, 7, 6, 4, 2]))

    def test18(self):
        self.assertEqual([], sprzatanie([]))
        self.assertEqual([0], sprzatanie([8]))
        self.assertEqual([0,3,1,2], sprzatanie([5,2,2,5]))

    def test19(self):
        self.assertTrue(czy_posortowane([5,3,1,0,-8]))
        self.assertTrue(czy_posortowane([5]*10))
        self.assertFalse(czy_posortowane([5,2,1, 0, -6, 1]))
        self.assertFalse(czy_posortowane([1,2,3,4,7,10,18,22]))


    def test20(self):
        self.assertEqual(1, najmniejsza_suma([[1]]))
        self.assertEqual(6, najmniejsza_suma([[1, 2, 3]]))
        self.assertEqual(1, najmniejsza_suma([[1], [2], [3]]))


    def test21(self):
        self.assertEqual(4, najmniejsza_suma([[1, 6], [5, 2], [3, 1]]))
        self.assertEqual(5, najmniejsza_suma([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
        self.assertEqual(4, najmniejsza_suma([[2, 2, 2], [2, 1, 20], [2, 1, 2]]))

    def test22(self):
        self.assertEqual(['abc'], stos_wyrazow(['abc']))
        self.assertEqual(['def', 'abc'], stos_wyrazow(['abc', 'def']))

    def test23(self):
        self.assertEqual(['defabc'], stos_wyrazow(['abc', 'def', 0]))
        self.assertEqual(['defabc'], stos_wyrazow(['abc', 'def', 0]))
        self.assertEqual(['dcb','a'], stos_wyrazow(['a', 'b', 'c', 'd', 0, 0]))
        self.assertEqual(['defabc'], stos_wyrazow(['abc', 'def', 0]))
        self.assertEqual(['defabc'], stos_wyrazow(['abc', 'def', 0]))
        self.assertEqual(['dcb', 'a'], stos_wyrazow(['a', 'b', 'c', 'd', 0, 0]))

    def test24(self):
        self.assertEqual(['C','b','a'], stos_wyrazow(['a', 'b', 'c', 1]))
        self.assertEqual(['CCBBAAA'], stos_wyrazow(['CCBBaaa', 1]))
        self.assertEqual(['ab'], stos_wyrazow(['abc', 2]))

    def test25(self):
        self.assertEqual(6, suma_rekurencyjna([1, 2, 3]))
        self.assertEqual(0, suma_rekurencyjna([]))

    def test26(self):
        self.assertEqual(6, suma_rekurencyjna([[[[[1, 2, 3]]]]]))
        self.assertEqual(36, suma_rekurencyjna([1, [2, 3], [4, [5, 6, [7, 8]]]]))

    def test27(self):
        self.assertEqual(0, zliczanie_stringow([]))
        self.assertEqual(2, zliczanie_stringow(['aa','b','cac']))
        self.assertEqual(1, zliczanie_stringow(['aaa', 'ab', 'acac']))
        self.assertEqual(5, zliczanie_stringow(['aa', 'bb', 'cc', 'dd', 'aa']))

    def test28(self):
        self.assertEqual(3, wieksza(3,1))
        self.assertEqual(30, wieksza(30, 30))
        self.assertEqual(-1, wieksza(-1, -20))

    def test29(self):
        self.assertFalse(zostaje_w_domu(False, False, False))
        self.assertFalse(zostaje_w_domu(False, False, True))
        self.assertFalse(zostaje_w_domu(False, True, False))
        self.assertTrue(zostaje_w_domu(False, True, True))
        self.assertTrue(zostaje_w_domu(True, False, False))
        self.assertTrue(zostaje_w_domu(True, False, True))
        self.assertTrue(zostaje_w_domu(True, True, False))
        self.assertTrue(zostaje_w_domu(True, True, True))

    def test30(self):
        self.assertTrue(palindrom("alla"))
        self.assertTrue(palindrom("a"))
        self.assertFalse(palindrom("zalla"))


if __name__ == '__main__':
    print(hashlib.md5("test_all.py").hexdigest())
    unittest.main()