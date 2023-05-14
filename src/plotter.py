import matplotlib.pyplot as plt


class Plot:

    def __init__(self, results, vacc_time, time):
        self.results = results
        self.vacc_time = vacc_time
        self.time = time

    # col: which column of the result we want to plot
    # col = 0: susceptible, col = 1: infected, col = 2: vaccinated
    def plot_results(self, col: int):
        r = self.results[:, col]
        # we saved the data before the vaccination and after the vaccination too
        # so to plot the results, in every Tth time point, the time interval should be near zero
        t_plot = [0]
        list1 = list(range(self.vacc_time+2))
        list1 = list1[1:]               # list of consecutive numbers 1, 2, ... , vacc_time+1
        for i in range(int(self.time/self.vacc_time)):
            l2 = list(map(lambda x: x + i*self.vacc_time, list1))  # multiply all the elements of list1 by i*vacc_time
            l2[-1] = l2[-1] - 1 + 1e-12             # the last element of the list should be the same as the previous
            t_plot = t_plot + l2
        # the last element of t_plot is after the last vaccination, but our results end before the last vaccination  
        t_plot = t_plot[:-1]            
        figure, axis = plt.subplots()
        axis.plot(t_plot, r, 'r', alpha=0.5)

        if col == 0:
            title = 'Susceptible'
        else:
            if col == 1:
                title = 'Infected'
            else:
                title = 'Vaccinated'

        axis.set_ylabel(title)
        plt.ylim([0, 1])
        plt.savefig("../plots/" + title + ".pdf")
        plt.show()

        return 0
