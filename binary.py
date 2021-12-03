import numpy as np
input = 'inputs/day3_input.txt'
test = 'inputs/day3_test.txt'


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

def oxygen(input_file):
   binaries = []

   with open(input_file) as file:
      for line in file:
         binary = []
         for digit in line[:-1]:
            binary.append(int(digit))
         binaries.append(binary)

   np_binaries = np.array(binaries)
   binary_length = np_binaries.shape[1]
   for i in range(binary_length):
      dig_sum = np_binaries[:, i].sum()
      remove = np.ones(np_binaries.shape[0], dtype=bool)
      if dig_sum > np_binaries.shape[0] / 2:
         for k, dig in enumerate(np_binaries[:, i]):
            if not dig:
               remove[k] = False
      else:
         for k, dig in enumerate(np_binaries[:, i]):
            if dig:
               remove[k] = False

      np_binaries = np.delete(np_binaries, remove, axis=0)

      if np_binaries.shape[0] == 1:
         break

   return np_binaries[0]

def carbon(input_file):
   binaries = []

   with open(input_file) as file:
      for line in file:
         binary = []
         for digit in line[:-1]:
            binary.append(int(digit))
         binaries.append(binary)

   np_binaries = np.array(binaries)
   binary_length = np_binaries.shape[1]
   for i in range(binary_length):
      dig_sum = np_binaries[:, i].sum()
      remove = np.ones(np_binaries.shape[0], dtype=bool)
      if dig_sum < np_binaries.shape[0] / 2:
         for k, dig in enumerate(np_binaries[:, i]):
            if not dig:
               remove[k] = False
      else:
         for k, dig in enumerate(np_binaries[:, i]):
            if dig:
               remove[k] = False



      np_binaries = np.delete(np_binaries, remove, axis=0)
      if np_binaries.shape[0] == 1:
         break

   return np_binaries[0]


ox = oxygen(test)
c = carbon(test)
print(ox)
print(c)

ox_decimal = binary_array_to_decimal(ox)
c_decimal = binary_array_to_decimal(c)

print(ox_decimal)
print(c_decimal)
print(ox_decimal * c_decimal)
