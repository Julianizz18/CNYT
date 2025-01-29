import Libcplx as lc
import unittest
import math

class TestComplexOperations(unittest.TestCase):
    def test_addition1(self): # (2+3i)+(-1+4i) = 1+7i
        resultado = lc.sumaC([2,3],[-1,4])
        self.assertAlmostEqual(resultado[0], 1)
        self.assertAlmostEqual(resultado[1], 7)

    def test_addition2(self): # (3+4i)+7i = 3+11i
        resultado = lc.sumaC([3,4],[0,7])
        self.assertAlmostEqual(resultado[0], 3)
        self.assertAlmostEqual(resultado[1], 11)
    
    def test_subtraction1(self): # (4+4√3i)-(-√2+i) = 5.4142+5.9282i
        resultado = lc.restaC((4,4*math.sqrt(3)),(-math.sqrt(2),1))
        self.assertAlmostEqual(resultado[0], 5.4142)
        self.assertAlmostEqual(resultado[1], 5.9282)

    def test_subtraction2(self): # (8+√11i)-(3+4i) = 5-0.6834i
        resultado = lc.restaC((8,math.sqrt(11)),(3,4))
        self.assertAlmostEqual(resultado[0], 5)
        self.assertAlmostEqual(resultado[1], -0.6834)

    def test_multiplication1(self): # (2+3i)**2 = -5+12i
        resultado = lc.multiplicacionC([2,3],[2,3])
        self.assertAlmostEqual(resultado[0], -5)
        self.assertAlmostEqual(resultado[1], 12)

    def test_multiplication2(self): # (-2-i)*(-1-2i) = 5i
        resultado = lc.multiplicacionC([-2,-1],[-1,-2])
        self.assertAlmostEqual(resultado[0], 0)
        self.assertAlmostEqual(resultado[1], 5)
    
    def test_division1(self): # i/(3-2i) = -0.1538+0.2308i
        resultado = lc.divisionC([0,1],[3,-2])
        self.assertAlmostEqual(resultado[0], -0.1538)
        self.assertAlmostEqual(resultado[1], 0.2308)

    def test_division2(self): # (20+30i)/(3+i) = 9+7i
        resultado = lc.divisionC([20,30],[3,1])
        self.assertAlmostEqual(resultado[0], 9)
        self.assertAlmostEqual(resultado[1], 7)
    
    def test_modulus1(self): # |(19/2)-(3/4)i| = 9.5296
        resultado = lc.moduloC([(19/2),(-3/4)])
        self.assertAlmostEqual(resultado, 9.5296)

    def test_modulus2(self): # |3+(5/2)i| = 3.9051
        resultado = lc.moduloC([3,(5/2)])
        self.assertAlmostEqual(resultado, 3.9051)
    
    def test_conjugate1(self): # 4+3i = 4-3i
        resultado = lc.conjugadoC([4,3])
        self.assertAlmostEqual(resultado[0], 4)
        self.assertAlmostEqual(resultado[1], -3)

    def test_conjugate2(self): # -2-5i = -2+5i
        resultado = lc.conjugadoC([-2,-5])
        self.assertAlmostEqual(resultado[0], -2)
        self.assertAlmostEqual(resultado[1], 5)
    
    def test_to_cartesian(self): # ρ=3 ^ θ=(π/3)rad => 1.5+2.5981i
        resultado = lc.CVR([3,(math.pi/3)], "cartesiano")
        self.assertAlmostEqual(resultado[0], 1.5)
        self.assertAlmostEqual(resultado[1], 2.5981)

    def test_to_polar(self): # -1+3i => ρ=3.1623 ^ θ=-1.2490rad
        resultado = lc.CVR([-1,3], "polar")
        self.assertAlmostEqual(resultado[0], 3.1623)
        self.assertAlmostEqual(resultado[1], -1.2490)
    
    def test_phase1(self): # 3+5i => θ=1.0304rad
        resultado = lc.fase([3,5])
        self.assertAlmostEqual(resultado, 1.0304)

    def test_phase2(self): # (-1/2)+(√3/2)i => θ=-1.0472rad
        resultado = lc.fase([(-1/2),((math.sqrt(3))/2)])
        self.assertAlmostEqual(resultado, -1.0472)

if __name__ == "__main__":
    unittest.main()
