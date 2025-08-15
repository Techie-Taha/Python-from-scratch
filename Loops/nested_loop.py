numbers = [5, 2, 5, 2, 2]
for x_count in numbers: 
    output =""
    for count in range(x_count): #nested loop is just adding one loop insdie of another loop
        output += 'x'
    print(output) #in the terminal we should see a F shape x
