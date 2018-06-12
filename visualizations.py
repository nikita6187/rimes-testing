import matplotlib.pyplot as plt
import sys
import re

# USAGE:
# Param 1: Over how much to average over
# Param 2..n: Path to source files


def main():

    data = []

    average_over = int(sys.argv[1])

    for i in range(1, len(sys.argv) - 1):
        data1 = []
        data2 = []
        with open(sys.argv[i + 1]) as f:
            for line in f:
                split = line.split(' ')
                if len(split) > 6:
                    if len(split) >= 10 and "'dev'" in split[2] \
                            and re.match("^\d+?\.\d+?$", split[9].split(',')[0]) is not None:
                        data1.append(float(split[9].split(',')[0]))
                    elif re.match("^\d+?\.\d+?$", split[6].split(',')[0]) is not None:
                        data1.append(float(split[6].split(',')[0]))
                elif len(split) == 2:
                    split2 = re.split(r'\[|\]', split[1])
                    if len(split2) == 3:
                        data1.append(float(split2[1]))
            new_data = 0
            for i in range(len(data1)):
                new_data += data1[i]/average_over
                if i % average_over == 0:
                    data2.append(new_data)
                    new_data = 0
        data.append(data2)

    colours = ['r', 'b', 'g']

    for i in range(len(data)):
        plt.plot(data[i], colours[i])
    plt.show()


if __name__ == '__main__':
    main()
