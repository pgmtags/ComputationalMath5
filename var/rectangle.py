from var.modules import np, plt


def right_rectangles_method(f_values, h):
    """
    Calculation of the definite integral using precomputed function values and step size.

    Args:
      f_values: Precomputed values of the integrand function.
      h: Width of each sub-interval.

    Returns:
      Approximate value of the integral.
    """
    return h * np.sum(f_values)


def plot_function_and_rectangles(a, b, f, x_values, f_values, h):
    x_plot = np.linspace(a, b, 500)
    y_plot = f(x_plot)
    plt.plot(x_plot, y_plot, label="f(x)")

    # Plot rectangles using precomputed values and align with the right edge
    plt.bar(x_values - h, f_values, width=h, align='edge', color="yellow", edgecolor='black', label="Rectangles")

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral approximation using the Right Rectangles Method')
    plt.legend()
    plt.grid(True)
