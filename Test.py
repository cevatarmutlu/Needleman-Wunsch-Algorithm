import Fasta
import Needleman
import MyThread


def create_thread(arr: list):
    arr.clear()
    arr.append(MyThread.MyThread(needleman.gap_list_create))
    arr.append(MyThread.MyThread(needleman.l_val_list_create))
    arr.append(MyThread.MyThread(needleman.u_val_list_create))
    return arr


match = 3.621354295
mis_match = -2.451795405
gap = -1.832482334

scores = []
fasta = Fasta.MyFasta('deneme')
line_list = fasta.get_list()

# num_lines = len(line_list)
num_lines = 9
needleman = Needleman.Needleman(match, mis_match, gap)
threads = []

for i in range(num_lines):
    for j in range(i + 1, num_lines):
        dna1 = line_list[i]
        dna2 = line_list[j]
        needleman.set_dna(dna1, dna2)
        threads = create_thread(threads)
        for ths in threads:
            ths.start()
        for thj in threads:
            thj.join()
        needleman.calculate()
        scores.append(needleman.get_score())

# -147572.93959690002
print(scores)



