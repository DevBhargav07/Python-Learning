
def towers_of_hanoi(n, src, dest, aux):
    if n <= 1:
        print(f"Move disk 1 from {src} to {dest}")
        return 
    towers_of_hanoi(n-1, src, aux, dest)
    print(f"Move disk {n} from {src} to {dest}")
    towers_of_hanoi(n-1, aux, dest, src)


towers_of_hanoi(3, 'A','B', 'C')
