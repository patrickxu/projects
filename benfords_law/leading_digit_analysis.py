import collections
import matplotlib.pyplot as plt

def leading_digit_recent(file):
    f = open(file)
    f.readline()
    f.readline()
    f.readline()
    leading_list = []
    for line in f:
        line_data = line.strip(',\r\n').split(",")
        name = line_data[0]
        recent_pop = line_data[-1].strip('"')
        if len(recent_pop) > 0:
            lead = int(recent_pop[0])
            leading_list.append(lead)
    print(len(leading_list))
    n, bins, patches = plt.hist(leading_list, 9, normed=1, facecolor='green', alpha=0.75)
    plt.xlabel('Leading Digit')
    plt.ylabel('Probability')
    plt.show()
    f.close()

#correct NYA 2013 salary: 231978886
def leading_digit_total(file):
    f = open(file)
    f.readline()
    f.readline()
    f.readline()
    leading_list = []
    for line in f:
        line_data = line.strip(',\r\n').split(",")
        name = line_data[0]
        for i in range(4, len(line_data)):
            pop = line_data[i].strip('"')
            if len(pop) > 0 and pop.isdigit():
                lead = int(pop[0])
                leading_list.append(lead)
    print(len(leading_list))
    n, bins, patches = plt.hist(leading_list, 9, normed=1, facecolor='green', alpha=0.75)
    plt.xlabel('Leading Digit')
    plt.ylabel('Probability')
    plt.title(r"Exploring Benford's Law Through Country Populations")
    plt.axis([1, 9, 0, 0.4])
    plt.show()
    f.close()
    
leading_digit_total(r'/Users/patrickxu/Desktop/global_pop_data.csv')