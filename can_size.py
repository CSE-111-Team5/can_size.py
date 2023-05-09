import math

def compute_volume(radius,height):
    volume = math.pi*radius**2*height
    return volume

def compute_suface_area(radius,height):
    surface_area =  2*math.pi*radius*(radius + height)
    return surface_area
def main(names,radius,height):
    surface_area=compute_suface_area(radius,height)
    volume = compute_volume(radius,height)
    storage_efficiency = volume/surface_area

    print (f'{names} {storage_efficiency:.2f}')

with open('txt folder//tin_cans.txt') as cansizefile:
    for sizes in cansizefile:
        parts = sizes.strip('\n').split(',')
        names = parts[0]
        radius =float(parts[1])
        height =float(parts [2])
        cost_per_can = float(parts[3].strip('$'))
        
        main(names,radius,height)

#This is the Tin Can Txt file
#Name	Radius(centimeters)	Height(centimeters)	Cost per Can(U.S. dollars)
#1 Picnic	6.83	10.16	$0.28
#1 Tall	7.78	11.91	$0.43
#2	8.73	11.59	$0.45
#2.5	10.32	11.91	$0.61
#3 Cylinder	10.79	17.78	$0.86
#5	13.02	14.29	$0.83
#6Z	5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10	15.72	17.78	$1.53
#211	6.83	12.38	$0.34
#300	7.62	11.27	$0.38
#303	8.10	11.11	$0.42

#This is the output the assinment wanted.
#> python can_sizes.py
#1 Picnic 2.04
#1 Tall 2.35
#2 2.49
#2.5 2.76
#3 Cylinder 3.36
#5 3.41
#6Z 1.68
#8Z short 1.80
#10 4.17
#211 2.20
#300 2.27
#303 2.34