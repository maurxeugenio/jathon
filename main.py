from java.lang import System, Math, String, Arrays
from java.util import Random, Collections, Date, Scanner


System.out.println("Bem-vindo ao Jathon!")

System.out.println("Math Test: " + str(Math.pow(2, 8)))
System.out.println("String Test:")
nome = String("Maurício")
System.out.println("Upper: " + nome.toUpperCase())

System.out.println("Array Test:")
arr = [3, 1, 4, 2]
Arrays.sort(arr)
System.out.println("Sorted: " + Arrays.toString(arr))

System.out.println("Random Examples:")
rand = Random()
System.out.println("nextInt(10): " + str(rand.nextInt(10)))
System.out.println("nextFloat(): " + str(rand.nextFloat()))
System.out.println("nextBoolean(): " + str(rand.nextBoolean()))

System.out.println("\nDate Example:")
d = Date()
System.out.println("Now: " + d.toString())

System.out.println("\nCollections Example:")
nums = [4, 1, 3, 2]
Collections.sort(nums)
System.out.println("Sorted: " + str(nums))
Collections.reverse(nums)
System.out.println("Reversed: " + str(nums))

# Simular entrada
System.out.println("\nScanner Example (simulado)")
fake_input = iter(["Maurício", "42"]).__next__
scanner = Scanner(source=fake_input)
System.out.println("Name: " + scanner.next())
System.out.println("Age: " + str(scanner.nextInt()))
