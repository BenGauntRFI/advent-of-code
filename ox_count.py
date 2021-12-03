import math

input = 'inputs/day3_input.txt'
test = 'inputs/day3_test.txt'


def get_digit(number_string, n):
   return int(number_string[n])

def get_data(input_file):
   number_strings = []

   with open(input_file) as file:
      for line in file:
         number_strings.append(line[:-1])

   return number_strings


def find_max_dig(binary_array, n, tie=1):
   count_zero = 0
   count_ones = 0
   for binary in binary_array:
      dig = get_digit(binary, n)
      if dig == 1:
         count_ones += 1
      else:
         count_zero += 1
   if count_zero < count_ones:
      return 1
   elif count_zero > count_ones:
      return 0
   else:
      return tie


def oxygen(binary_array):
   digits = len(binary_array[0])

   for i in range(digits):
      bit_crit = find_max_dig(binary_array, i)
      new_array = [binary for binary in binary_array if get_digit(binary, i) == bit_crit]
      if len(new_array) == 1:
         return new_array
      else:
         binary_array = new_array

def carbon(binary_array):
   digits = len(binary_array[0])

   for i in range(digits):
      bit_crit = find_max_dig(binary_array, i)
      new_array = [binary for binary in binary_array if get_digit(binary, i) != bit_crit]
      if len(new_array) == 1:
         return new_array
      else:
         binary_array = new_array



data = get_data(input)

oxy = oxygen(data)
dec_oxy = int(oxy[0], 2)

car = carbon(data)
dec_car = int(car[0], 2)

print(dec_oxy, dec_car, dec_oxy * dec_car)