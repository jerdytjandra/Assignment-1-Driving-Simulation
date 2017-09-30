#Assume a ball is in cup A
def CubsNBall():

    cup1 = 1
    cup2 = 0
    cup3 = 0
#A ball is in cup1
    method = input('Method A/B/C:') #3 methods: A, B, and C
    for ball in method:
        if ball == 'A':
            cup1, cup2 = cup2, cup1
        elif ball == 'B':
            cup2, cup3 = cup3, cup2
        elif ball == 'C':
            cup1, cup3 = cup3, cup1

    if cup1 == 1:
        print(1)
    elif cup2 == 1:
        print(2)
    elif cup3 == 1:
        print(3)

CubsNBall()
