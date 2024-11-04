maxx=0
def find_max(*args):
    for arg in args:
        if(arg>maxx):
            maxx=arg
            
 max_nam=find_max(3,2,5,8,6,9)
 print(max_nam)
