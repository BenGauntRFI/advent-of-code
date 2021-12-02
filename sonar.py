input = 'inputs/day1_input.txt'


def single_depths(input_file):
   depths = []

   with open(input_file) as file:
      for line in file:
         depths.append(int(line))

   increases = 0
   for i in range(len(depths) - 1):
      if depths[i + 1] > depths[i]:
         increases += 1

   return increases

def triple_depths(input_file):
   depths = []

   with open(input_file) as file:
      for line in file:
         depths.append(int(line))

   increases = 0
   for i in range(len(depths) - 3):
      sum_i = depths[i] + depths[i + 1] + depths[i + 2]
      sum_i_plus_one = depths[i + 1] + depths[i + 2] + depths[i + 3]
      if sum_i_plus_one > sum_i:
         increases += 1

   return increases

print(triple_depths(input))