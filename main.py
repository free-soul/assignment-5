import matplotlib.pyplot as plt
import numpy

__dir = './GasPrices.txt'
__encoding = 'UTF-8'
components = open(__dir, 'r', encoding=__encoding).read().split('\n')
now_year = int(components[0].split('-')[2].split(':')[0])

x = []
y = []

def meanNumber(year):

    __database = []
    for data in components:
        if not len(data) <= 0:
            if (int(data.split('-')[2].split(':')[0]) == year):
                __database.append(float(data.split(':')[1]))

    if len(__database) <= 0:
        return None
    return numpy.mean(__database)

while True:

    means = meanNumber(now_year)
    if not means == None:
        x.append(now_year)
        y.append(means)
        now_year += 1
    else:
        break

plt.plot(x, y)
plt.xticks(numpy.arange(min(x), max(x)+1, 1.0))
plt.title('Average gas price per year in US')
plt.xlabel('year')
plt.ylabel('Avg. gas price per gallon [$]')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
