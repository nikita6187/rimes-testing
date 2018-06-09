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
                print(line)
                split = line.split(' ')
                if len(split) > 6:
                    print(split[6].split(',')[0])
                    if re.match("^\d+?\.\d+?$", split[6].split(',')[0]) is not None:
                        data1.append(float(split[6].split(',')[0]))
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
