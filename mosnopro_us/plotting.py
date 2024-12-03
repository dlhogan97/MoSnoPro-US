# Adapted from https://github.com/UW-Hydro/pysumma/blob/master/pysumma/plotting/layers.py

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from utils import justify
import matplotlib.colors as colors
import pandas as pd


def plot_layers(var, depth, ax=None, colormap='viridis', plot_soil=True,
           plot_snow=True, variable_range=None, add_colorbar=True,
           line_kwargs={}, cbar_kwargs={}):
    """
    Makes a layers plot. Example usage:

    ::

        import pysumma.plotting as psp
        time_range = slice('10-29-2000', '04-30-2001')
        depth    = ds.isel(hru=0).sel(time=time_range)['iLayerHeight']
        temp     = ds.isel(hru=0).sel(time=time_range)['mLayerTemp']
        psp.layers(temp, depth)

    Parameters
    ----------
    var: xr.DataArray
        The variable holding the data to plot.
        Typically begins with ``mLayer``.
    depth: xr.DataArray
        The variable defining the depths of the interfaces
        of each layer. Typically should be ``iLayerHeight``
    ax: Axes
        The axis to plot on. If none is given, a new axis
        will be created
    colormap: string, default='viridis'
        The colormap to use
    plot_soil: boolean, default=True
        Whether to plot the soil domain
    plot_snow: boolean, default=True
        Whether to plot the snow domain
    variable_range: List[float], default=variable range
        The range of numerical values to use. Must be two numbers.
    add_colorbar: boolean, default=True
        Whether to add a colorbar
    line_kwargs: Dict, default={}
        Keyword arguments to pass to ax.vlines.
        These draw the individual layers.
    cbar_kwargs: Dict, default={}
        Keyword arguments to draw the colorbar.
        They are passed directly to plt.colorbar.
    """
    # Preprocess the data
    vmask = var != -9999
    dmask = depth != -9999
    depth.values = justify(depth.where(dmask).values)
    var.values = justify(var.where(vmask).values)
    lo_depth = depth.where(depth > 0).T
    hi_depth = depth.where(depth < 0).T
    if plot_soil and not plot_snow:
        var = var.where((depth > 0).values[:,:-1]).T
    elif plot_snow and not plot_soil:
        var = var.where((depth < 0).values[:,:-1]).T
    else:
        var = var.T
    time = depth.time.values

    # Map colors to full range of data
    if variable_range is not None:
        assert len(variable_range) == 2, 'variable_range must have 2 values!'
        norm = plt.Normalize(variable_range[0], variable_range[1])
    else:
        norm = plt.Normalize(np.nanmin(var), np.nanmax(var))
    cmap = mpl.cm.get_cmap(colormap)
    rgba = cmap(norm(var))

    # Create axes if needed
    if not ax:
        fig, ax = plt.subplots(figsize=(18,8))

    # Plot soil layers - need to reverse because we plot bottom down
    if plot_soil:
        for l in lo_depth.ifcToto.values[:-1][::-1]:
            y = lo_depth[l]
            y[np.isnan(y)] = 0
            ax.vlines(time, ymin=-y, ymax=0, color=rgba[l], **line_kwargs)

    # Plot snow layers - plot top down
    if plot_snow:
        for l in hi_depth.ifcToto.values[:-1]:
            y = hi_depth[l]
            y[np.isnan(y)] = 0
            if (y != 0).any():
                ax.vlines(time, ymin=0, ymax=-y, color=rgba[l], **line_kwargs)

    # Add the colorbar
    mappable = cm.ScalarMappable(norm=norm, cmap=cmap)
    mappable.set_array(var.values.flatten())
    try:
        label = var.long_name
    except:
        label = var.name
    if 'label' not in cbar_kwargs.keys():
        cbar_kwargs['label'] = label
    if 'ax' not in cbar_kwargs.keys():
        cbar_kwargs['ax'] = ax
    if add_colorbar:
        plt.gcf().colorbar(mappable, **cbar_kwargs)
    return ax, mappable

# Create colomaps

# The range of temperature bins in Fahrenheit
a = np.arange(-20,5,1)

# Bins normalized between 0 and 1
norm = [(float(i)-min(a))/(max(a)-min(a)) for i in a]

# Color tuple for every bin
C = np.array([[145,0,63],
              [206,18,86],
              [231,41,138],
              [223,101,176],
              [255,115,223],
              [255,190,232],
              [255,255,255],
              [218,218,235],
              [188,189,220],
              [158,154,200],
              [117,107,177],
              [84,39,143],
              [13,0,125],
              [13,61,156],
              [0,102,194],
              [41,158,255], 
              [74,199,255], 
              [115,215,255], 
              [173,255,255],
              [48,207,194], 
              [0,153,150], 
              [18,87,87],
              [6,109,44],
              [49,163,84],
              [116,196,118],
              [161,217,155],
              [211,255,190],  
              [255,255,179], 
              [255,237,160], 
              [254,209,118], 
              [254,174,42], 
              [253,141,60], 
              [252,78,42], 
              [227,26,28], 
              [177,0,38], 
              [128,0,38], 
              [89,0,66], 
              [40,0,40]])/255.

# Create a tuple for every color indicating the normalized position on the colormap and the assigned color.
COLORS = []
for i, n in enumerate(norm):
    COLORS.append((n, C[i]))

temp_cmap = colors.LinearSegmentedColormap.from_list("Temperature", COLORS)
# The sky covered by clouds in percent (%)
a = range(50,500,50)

# Normalize the bin between 0 and 1 (uneven bins are important here)
norm = [(float(i)-min(a))/(max(a)-min(a)) for i in a]

# Color tuple for every bin
C = np.array([[36, 160, 242],
              [78, 176, 242],
              [128, 183, 248],
              [160, 200, 255],
              [210, 225, 255],
              [225, 225, 225],
              [201, 201, 201],
              [165, 165, 165],
              [110, 110, 110],
              [80, 80, 80]])

# Create a tuple for every color indicating the normalized position on the colormap and the assigned color.
COLORS = []
COLORS_r = []
for i, n in enumerate(norm):
    COLORS.append((n, np.array(C[i])/255.))
    COLORS_r.append((n, np.array(C[::-1][i])/255.))

# Create the colormap
density_cmap = colors.LinearSegmentedColormap.from_list("density", COLORS)

# create the inverse
density_cmap_r = colors.LinearSegmentedColormap.from_list("density_r", COLORS_r)

def get_snotel_depth(df, min_time):
    """This function gets the observed snow depth from the snotel and returns it as a pandas series"""
    # get snotel observation depth
    snow_depth_obs = df.loc[min_time:]['SNOWDEPTH'].resample('1D').max().shift()  * 2.54/100
    # replace below zero values with 0
    snow_depth_obs[snow_depth_obs < 0] = 0
    # replace nan values with nan
    snow_depth_obs[abs(snow_depth_obs.diff()) > 25] = np.nan
    # interpolate missing values
    snow_depth_obs = snow_depth_obs.interpolate()
    return snow_depth_obs

def produce_temp_depth_fig(summa_df, snotel_df, name):
    # get temperature and depth layers
    # get depth of each layer
    depth = summa_df.isel(hru=0)['iLayerHeight']
    # get temperature of each layer
    temp = summa_df.isel(hru=0)['mLayerTemp']
    # convert to Celsius
    temp = temp.where(temp<-100, temp-273.15)

    min_time = pd.to_datetime(depth.time.values.min())
    # get observed snow depth
    snow_depth_obs = get_snotel_depth(snotel_df, min_time)

    fig, ax = plt.subplots(figsize=(8,5))
    plot_layers(temp, (depth), colormap=temp_cmap, plot_soil=False, plot_snow=True, cbar_kwargs={'label': 'Temperature (C)', 'ticks':np.arange(-10,1,1)}, variable_range=[-10, 1], ax=ax)
    (summa_df['scalarSnowDepth']).plot(color='k', linewidth=2, ax=ax, label='SUMMA Modeled Snow Depth');
    snow_depth_obs.plot(color='red', ls='--', linewidth=2, ax=ax, label='Observed Snow Depth');
    ax.legend()
    ax.set_title(f"{name} Snow Depth\n{snow_depth_obs.index.min().strftime('%Y-%m-%d %H:%M')} to {snow_depth_obs.index.max().strftime('%Y-%m-%d %H:%M')}\nElevation: {snotel_df['geometry'].iloc[0][-5:-1]} ft")
    ax.set_ylabel('Snow Depth (m)')
    ax.set_xlabel('Date')
    fig.show()
    return fig

def produce_density_depth_fig(summa_df, snotel_df, name):
    # get temperature and depth layers
    # get depth of each layer
    depth = summa_df.isel(hru=0)['iLayerHeight']
    # get density of each layer
    density = summa_df.isel(hru=0)['mLayerVolFracWat']*1000
    density = density.where(density>=0, np.nan)

    min_time = depth.time.values.min()
    # get observed snow depth
    snow_depth_obs = get_snotel_depth(snotel_df, min_time)

    fig, ax = plt.subplots(figsize=(8,5))
    plot_layers(density, (depth), colormap=density_cmap_r, plot_soil=False, plot_snow=True, cbar_kwargs={'label': 'Density (kg/m$^3$)', 'ticks':np.arange(100,400,30)}, variable_range=[100, 400], ax=ax)
    (summa_df['scalarSnowDepth']).plot(color='k', linewidth=2, ax=ax, label='SUMMA Modeled Snow Depth');
    snow_depth_obs.plot(color='red', ls='--', linewidth=2, ax=ax, label='Observed Snow Depth');
    ax.legend()
    ax.set_title(f"{name} Snow Depth\n{snow_depth_obs.index.min().strftime('%Y-%m-%d %H:%M')} to {snow_depth_obs.index.max().strftime('%Y-%m-%d %H:%M')}\nElevation: {snotel_df['geometry'].iloc[0][-5:-1]} ft")
    ax.set_ylabel('Snow Depth (m)')
    ax.set_xlabel('Date')
    fig.show()
    return fig

def produce_liquid_water_depth_fig(summa_df, snotel_df, name):
    # get temperature and depth layers
    # get depth of each layer
    depth = summa_df.isel(hru=0)['iLayerHeight']
    # get density of each layer
    liq_water = summa_df.isel(hru=0)['mLayerVolFracLiq']*1000
    liq_water = liq_water.where(density>=0, np.nan)

    # get observed snow depth
    snow_depth_obs = get_snotel_depth(snotel_df)

    fig, ax = plt.subplots(figsize=(8,5))
    plot_layers(liq_water, (depth), colormap=density_cmap_r, plot_soil=False, plot_snow=True, cbar_kwargs={'label': 'Liquid Water Content (kg/m$^3$)', 'ticks':np.arange(0,100,10)}, variable_range=[0, 100], ax=ax)
    (summa_df['scalarSnowDepth']).plot(color='k', linewidth=2, ax=ax, label='SUMMA Modeled Snow Depth');
    snow_depth_obs.plot(color='red', ls='--', linewidth=2, ax=ax, label='Observed Snow Depth');
    ax.legend()
    ax.set_title(f"{name} Snow Depth\n{snow_depth_obs.index.min().strftime('%Y-%m-%d %H:%M')} to {snow_depth_obs.index.max().strftime('%Y-%m-%d %H:%M')}\nElevation: {snotel_df['geometry'].iloc[0][-5:-1]} ft")
    ax.set_ylabel('Snow Depth (m)')
    ax.set_xlabel('Date')
    fig.show()
    return fig