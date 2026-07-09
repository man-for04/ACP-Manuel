import json

from VH_Impl import VH_Impl
from VH_Skeleton import VH_Skeleton

if __name__ == "__main__":
    
    with open('status.txt', 'a') as channel:
        
        delegato = VH_Impl(channel)
        skeleton = VH_Skeleton(delegato)
        skeleton.run_skeleton()