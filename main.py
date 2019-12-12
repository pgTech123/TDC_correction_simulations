import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from transfer_function_ideal import TransferFunctionIdeal
from transfer_function_no_correction import TransferFunctionNoCorrections
from transfer_function_ICSSHSR4 import TransferFunctionICSSHSR4
from transfer_function_ICYSHSR1 import TransferFunctionICYSHSR1

TDC_VISUALIZED = 6

def main():
    filename = "./../data/Demo_Uncorrelated_coefficients_4.txt"
    tf_ideal = TransferFunctionIdeal(filename=filename, tf_starts_at_origin=True)
    tf_icsshsr4_median = TransferFunctionICSSHSR4(tf_ideal, algorithm="median")
    tf_icsshsr4_linear_reg = TransferFunctionICSSHSR4(tf_ideal, algorithm="linear_regression")
    tf_icyshsr1 = TransferFunctionICYSHSR1(tf_ideal, "lookup_coarse")
    tf_icyshsr1_better = TransferFunctionICYSHSR1(tf_ideal, "lookup_and_fine_correction")


    tf_graph_ideal = tf_ideal.get_transfer_functions_raw_data()
    tf_graph_icsshsr4_median = tf_icsshsr4_median.get_transfer_functions_raw_data()
    tf_graph_icsshsr4_linear_reg = tf_icsshsr4_linear_reg.get_transfer_functions_raw_data()
    tf_graph_icyshsr1 = tf_icyshsr1.get_transfer_functions_raw_data()
    tf_graph_icyshsr1_better = tf_icyshsr1_better.get_transfer_functions_raw_data()

    # Transfer function graph
    plt.figure()
    plt.plot(tf_graph_ideal[0][1], tf_graph_ideal[1][1], 'k--', label="Ideal Transfer Function")
    plt.plot(tf_graph_icsshsr4_median[0][1], tf_graph_icsshsr4_median[1][1], 'g', label="ICSSHSR4 Algorithm: Median Slope")
    plt.plot(tf_graph_icsshsr4_linear_reg[0][1], tf_graph_icsshsr4_linear_reg[1][1], 'r', label="ICSSHSR4 Algorithm: Linear Regression")
    plt.plot(tf_graph_icyshsr1[0][1], tf_graph_icyshsr1[1][1], 'b', label="ICSSHSRY Algorithm: Bias correction on each coarse")
    plt.plot(tf_graph_icyshsr1_better[0][1], tf_graph_icyshsr1_better[1][1], 'm', label="ICSSHSRY Algorithm: Bias and slope correction on each coarse")
    plt.title("Transfer function of the time conversion for different algorithms")
    plt.legend()

    # Error graph
    plt.figure()
    plt.plot(tf_graph_ideal[0][TDC_VISUALIZED], tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icsshsr4_linear_reg[1][TDC_VISUALIZED], 'r', label="Linear Regression")
    plt.plot(tf_graph_ideal[0][TDC_VISUALIZED], tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icsshsr4_median[1][TDC_VISUALIZED], 'g', label="Median Slope")
    plt.plot(tf_graph_ideal[0][TDC_VISUALIZED], tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icyshsr1[1][TDC_VISUALIZED], 'b', label="Bias correction on each coarse")
    plt.plot(tf_graph_ideal[0][TDC_VISUALIZED], tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icyshsr1_better[1][TDC_VISUALIZED], 'm', label="Bias and slope correction on each coarse")
    plt.title("Error between the ideal transfer function and different correction algorithms")
    plt.legend()

    # METRICS
    min_ideal_icsshsr4_median = min(tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icsshsr4_median[1][TDC_VISUALIZED])
    max_ideal_icsshsr4_median = max(tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icsshsr4_median[1][TDC_VISUALIZED])

    min_ideal_icsshsr4_linear_reg = min(tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icsshsr4_linear_reg[1][TDC_VISUALIZED])
    max_ideal_icsshsr4_linear_reg = max(tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icsshsr4_linear_reg[1][TDC_VISUALIZED])

    min_ideal_icyshsr1 = min(tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icyshsr1[1][TDC_VISUALIZED])
    max_ideal_icyshsr1 = max(tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icyshsr1[1][TDC_VISUALIZED])

    min_ideal_icyshsr1_better = min(tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icyshsr1_better[1][TDC_VISUALIZED])
    max_ideal_icyshsr1_better = max(tf_graph_ideal[1][TDC_VISUALIZED]-tf_graph_icyshsr1_better[1][TDC_VISUALIZED])

    print("Error range on correction for ICSSHSR4 median: " + str(max_ideal_icsshsr4_median - min_ideal_icsshsr4_median) + ", max=" + str(max_ideal_icsshsr4_median) + ", min=" + str(min_ideal_icsshsr4_median))
    print("Error range on correction for ICSSHSR4 linear regression: " + str(max_ideal_icsshsr4_linear_reg - min_ideal_icsshsr4_linear_reg) + ", max=" + str(max_ideal_icsshsr4_linear_reg) + ", min=" + str(min_ideal_icsshsr4_linear_reg))
    print("Error range on correction for ICYSHSR1: " + str(max_ideal_icyshsr1 - min_ideal_icyshsr1) + ", max=" + str(max_ideal_icyshsr1) + ", min=" + str(min_ideal_icyshsr1))
    print("Error range on correction for ICYSHSR1 better: " + str(max_ideal_icyshsr1_better - min_ideal_icyshsr1_better) + ", max=" + str(max_ideal_icyshsr1_better) + ", min=" + str(min_ideal_icyshsr1_better))

    #plt.figure()
    #histogram = tf_ideal.get_histograms()[TDC_VISUALIZED]
    #plt.bar(x=histogram[1][:-1], height=histogram[0])

    #inl = tf_ideal.get_inl_data()
    #dnl = tf_ideal.get_dnl_data()

    #plt.figure()
    #plt.plot(inl[0][TDC_VISUALIZED], inl[1][TDC_VISUALIZED])
    #plt.plot(dnl[0][TDC_VISUALIZED], dnl[1][TDC_VISUALIZED])

    plt.show()


main()
