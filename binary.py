import numpy as np
input = 'inputs/day3_input.txt'


def power(input_file):
   binaries = []

   with open(input_file) as file:
      for line in file:
         binary = []
         for digit in line[:-1]:
            binary.append(int(digit))
         binaries.append(binary)

   np_binaries = np.array(binaries)
   output_bin = []
   binary_length = np_binaries.shape[1]
   for i in range(binary_length):
      dig_sum = np_binaries[:, i].sum()
      if dig_sum > np_binaries.shape[0] / 2:
         output_bin.append(1)
      else:
         output_bin.append(0)

   return output_bin

def binary_array_to_decimal(binary_array):
   string = ''
   for digit in binary_array:
      string = string + str(digit)
   decimal = int(string, 2)
   return decimal

def binary_flip(binary_array):
   flipped_array = []
   for digit in binary_array:
      if digit:
         flipped_array.append(0)
      else:
         flipped_array.append(1)
   return flipped_array


gamma = power(input)
decimal_gamma = binary_array_to_decimal(gamma)

epsilon = binary_flip(gamma)
decimal_epsilon = binary_array_to_decimal(epsilon)

print("gamma = {}, epsilon = {}, power = {}".format(decimal_gamma, decimal_epsilon, decimal_gamma * decimal_epsilon))

