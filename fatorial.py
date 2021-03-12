def fatorial(n):
   if n == 0 or n == 1:
        return 1 
   else:
        return n * fatorial(n - 1) 


if __name__ == "__main__":
    print(f'10! = {fatorial(10)}')
