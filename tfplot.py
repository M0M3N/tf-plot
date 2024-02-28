import sys
from matplotlib import pyplot as plt
import control

def invalid_usage():
    print("\nusage:\n\ntfplot.py <numerator_coefficients/denominator_coefficients> <plot>\n")
    print("the plot number corresponds to a specific plot:\n1) Nyquist\n2) Bode plot\n3) Root locus\n")
    print("for example, if you want the Nyquist plot for the transfer function (s^2+2s+7)/(s^3+s+3) enter:")
    print("tfplot.py 1,2,7/1,0,1,3 1\n")
    exit(0)

if (len(sys.argv) < 3 or (not 0 < int(sys.argv[2]) < 4) or sys.argv[1].find("/") == -1):
    invalid_usage()

tf, plot = sys.argv[1:3]
num, den = [c.split(",") for c in tf.split("/")]


num_coe = [int(item) for item in num]
den_coe = [int(item) for item in den]


G = control.TransferFunction(num_coe, den_coe)


if plot == '1':
        # draw Nyquist plot of the transfer function
        klist = control.nyquist(G)
elif plot == '2':
        # draw Bode plots
        klist = control.bode(G)
elif plot == '3':
        # draw the root locus plot
        klist = control.root_locus(G)

plt.show()