data = open('inputs/1_1.txt', 'r').read().splitlines()
safeReports = 0

def containsDuplicates(report):
    s = set(report)
    if len(s) == len(report):
        return False
    return True

def findDuplicate(report):
    s= set(report)
    dups = abs(len(s) - len(report))
    if dups > 1:
        return False
    #dups is just one
    for i in range(len(report)):
        for j in range(i+1,len(report)):
            if report[i] == report[j]:
                return [i,j]


def remOneOrOther(d_indices, r):
    copy_report = r.copy()
    copy_report.pop(d_indices[0])
    r.pop(d_indices[1])
    return copy_report,r

def extract(reportString):
    levels = reportString.split(' ')
    report = []
    for level in levels:
        report.append(int(level))
    return report
def sortErrors(r_sort):
    p1 = 1
    errors = {}
    while p1 < len(r_sort):
        if r_sort[p1 - 1] < r_sort[p1]:
            if r_sort[p1] < r_sort[p1 + 1]:
                p1 += 1
            else:
                return p1+1

        if r_sort[p1 - 1] > r_sort[p1]:
            if r_sort[p1] > r_sort[p1 + 1]:
                p1 += 1
            else:
                return p1+1

def CheckReport(report):
    decrL = sorted(report, reverse=True)
    incrL = sorted(report)
    p1 = 0
    p2 = 1
    if len(report) == len(set(report)):
        if report != decrL and report != incrL:
                return "sort"
        while p2 < len(report)-1:
             diff = abs(report[p1] - report[p2])
             if diff > 3 or diff < 1 :
                 return [p1,p2]
             p1+=1
             p2+=1

        return True
    return "dups"

for report in data:
    extracted_report = extract(report)
    if containsDuplicates(extracted_report):
        if findDuplicate(extracted_report) != False:
            dups = findDuplicate(extracted_report)


            v= remOneOrOther(dups, extracted_report)
            if CheckReport(v[0]) == True or CheckReport(v[1]) == True:
                safeReports += 1

    elif CheckReport(extracted_report) == "sort":
        s = sortErrors(extracted_report)
        cpy = extracted_report.copy()
        cpy2 = extracted_report.copy()
        cpy3 = extracted_report.copy()
        cpy.pop(s)
        cpy2.pop(s-1)
        cpy3.pop(s-2)

        if CheckReport(cpy) == True or CheckReport(cpy2) == True or CheckReport(cpy3) == True:
            print(CheckReport(cpy), CheckReport(cpy2), CheckReport(cpy3))
            safeReports += 1
    else:
        d = CheckReport(extracted_report)
        print("d",d)

        if d != True:
            v = remOneOrOther(d, extracted_report)
            print("v",v)
            if CheckReport(v[0]) == True or CheckReport(v[1]) == True:
                safeReports += 1
        else:
            if CheckReport(extracted_report) == True:
                safeReports += 1


print("SAfe reports", safeReports)

