import Fasta
import Needleman
import time
import MyThread

'''
    Çalışma mantığı şöyle: fasta dosyasından satırları alıp hepsini bir diziyi atıyorum.
    Sonra num_lines kadar satırı birbiri ile karşılaştırıyorum
    
    Thread olayına gelirsek:
        Bu örnekte ilk satırı (num_lines - 1) tane satırla karşılaştırıp score değeri elde ediyor.
        İşte buradan başka thread açabileceğim başka yer bulamadım. 
        Bende (num_lines - 1) değerini bölerek threadlere vermeye karar verdim. Sıkıntı daha yavaş çalışıyor.
        200'den fazla denemedim. 200 satırda tekil olarak 515 saniyede çalıştırırken threadli 912 sanitede çalıştırıyor.
'''


def isim_bulamadim(first: int, last: int):
    # bu fonk. isim bulursanız değiştirin.
    for j in range(first, last):
        dna2 = line_list[j]
        score = Needleman.calculate(dna1, dna2, gap, match, mis_match)
        scores.append(['s' + str(i), 's' + str(j), str(score)])


line_list = Fasta.MyFasta('deneme').get_list()

match = 3.621354295
mis_match = -2.451795405
gap = -1.832482334
scores = []
# num_lines = len(line_list)
num_lines = 50
start_time = time.time()
print('Başlangıç zamanı %f' % start_time)
for i in range(num_lines):
    dna1 = line_list[i]
    karsilastirilacak_satir_sayisi = num_lines - (i + 1)
    pt1 = int(karsilastirilacak_satir_sayisi / 2)
    # isim_bulamadim(i + 1, num_lines)

    thread1 = MyThread.MyThread(isim_bulamadim, i + 1, pt1)
    thread2 = MyThread.MyThread(isim_bulamadim, pt1, num_lines)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

end_time = time.time()
print('Bitiş zamanı %f' % end_time)
print('Tamamlanma süresi %f' % (end_time - start_time))
'''
for sc in scores:
    for item in sc:
        print('%s' % item, end=" ")
    print()
'''
