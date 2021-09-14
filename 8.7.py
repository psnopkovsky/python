class ComplexNumber:
    result_sum = 0
    result_mul = 1

    def __init__(self, num_1, num_2):
        self.number = complex(num_1, num_2)

    def __add__(self, other):
        ComplexNumber.result_sum += self.number + other.number
        return ComplexNumber(0, 0)

    def __str__(self):
        result_sum = ComplexNumber.result_sum
        result_mul = ComplexNumber.result_mul
        ComplexNumber.result_sum = 0
        ComplexNumber.result_mul = 1
        if result_mul == 1:
            return f'{result_sum}'
        else:
            return f'{result_mul}'

    def __mul__(self, other):
        ComplexNumber.result_mul *= self.number * other.number
        return ComplexNumber(1, 0)


first_complex = ComplexNumber(3, 17)
second_complex = ComplexNumber(5, -8)
third_complex = ComplexNumber(-7, -8)

print(first_complex.number)
print(second_complex.number)
print(third_complex.number)
print('Сумма: ', first_complex + second_complex + third_complex)
print('Произведение: ', first_complex * second_complex * third_complex)