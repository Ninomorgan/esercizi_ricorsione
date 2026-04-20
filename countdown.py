from time import sleep




#metodo normale
def countdown(n):
    while n>=0:
        print(n)
        sleep(1)
        n-=1
    pass

#metodo ricorsione

def countdown_ricorsione(n):
    #condizione terminale
    if n==0:
        print("Auguri")


    #condizione non terminale
    else:
        print(n)
        sleep(1)
        countdown_ricorsione(n-1)
if __name__ == '__main__':
    n=10
    countdown_ricorsione(n)