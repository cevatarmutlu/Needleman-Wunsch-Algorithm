import Fasta
import Needleman
line_list = Fasta.MyFasta('deneme').get_list()

match = 3.621354295
mis_match = -2.451795405
gap = -1.832482334
scores = []
# num_lines = len(line_list)
num_lines = 10

for i in range(num_lines):
    for j in range(i + 1, num_lines):
        dna1 = line_list[i]
        dna2 = line_list[j]
        score = Needleman.calculate(dna1, dna2, gap, match, mis_match)

        scores.append(['s' + str(i), 's' + str(j), str(score)])

# 223.91927892400074
for sc in scores:
    for item in sc:
        print('%s' % item, end=" ")
    print()
