import sys
import shutil
import os
import datetime

count = 0
n = 0
conv = 0.5 # this value will vary for different test cases in the backend
epoch = sys.argv[1]

def rewrite_pagerank():
    os.remove("/home/pes1ug19cs592/A2/v.txt")
    source = "/home/pes1ug19cs592/A2/v1.txt"
    destination = "/home/pes1ug19cs592/A2/v.txt"
    dest = shutil.copyfile(source, destination)


with open("/home/pes1ug19cs592/A2/v.txt") as file1, open("/home/pes1ug19cs592/A2/v1.txt") as file2, open("/home/pes1ug19cs592/A2/log", "a") as logging:
    for line1, line2 in zip(file1, file2):
        count += 1
        old_pagerank = float(line1.split(",")[1])
        new_pagerank = float(line2.split(",")[1])

        if abs(old_pagerank - new_pagerank) < conv:
            n += 1
	
    if epoch == '1':
        t = str(datetime.datetime.now())
        logging.write(f"BEGINNING CONVERGENCE AT {t}\n")
    logging.write(f"Iteration: {epoch} - {n}/{count}\n")

    if n == count:
        t = str(datetime.datetime.now())
        logging.write(f"CONVERGENCE REACHED AT {t}\n")
        print(0)
    else:
        rewrite_pagerank()
        print(1)
