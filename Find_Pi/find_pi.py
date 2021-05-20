#read the "README.mp" file to find out what I will be doing 

#importing the random dictionary
import random

#create a function that takes in the number of points the function will use
def estimate(num_points):
    #points that are in the circle
    in_circle = 0
    #points that are in the circle
    out_circle = 0

    for i in range(num_points):
        #crete points, x and y
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        #find the distance from the origin to the point
        #and check if it is in the radius of 1
        if x**2 + y**2 <= 1:
            #if the point is under the 1 unit radius, then I check that the point is in fact, in the circle
            in_circle += 1
        
        #else, it is out of the circle
        out_circle += 1

    #I find the ratio between the area of the circle and the area of a square with radius 2r
    #I then set that ration equal to another ration between the number of points in the circle and total points
    # the equation looks like, 2ℼ^2 / (2r)^2 = points_in_cirlce / total_num_points
    #I solve for ℼ and get the formula, 4 * points_in_cirlce / total_num_points
    #I then return that value
    return 4 * in_circle / out_circle

#get an input number from user
num = int(input())

#use that input as the number of points used by the function, estimate()
print("pi estimate (using " + str(num) + " points): " + str(estimate(num)))

