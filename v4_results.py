import csv


def final_results():
    candidates_info = open("candidates.csv", "r", newline="")
    read_candidatesinfo = csv.reader(candidates_info)
    for i in read_candidatesinfo:
        print(i)
    candidates_info.close()
    f=open("result.csv","r",newline="")
    rd=csv.reader(f)
    for i in rd:
        print(i)

    input("PRESS ENTER TO CLOSE")
    f.close()


final_results()