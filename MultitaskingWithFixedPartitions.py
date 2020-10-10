
def firstfit(partitions,processes):
    result = [-1]*len(partitions)
    internalfrag = [-1]*len(partitions)
    
    for i in range(0,len(processes)):
        for j in range(0,len(partitions)):
            if processes[i] <= partitions[j] and result[j] == -1:
                result[j] = i+1
                internalfrag[j] = partitions[j] - processes[i]
                break
    fitname = "First fit"
    output(partitions,processes,result,internalfrag,fitname)
    

def bestfit(partitions,processes):
    result = [-1]*len(partitions)
    internalfrag = [-1]*len(partitions)

    for i in range(0,len(processes)):
        mini = sum(partitions)
        minindex = -1
        flagbit = False
        for j in range(0,len(partitions)):
            if processes[i] <= partitions[j] and result[j] == -1 and partitions[j]-processes[i]<=mini:
                minindex = j
                mini = partitions[j] - processes[i]
                flagbit = True
        if flagbit and minindex!=1:
            result[minindex] = i+1
            internalfrag[minindex] = mini
    fitname = "Best Fit"
    output(partitions,processes,result,internalfrag,fitname)


def worstfit(partitions,processes):
    result = [-1]*len(partitions)
    internalfrag = [-1]*len(partitions)

    for i in range(0,len(processes)):
        maxi = -1
        maxindex = -1
        flagbit = False
        for j in range(0,len(partitions)):
            if processes[i] <= partitions[j] and result[j] == -1 and partitions[j]-processes[i]>=maxi:
                print("i am process",i+1)
                print("in the partition",j+1)
                maxindex = j
                maxi = partitions[j] - processes[i]
                print(maxindex,maxi)
                flagbit = True
        if maxindex != -1 and flagbit:
            result[maxindex] = i+1
            internalfrag[maxindex] = maxi
        else:
            continue        
    fitname = "Worst Fit"
    output(partitions,processes,result,internalfrag,fitname)


def output(partitions,processes,result,internalfrag,fitname):
    print("\n")
    print("------------"+fitname+"------------")
    print("Partitions: ".ljust(23),partitions)
    print("Processes: ".ljust(23),processes)
    print("Allocation: ".ljust(23),result)
    print("Internal Fragmentation:".ljust(23),internalfrag)
    #unallocated processes
    print("--------Unallocated processes--------")
    isunalloc = False
    for i in range(len(processes)):
        if i+1 not in result:
            isunalloc = True
            print("Process "+str(i+1)+" cannot be allocated")
    if isunalloc == False:
        print("All processes have been allocated successfully")
    print("\n")
    
    



#execution begins here.
phymem = int(input("Enter the size of physical memory : "))

partitions = []
no_partitions = int(input("Enter number of partitions : "))
for i in range(0,no_partitions):
    partitions.append(int(input("Enter partition"+str(i+1)+" size: ")))

if sum(partitions) == phymem:
    processes = []
    no_processes = int(input("Enter number of processes incoming :"))
    for j in range(0,no_processes):
        processes.append(int(input("Enter process"+str(j+1)+" size: ")))
    #input has been taken
    firstfit(partitions,processes)
    bestfit(partitions,processes)
    worstfit(partitions,processes)
