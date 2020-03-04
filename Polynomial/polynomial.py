from functools import reduce


class Polynomial:
    def __init__(self, obj):
        if isinstance(obj, (list, tuple)) and len(obj) == 0:
            raise AttributeError()
        if isinstance(obj, list):
            self.coeffs = obj
        elif isinstance(obj, tuple):
            self.coeffs = list(obj)
        elif isinstance(obj, Polynomial):
            self.coeffs = obj.coeffs.copy()
        else:
            raise TypeError()

    def __eq__(self, o):
        if isinstance(o, Polynomial):
            return self.coeffs == o.coeffs
        else:
            raise TypeError

    def __add__(self, o):
        return self.__add(o)

    def __radd__(self, o):
        return self.__add(o)

    def __sub__(self, o):
        return self.__add(-o)

    def __rsub__(self, o):
        return (-self).__add(o)

    def __neg__(self):
        self.coeffs = [-i for i in self.coeffs]
        return self

    def __mul__(self, o):
        return self.__mul(o)

    def __rmul__(self, o):
        return self.__mul(o)

    def __mul(self, o):
        if isinstance(o, int):
            return Polynomial([x * o for x in self.coeffs])
        elif isinstance(o, Polynomial):
            _len = len(self.coeffs)
            return reduce(lambda x, y: x + y,
                          map(
                              lambda i: Polynomial((o * self.coeffs[i]).coeffs + [0 for j in range(_len-i-1)]),
                              range(_len)
                          ))
        else:
            raise TypeError

    def __repr__(self):
        return "Polynomial(" + str(self.coeffs) + ")"

    def __str__(self):
        if len(self.coeffs) == 1:
            return str(self.coeffs[0])

        str_format = []

        def to_str(x, zero_index=False):
            if x > 1:
                return "+" + str(x)
            elif x == 1:
                if zero_index:
                    return "+1"
                else:
                    return ""
            elif x == -1:
                return "-"
            else:
                return str(x)

        args = self.coeffs[-1::-1]
        for i in range(len(self.coeffs), 0, -1):
            i = i - 1
            if args[i] != 0:
                if i == 0:
                    str_part = to_str(args[i], zero_index=True)
                else:
                    str_part = to_str(args[i])
                    if i == 1:
                        str_part = str_part + "x"
                    else:
                        str_part = str_part + "x^" + str(i)

                str_format.append(str_part)

        result = "".join(str_format)
        if len(result) != 0 and result[0] == "+":
            result = result[1:]
        return result

    def __add(self, o):
        if isinstance(o, int):
            self.coeffs[-1] = self.coeffs[-1] + o
        elif isinstance(o, Polynomial):
            (min_len, short, long) = (len(self.coeffs), self.coeffs, o.coeffs) \
                if len(self.coeffs) < len(o.coeffs) \
                else (len(o.coeffs), o.coeffs, self.coeffs)
            for i in range(min_len):
                long[-i - 1] = long[-i - 1] + short[-i - 1]
            self.coeffs = long
        else:
            raise TypeError()
        return self
