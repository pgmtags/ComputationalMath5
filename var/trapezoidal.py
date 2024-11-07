from var.modules import np, plt


def trapezoidal_method(f_values, h):
    """
    Calculation of the definite integral using precomputed function values and step size.

    Args:
      f_values: Precomputed values of the integrand function at all sub-interval boundaries.
      h: Width of each sub-interval.

    Returns:
      Approximate value of the integral.
    """
    return h / 2 * np.sum(f_values[0:-1] + f_values[1:])


def plot_function_and_trapezoids(a, b, f, x_values, f_values, h):
    x_plot = np.linspace(a, b, 500)
    y_plot = f(x_plot)
    plt.plot(x_plot, y_plot, label="f(x)")

    for i in range(len(x_values) - 1):
        # Plotting trapezoids
        plt.fill_between([x_values[i], x_values[i + 1]],
                         [f_values[i], f_values[i + 1]],
                         color='green', edgecolor='black')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral approximation using the Trapezoidal Method')
    plt.legend()
    plt.grid(True)
