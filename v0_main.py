import csv
import sys
import subprocess
print("------------------------------------WELCOME TO SCHOOL COUNCIL ELECTIONS------------------------------------")
print("----------------powered by PYTHON BASED VOTING SYSTEM FOR SCHOOL COUNCIL ELECTIONS (PVSSCE)----------------\n----------------------------------------------------------------------------brought to you by:-NIPUN TAMORE")
while True:
    choice_1=input("\n# FOR READING THE PROCEDURES OF PVSSCE,--------> enter:100\n# FOR VIEWING LIST OF CANDIDATES,--------------> enter:101\n# FOR VIEWING RESULTS(only after voting),------> enter:102\n# FOR QUITING FROM OUTPUT,---------------------> enter:x\nEnter here-")
    if choice_1=="100":
        print("\n\n\nSTEP-1:RUN THE FILE NAMED 'v1_candidates.py'\n-->ENTER THE DETAILS OF CANDIDATES AS ASKED","\nSTEP-2:RUN THE PYTHON FILE NAMED 'v2_segregation_of posts.py'\n-->THIS WILL SEGREGATE THE CANDIDATES ACCORDING TO THEIR POST","\n""STEP-3: RUN THE PYTHON FILE NAMED 'v3_voting'\n-->HERE THE VOTERS ARE ABLE TO CASTE THEIR VOTES","\nSTEP-4: RUN THE PYTHON FILE NAMED 'v4_results.py'\n-->THE RESULTS ARE HERE!!\n\n")
    if choice_1=="101":
        candidates_info = open("candidates.csv", "r", newline="")
        read_candidatesinfo = csv.reader(candidates_info)
        for i in read_candidatesinfo:
            print(i)
    if choice_1=="102":
        def run_result_file(v4_results):
            subprocess.call(['python',v4_results])
        if __name__=='__main__':
            run_result_file('v4_results.py')



    if choice_1=="x":
        sys.exit()

#candidate activities

#election authorities
