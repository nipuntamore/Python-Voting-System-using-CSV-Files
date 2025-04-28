import csv
candidates_info=open("candidates.csv","r",newline="")
count_hb=0
read_candidatesinfo=csv.reader(candidates_info)
def segregation_of_applicants():
    for j in read_candidatesinfo:
        for i in read_candidatesinfo:
           if i[4]=="HEAD BOY" :
               hb=open("hb.csv","a",newline="")
               hbwrite=csv.writer(hb)
               hbwrite.writerow(i)
               hb.close()

           elif i[4]=="HEAD GIRL":
               hg=open("hg.csv","a",newline="")
               hgwrite=csv.writer(hg)
               hgwrite.writerow(i)
               hg.close()

           elif i[4]=="DEPUTY SCHOOL CAPTAIN":
               dsc=open("dsc.csv","a",newline="")
               dscwrite=csv.writer(dsc)
               dscwrite.writerow(i)
               dsc.close()

           elif i[4]=="CCA CAPTAIN (BOY)":
               ccab=open("ccab.csv", "a", newline="")
               ccabwrite=csv.writer(ccab)
               ccabwrite.writerow(i)
               ccab.close()

           elif i[4]=="CCA CAPTAIN (GIRL)":
               ccag=open("ccag.csv", "a", newline="")
               ccagwrite=csv.writer(ccag)
               ccagwrite.writerow(i)
               ccag.close()

           elif i[4]=="SPORTS CAPTAIN (BOY)" :
               spob=open("spob.csv", "a", newline="")
               spobwrite = csv.writer(spob)
               spobwrite.writerow(i)
               spob.close()

           elif i[4]=="SPORTS CAPTAIN (GIRL)":
               spog=open("spog.csv", "a", newline="")
               spogwrite = csv.writer(spog)
               spogwrite.writerow(i)
               spog.close()
           else:
               print("record not found")





segregation_of_applicants()