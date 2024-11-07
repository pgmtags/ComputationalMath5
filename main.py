from var.rectangle import plot_function_and_rectangles, right_rectangles_method
from var.trapezoidal import plot_function_and_trapezoids, trapezoidal_method
from var.modules import f, plt, np


def main():
    # Set integration parameters
    a, b, n = 0.2, 1.2, 1000
    h = (b - a) / n

    # Define x-values for the integration (including left and right edges)
    x_values = np.linspace(a, b, n + 1)

    # Precompute function values at all sub-interval boundaries
    f_values = f(x_values)

    # Calculate the integral with precomputed function values
    integral_value1 = trapezoidal_method(f_values, h)
    integral_value2 = right_rectangles_method(f_values, h)

    # Create a figure with 2 rows and 1 column of subplots
    plt.figure(figsize=(10, 8))

    # First subplot: Trapezoidal Method
    plt.subplot(2, 1, 1)  # (rows, columns, index)
    plot_function_and_trapezoids(a, b, f, x_values, f_values, h)
    plt.title(f'Integral approximation using the Trapezoidal Method\nCalculated integral value: {integral_value1}')

    # Second subplot: Right Rectangles Method
    plt.subplot(2, 1, 2)  # (rows, columns, index)
    plot_function_and_rectangles(a, b, f, x_values, f_values, h)
    plt.title(f'Integral approximation using the Right Rectangles Method\nCalculated integral value: {integral_value2}')

    # Adjust layout to prevent overlap of titles and labels
    plt.tight_layout()

    # Show the plots
    plt.show()


if __name__ == "__main__":
    main()
