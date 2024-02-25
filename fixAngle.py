def FixAng(angle):
    a = angle
    if(angle>359):
        a -= 360
    elif(angle<0):
        a += 360
    return a

def FixAng2(angle):
    return angle%360

if __name__ == "__main__":
    print(FixAng(361))
    print(FixAng(-1))
    print(FixAng2(361))
    print(FixAng2(-1))
