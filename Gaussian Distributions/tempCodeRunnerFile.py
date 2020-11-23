    for i in range(len(mu_var)):
        plt.subplot(2,3,i+1)
        plt.title("CDF Over [" + str(start_val) + ", " + str(end_val) + 
            "] For (mu=" + str(mu_var[i][0]) + " var=" + str(mu_var[i][1]) + ")")
        plt.plot(x_vals, plot_vals_cdf[i].values())
        plt.xlabel("Interval Values")
        plt.ylabel("F(x)")      
    plt.show()  