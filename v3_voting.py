import csv


def main():
    no_of_voters = int(input("No. of voters: "))
    vote_count = {}
    for i in range(no_of_voters):
        print("\n\n\n\nVoter no. ",i+1)
        print("\nVoting for Head Boy and Head Girl:")
        vote_for_hbandhg(vote_count)
        print("\nVoting for Deputy School Captain:")
        vote_for_dsc(vote_count)
        print("\nVoting for CCA captain (boy) and CCA captain(girl):")
        vote_for_ccbandccg(vote_count)
        print("\nVoting for Sports captain (boy) and Sports captain(girl):")
        vote_for_scbandscg(vote_count)

        input("\nThank you for voting!!!\nPress Enter for new vote\n\n")
        
    print("VOTING OF THIS BATCH IS SUCCESFULLY COMPLETED")
    n=3

    for i in range(3):
        n = n - 1
        password = input("ENTER PASSWORD (by the election coordinator)")
        if password == "9876543210":#password to be changed as suitable
            print("\nFinal vote count:")
            for candidate, count in vote_count.items():
                result = open("result.csv", "a")
                res = csv.writer(result)
                a=[f"Candidate with SR.no. {candidate} received {count} votes."]
                res.writerow(a)
                result.close()
                print(f"Candidate with SR.no. {candidate} received {count} votes.")
        else:
                print("incorrect password",n,"attempts remaining")



def vote_for_hbandhg(vote_count):
    vote_for_post("Head Boy", "hb.csv", vote_count)
    vote_for_post("Head Girl", "hg.csv", vote_count)


def vote_for_dsc(vote_count):
    vote_for_post("Deputy School Captain", "dsc.csv", vote_count)


def vote_for_scbandscg(vote_count):
    vote_for_post("School sports captain Boy", "spob.csv", vote_count)
    vote_for_post("school sports captain Girl", "spog.csv", vote_count)

def vote_for_ccbandccg(vote_count):
    vote_for_post("School CCA captain Boy", "ccab.csv", vote_count)
    vote_for_post("school CCA captain Girl", "ccag.csv", vote_count)




def vote_for_post(post_name, filename, vote_count):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        candidates = []
        for record in reader:
            print(record)
            candidates.append(record[0])


        vote = input(
            f"['0','None Of The Above (NOTA)']\nWhom do you choose as {post_name} from above (choose from the number given before their name)\nInput no. here: ")
        nota=0
        if vote in candidates:
            vote_count[vote] = vote_count.get(vote, 0) + 1
            print(f"You voted for {post_name} candidate with number {vote}\n\n\n\n")
        elif vote=='0':
            nota=nota+1
            print(f"You voted for {post_name} as NOTA\n\n\n\n")
            return(nota)

        else:
            print("Invalid vote. No candidate with that number.\n\n\n\n")


if __name__ == "__main__":
    main()
