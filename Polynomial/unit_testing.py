import unittest
from Polynomial.polynomial import Polynomial


class PolynomialTest(unittest.TestCase):

    ######                 ######
    ##       __init__()        ##
    ######                 ######

    def test_init_1(self):
        self.assertEqual(
            [-1, 0, 4],
            Polynomial([-1, 0, 4]).coeffs)

    def test_init_2(self):
        p1 = Polynomial([-1, 0, 4])
        p2 = Polynomial(p1)
        p1.coeffs[0] = 1

        self.assertEqual(
            [1, 0, 4],
            p1.coeffs)

        self.assertEqual(
            [-1, 0, 4],
            p2.coeffs)

    def test_init_3(self):
        with self.assertRaises(TypeError):
            Polynomial(-1)

    def test_init_4(self):
        self.assertEqual(
            [-1, 0, 4],
            Polynomial((-1, 0, 4)).coeffs)

    def test_init_5(self):
        with self.assertRaises(AttributeError):
            Polynomial([])

    ######                 ######
    ##        __add__()        ##
    ######                 ######

    def test_add_1(self):
        self.assertEqual(
            Polynomial([-1, 0, 5]),
            Polynomial([-1, 0, 4]) + 1)

    def test_add_2(self):
        self.assertEqual(
            Polynomial([-1, 0, 5]),
            1 + Polynomial([-1, 0, 4]))

    def test_add_3(self):
        with self.assertRaises(TypeError):
            Polynomial([-2]) + {4: "ds"}

    def test_add_4(self):
        self.assertEqual(
            Polynomial([-1, 0, 8]),
            Polynomial([4]) + Polynomial([-1, 0, 4]))

    def test_add_5(self):
        self.assertEqual(
            Polynomial([-1, 4, 7]),
            Polynomial([4, 3]) + Polynomial([-1, 0, 4]))

    def test_add_6(self):
        self.assertEqual(
            Polynomial([3, 3, 6]),
            Polynomial([4, 3, 2]) + Polynomial([-1, 0, 4]))

    def test_add_7(self):
        self.assertEqual(
            Polynomial([3, 3, 6, 2]),
            Polynomial([4, 3, 2, 1]) + Polynomial([-1, 0, 4, 1]))

    ######                 ######
    ##        __sub__()        ##
    ######                 ######

    def test_sub_1(self):
        self.assertEqual(
            Polynomial([-1, 0, 3]),
            Polynomial([-1, 0, 4]) - 1)

    def test_sub_2(self):
        self.assertEqual(
            Polynomial([-1, -2, 5]),
            Polynomial([-1, 0, 4]) - Polynomial([2, -1]))

    def test_sub_3(self):
        self.assertEqual(
            Polynomial([1, 0, -3]),
            1 - Polynomial([-1, 0, 4]))

    def test_sub_4(self):
        with self.assertRaises(TypeError):
            Polynomial([-2]) - {4: "ds"}

    def test_sub_5(self):
        self.assertEqual(
            Polynomial([1, 0, 0]),
            Polynomial([4]) - Polynomial([-1, 0, 4]))

    def test_sub_6(self):
        self.assertEqual(
            Polynomial([1, 4, -1]),
            Polynomial([4, 3]) - Polynomial([-1, 0, 4]))

    def test_sub_7(self):
        self.assertEqual(
            Polynomial([0, 0, 0]),
            Polynomial([4, 3, 2]) - Polynomial([4, 3, 2]))

    def test_sub_8(self):
        self.assertEqual(
            Polynomial([-8, -6, -4]),
            -Polynomial([4, 3, 2]) - Polynomial([4, 3, 2]))

    ######                 ######
    ##        __neg__()        ##
    ######                 ######

    def test_neg_1(self):
        self.assertEqual(
            Polynomial([1, 0, -4]),
            -Polynomial([-1, 0, 4]))

    ######                 ######
    ##       __mul__()        ##
    ######                 ######

    def test_mul_1(self):
        self.assertEqual(
            Polynomial([-2, 0, 8]),
            Polynomial([-1, 0, 4]) * 2)

    def test_mul_2(self):
        self.assertEqual(
            Polynomial([-2, 0, 8]),
            2 * Polynomial([-1, 0, 4]))

    def test_mul_3(self):
        with self.assertRaises(TypeError):
            Polynomial([-2]) * {4: "ds"}

    def test_mul_4(self):
        with self.assertRaises(TypeError):
            2. * Polynomial([-2])

    def test_mul_5(self):
        self.assertEqual(
            Polynomial([12, -15, 21, 0, 0]),
            Polynomial([3, 0, 0]) * Polynomial([4, -5, 7]))

    def test_mul_6(self):
        self.assertEqual(
            Polynomial([8, 2, -39, 30]),
            Polynomial([4, -5]) * Polynomial([2, 3, -6]))

    ######                 ######
    ##    complex operation    ##
    ######                 ######

    def test_complex_1(self):
        self.assertEqual(
            Polynomial([-8, -2, 36, -24]),
            -(Polynomial([4, -5]) * Polynomial([2, 3, -6])) - Polynomial([3, -6]))

    ######                 ######
    ##       __repr__()        ##
    ######                 ######

    def test_repr_1(self):
        self.assertEqual(
            'Polynomial([-1, 0, 4])',
            repr(Polynomial([-1, 0, 4])))

    ######                 ######
    ##        __str__()        ##
    ######                 ######

    def test_str_1(self):
        self.assertEqual(
            'x^2+2x-3',
            str(Polynomial([1, 2, -3])))

    def test_str_2(self):
        self.assertEqual(
            '-x^2+3',
            str(Polynomial([-1, 0, 3])))

    def test_str_3(self):
        self.assertEqual(
            '',
            str(Polynomial([0, 0, 0])))

    def test_str_4(self):
        self.assertEqual(
            'x^2+32x+423',
            str(Polynomial([1, 32, 423])))

    def test_str_5(self):
        self.assertEqual(
            '-3x^4-3x^3-3x^2-3x-3',
            str(Polynomial([-3, -3, -3, -3, -3])))

    def test_str_6(self):
        self.assertEqual(
            '1',
            str(Polynomial([1])))

    def test_str_7(self):
        self.assertEqual(
            '2x+1',
            str(Polynomial([2, 1])))