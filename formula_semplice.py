# Formula semplice per il calcolo della rata mensile
# da https://www.facile.it/mutui/guida/calcolo-rata-mutuo-come-fare.html

C = 90_000  # capitale
TA = 3.0 / 100  # tasso
PA = 12  # mesi per anno
A = 10  # anni

RATA = C*(1+TA/PA)**(PA*A) * TA/PA /((1+TA/PA)**(PA*A)-1)

