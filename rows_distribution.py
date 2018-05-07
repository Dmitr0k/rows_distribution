import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # variables
    i = int(input("Input i: "))
    x = []
    p = []
    Fx = []
    Mx = 0

    for ind in range(0, i):
        x.append(int(input("Input x[{0}]: ".format(ind))))
        p.append(float(input("Input p[{0}]: ".format(ind))))
        print("")
    os.system("clear")

    if sum(p) == 1:
        # print table
        print("x[i]", end='')
        for ind in range(0, i):
            print("\t{0}".format(x[ind]), end='')
        print("\np[i]", end='')
        for ind in range(0, i):
            print("\t{0}".format(p[ind]), end='')
        print("")

        # calc and print F(x)
        for ind in range(0, i+1):
            Fx.append(float(format(sum(p[some] for some in range(0, ind)), ".2f")))

        # calc and print Mx
        Mx = float(format(sum(x[ind]*p[ind] for ind in range(0, i)), ".3f"))

        # calc and print Dx
        Mxx = sum((x[ind]**2)*p[ind] for ind in range(0, i))
        Dx = float(format(Mxx - Mx**2, ".3f"))

        # print result
        result_text = "\nF(x):"
        result_text += "\n0 for x <= {0}".format(x[0])
        for ind in range(0, i - 1):
            result_text += "\n{0} for {1} < x <= {2}".format(Fx[ind + 1], x[ind], x[ind + 1])
        result_text += "\n{0} for x > {1}".format(Fx[i], x[i - 1])
        result_text += "\n\nM(x) = {0}".format(Mx)
        result_text += "\n\nD(x) = {0}".format(Dx)
        print(result_text)

        # first graph params
        leftlim1 = x[0] - 5
        rightlim1 = x[len(x)-1] + 5
        vx1 = np.array([])
        vy1 = np.array([])
        shiftx = np.array([])
        shifty = np.array([])

        for fx in Fx:
            vy1 = np.append(vy1, fx)
        for ind in range(0, len(x)):
            vx1 = np.append(vx1, x[ind])
        vx1 = np.append(vx1, rightlim1)
        for ind in range(0, len(Fx)):
            shifty = np.append(shifty, 0)
        shiftx = np.append(shiftx, -5)
        for ind in range(0, len(x)-1):
            shiftx = np.append(shiftx, x[ind]-x[ind+1])
        shiftx = np.append(shiftx, -5)

        # second graphic params
        ox = np.array(x)
        oy = np.array(p)

        # graphics
        fig1 = plt.figure()
        fig1.canvas.set_window_title("Rows distribution by Dmitr0k")
        fig1.subplots_adjust(hspace=0.35)
        # ax1 = fig1.add_subplot(1, 1, 1)
        ax1 = fig1.add_subplot(2, 2, 1)
        ax1.quiver(vx1, vy1, shiftx, shifty, angles='xy', scale_units='xy', scale=1)
        ax1.grid()
        ax1.set_axisbelow(True)
        major_x_ticks_1 = np.arange(leftlim1, rightlim1 + 1, 2)
        major_y_ticks_1 = np.arange(0, 1.1, 0.1)
        ax1.set_xticks(major_x_ticks_1)
        ax1.set_yticks(major_y_ticks_1)
        ax1.grid(which='major', linestyle='-', linewidth='0.2', color='black')
        ax1.set_title('Distribution function')

        # fig2 = plt.figure()
        # ax2 = fig2.add_subplot(1, 1, 1)
        ax2 = fig1.add_subplot(2, 2, 2)
        ax2.plot(ox, oy)
        ax2.grid(which='major', linestyle='-', linewidth='0.2', color='black')
        ax2.set_title('Polygon distribution')

        #table
        ax_result = fig1.add_subplot(2, 2, 3, frameon=False)
        plt.setp(ax_result, xticks=[], yticks=[])
        ax_result.text(0, 0, result_text, transform=ax_result.transAxes)

        #result
        ax_table = fig1.add_subplot(2, 2, 4, frameon=False)
        row_labels = ['x[i]', 'p[i]']
        plt.setp(ax_table, xticks=[], yticks=[])
        ax_table.table(cellText=[x, p], loc='upper center', rowLabels=row_labels)


        plt.tight_layout()
        plt.show()

    else:
        print("Sum of p[i] must be equal to 1")

