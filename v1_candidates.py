import csv
n=0
noofcandidates=int(input("enter no. of candidates:"))
candidate_file1=open("candidates.csv","w",newline="")
candidate_writer=csv.writer(candidate_file1)
OPTIONSCHOSEN=[]
candidate_writer.writerow(['VOTING CANDIDATE no.','CANDIDATE NAME','CLASS AND SEC OF CANDIDATE','HOUSE OF CANDIDATE','POST APPLIED'])
def candidates_info():
    for i in range(noofcandidates):
        name=input("ENTER NAME OF CANDIDATE:")
        classsec=input("ENTER CLASS AND SEC OF CANDIDATE:")
        house=input("ENTER HOUSE OF CANDIDATE:")
        post=int(input("CHOOSE THE POST FOR APPLICATION WITH THE USE OF NUMBERS INDICATED:-\n"                             
                       "(1) for HEAD BOY\n"                                                                                
                       "(2) for HEAD GIRL\n"                                                                               
                       "(3) for DEPUTY SCHOOL CAPTAIN\n"                                                                   
                       "(4) for CCA CAPTAIN (BOY)\n"                                                                       
                       "(5) for CCA CAPTAIN (GIRL)\n"                                                                      
                       "(6) for SPORTS CAPTAIN (BOY)\n"                                                                    
                       "(7) for SPORTS CAPTAIN (GIRL)\n"))
        if post==1:
            pa="HEAD BOY"
        elif post == 2:
            pa="HEAD GIRL"
        elif post == 3:
            pa="DEPUTY SCHOOL CAPTAIN"
        elif post == 4:
            pa="CCA CAPTAIN (BOY)"
        elif post == 5:
            pa="CCA CAPTAIN (GIRL)"
        elif post == 6:
            pa="SPORTS CAPTAIN (BOY)"
        elif post == 7:
            pa="SPORTS CAPTAIN (GIRL)"
        else:
            pa="not found"
        n=i+1
        OPTIONSCHOSEN=[n,name,classsec,house,pa]
        candidate_writer.writerow(OPTIONSCHOSEN)
        input("press enter for new entry")
    candidate_file1.close()

candidates_info()


