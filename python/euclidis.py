import sys

def euclidis_algoritm(m:int, n:int) -> int:
  return n if (m % n == 0) else euclidis_algoritm(n, m % n)

def main(m:int, n:int):
  print(euclidis_algoritm(m, n))

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python3 euclidis.py <m> <n>")
    sys.exit(1)
  m = int(sys.argv[1])
  n = int(sys.argv[2])
  main(m, n)