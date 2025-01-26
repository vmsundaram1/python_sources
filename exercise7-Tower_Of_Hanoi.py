# This program solves the Tower of Hanoi for any number of 
# discs.
def tower_of_hanoi(n, source, target, auxiliary):
  """
  Solve the Tower of Hanoi problem and print the steps.
  Parameters:
  n (int): Number of disks
  source (str): The name of the source rod
  target (str): The name of the target rod
  auxiliary (str): The name of the auxiliary rod
  """
  if n == 1:
    print(f"Move disk 1 from {source} to {target}")
    return

  # Move n-1 disks from source to auxiliary, using target as a buffer
  tower_of_hanoi(n - 1, source, auxiliary, target)

  # Move the nth disk from source to target
  print(f"Move disk {n} from {source} to {target}")

  # Move the n-1 disks from auxiliary to target, using source as a buffer
  tower_of_hanoi(n - 1, auxiliary, target, source)



number_of_disks = input("Enter the number of disks for Tower of Hanoi: \n")

source_for_disks = input("Enter the Source for Disk (Any alphabet character): \n")

target_for_disks = input("Enter the Target for Disk (Any alphabet character): \n")

auxiliary_for_disks = input("Enter the Auxiliary for Disk (Any alphabet character): \n")


number1 = int(number_of_disks)

tower_of_hanoi(number1, source_for_disks,target_for_disks,auxiliary_for_disks)