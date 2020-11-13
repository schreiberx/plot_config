#! /usr/bin/env python3

#
# Author: Martin Schreiber <martin.schreiber@tum.de>
#
# Creation Date: Somewhen 2019
#
# Changelog:
# 2019-01-14: Minor updates & Cleanups (Martin)
# 2019-02-01: Added markevery option
#

#
# There is an EXAMPLE GIVEN BELOW which plots a picture if this file is executed directly
#



def setup(
        figsize = None, # Size of figure
        scale = 1.0,    # Scaling factor for default image size
                        # Use only this to resize your image.
        nrows = 1,      # Number of rows in plot
        ncols = 1,      # Number of colums in plot
    ):
    """
    Setup the plotting with default parameters which are optimized for PDF DinA4 plots

    Use the 'scale' parameter to enlarge or shrink the picture if required
    """

    #
    # Important: Optimize this only for PDF output!
    #
    import matplotlib
    matplotlib.rcParams.update({'figure.dpi': 300})
    matplotlib.rcParams.update({'font.size': 8})
    matplotlib.rcParams.update({'legend.fontsize': 6})

    import __main__ as pc

    if figsize == None:
        default_figsize = (4, 3)
        figsize = (default_figsize[0]*scale, default_figsize[1]*scale)
    else:
        figsize = (figsize[0]*scale, figsize[1]*scale)

    import matplotlib.pyplot as plt

    # Start new plot
    plt.close()

    return plt.subplots(nrows, ncols, figsize=figsize)



class PlotStyles:
    """
    Class which provides a variety of plot styles

    There are three different styles, for lines, markers and colors

    Using different lines and markers is in particular helpful for colorblind people.
    """

    def __init__(self):

        self.markers = []

        # dot
        self.markers += ['.']

        # crosses
        self.markers += ['1', '2', '3', '4', '+', 'x']

        # Triangles
        self.markers += [4, 5, 6, 7, 8, 9, 10, 11]

        self.linestyles = [
            #(?, (line, spacing)
            (0, (1, 1)),

            (0, (8, 1)),
            (0, (5, 1)),

            (0, (3, 2, 5, 2)),
            (0, (3, 1, 1, 1)),

            (0, (6, 1, 6, 1, 6, 1)),
        ]

        self.colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

        self.reset()

    def reset(self):
        """
        Reset all style counters
        """
        self.c_colors = 0
        self.c_markers = 0
        self.c_linestyles = 0

    def set_color_counter(self, c):
        """
        Set style for color counter

        This is e.g. helpful to group some lines to have the same color
        """
        self.c_colors = c

    def set_marker_counter(self, c):
        """
        Set the marker style counter
        """
        self.c_markers = c

    def set_linestyle_counter(self, c):
        """
        Set the line style counter
        """
        self.c_linestyles = c


    def getNextStyle(self, num_points=None, num_markers=15):
        """
        Return a set of parameters which are ready to be used
        e.g. for plt.plot(...) with the ** Python feature, e.g.
        plt.plot(x, y, **ps.getNextStyle(), label="f(x) = cos(x)")
        """
        retval = {}

        retval['color'] = self.colors[self.c_colors % len(self.colors)]
        retval['marker'] = self.markers[self.c_markers % len(self.markers)]
        retval['linestyle'] = self.linestyles[self.c_linestyles % len(self.linestyles)]

        if num_points != None:
            retval['markevery'] = num_points//num_markers
            if retval['markevery'] == 0:
                retval['markevery'] = 1

        self.c_colors += 1
        self.c_markers += 1
        self.c_linestyles += 1

        return retval



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    # Import plot_config
    import plot_config as pc

    #
    # Call setup() for each new plot
    # Using scaling factor in case you need larger plots
    #
    # The default scaling of 1.0 is optimized for smaller
    # plots on presentations if you store them as a .pdf file
    #
    fig, ax = pc.setup(scale=1.0)

    #
    # Get a handler to different plotting styles
    #
    ps = PlotStyles()


    x = np.linspace(0, 1, 80)
    y = np.sin(x*10)

    #
    # The next plotting style can be loaded with ps.getNextStyle()
    # This returns a dictionary of parameters and values
    #
    # In order to use it as a parameter, we use the ** prefix
    #
    plt.plot(x, y, **ps.getNextStyle(), label="f(x) = sin(x)")

    y = np.cos(x*10)
    plt.plot(x, y, **ps.getNextStyle(), label="f(x) = cos(x)")

    y = x
    plt.plot(x[-len(x)//7:], y[-len(x)//7:], color='black', linestyle="dashed", linewidth=1, label="ref. order 1")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("plot_config example")
    plt.legend()
    plt.tight_layout()
    plt.show()

