#---------.|.---------
#------.|..|..|.------
#---.|..|..|..|..|.---
#-------WELCOME-------
#---.|..|..|..|..|.---
#------.|..|..|.------
#---------.|.---------

def designer_pattern(n,m):
    for i in range(1,n,2):
        pattern=(".|."*i).center(m,"-")
        print(pattern)
    print("WELCOME".center(m,'-'))
    
    for i in range(n-2,0,-2):
        pattern=(".|."*i).center(m,"-")
        print(pattern)
        
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    designer_pattern(n,m)