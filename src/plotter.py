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
        for i in range(int(self.time/self.vacc_time)):
            t_plot = t_plot + [i*self.vacc_time+1, i*self.vacc_time+2,
                               i*self.vacc_time+3, i*self.vacc_time+3+1e-12]
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
