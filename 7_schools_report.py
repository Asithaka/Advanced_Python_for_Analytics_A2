"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000

"""

import json

infile = open('school_data.json','r')

schools = json.load(infile)

conference_school = [372,108,107,130]

# Report 1 - Grad rate for women
for school in schools:

    graduation_rate = school['Graduation rate  women (DRVGR2020)'] 
    
    conference_number = school['NCAA']['NAIA conference number football (IC2020)']

    if graduation_rate is not None:

        if  graduation_rate > 50 and conference_number in conference_school:

            print(f"University: {school['instnm']}")
            print(f"Graduation Rate for Women: {school['Graduation rate  women (DRVGR2020)']}%")
            print()
            print()

# Report 2- off campus cost

for school in schools:

    total_price = school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] 
    
    conference_number = school['NCAA']['NAIA conference number football (IC2020)']

    if total_price is not None:

        if  total_price > 50000 and conference_number in conference_school:

            print(f"University: {school['instnm']}")
            print(f"Total price for in-state students living off campus: ${total_price:,.2f}")
            print()
            print()
