phymem = int(input("Enter the size of Physical memory: "))
Again = True
process_number = 0
processes = {}
unallocated = {}
cumulativesum = 0
while Again:
    Again = False
    process_number+=1
    process_name = input("\nEnter the name of the process: ")
    process_size = int(input("Enter the size of the process: "))
    if cumulativesum + process_size <=phymem:
        cumulativesum += process_size
        processes[process_name] = [process_number,process_size]
        confirm = input("Is there process incoming?[Y/N]")
        if confirm.upper() == 'Y':
            Again = True
    else:
        unallocated[process_name] = [process_number,process_size]
        confirm = input("Current process didn't fit in the memory!! Is there any process still incoming?[Y/N]")
        if confirm.upper() == 'Y':
            Again = True  


    
print("\nProcessName\tPartitionNumber\tProcessSize")
print("---------------|----------------|------------")
for k,v in processes.items():
    print(k.ljust(15)+str(v[0]).center(16)+str(v[1]).center(11))

print("\nExternal Fragmentation =",phymem-cumulativesum)

print("\n--------Unallocated processes--------")
print("ProcessName\tProcessSize")
for k,v in unallocated.items():
    print(k.ljust(15)+str(v[1]).center(11))



