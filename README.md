# MoSnoPro-US 🏔️❄️
MoSnoPro-US stands for Modeling Snow Properties - Using SUMMA, a modeling and visualization tool for snow pack properties using real time (and possibly forecasted) observations in Washington State, USA.

### **Project summary:**
As a short summary, the plan is to make an interactive tool for running a snow model at different sites across Washington and providing visualizations that convey possible instabilities within the snowpack for the user. Additionally, if all goes well, I would consider adding in a forecasting aspect, which uses weather model data to try to forecast how the snowpack may change in the few days ahead.

### **Background:**
Like pages of a book, each passing storm during the winter builds what we call the snowpack. Different "pages" in the snowpack book (we call them layers) react and change to the overlying weather conditions throughout the winter. Certain conditions cause layers within the snowpack to become unstable. Instabilities in the snowpack are hard to predict and difficult to manage, but are a main component necessary for avalanches to occur. These avalanches pose risks to transportation, resources, and recreation in the area. Understanding when snow falls, how much snow falls, how dense that snow is, and the temperature within layers of the snowpack can provide useful information to predict which layers may become unstable. Models can provide us with a tool to see into the snowpack without needing to go into the field to measure these parameters. However, modeling obviously carries ample amounts of uncertainty, so certain methods should be employed to try to limit that uncertainty.

### **Inspiration Examples:**
I wanted to provide a few examples of the type of tool I'm thinking of. The two below are examples from CW3E (Center for Western Water and Weather Extremes). They have a point + click tool that provides useful information about forecasted storm precipitation totals from 2 different ensemble weather models (GEFS and EPS) and freezing levels (where falling snow will melt to rain) throughout river basins/watersheds in the western United States. Check out the tool [here](https://cw3e.ucsd.edu/DSMaps/DS_freezing.html).

### **Model:**
The model we will be using is called SUMMA (Structure for Unifying Multiple Model Alternatives). It has a python wrapper and can be installed as a python package. See the documentation [here](https://github.com/UW-Hydro/pysumma).

### **Data:** 
1. The dataset will be from NRCS (National Resource Conservation Service) SNOTEL (Snow Telemetry) weather stations throughout Washington. We will use a tool called metloom to efficiently access this data. See documentation [here](https://metloom.readthedocs.io/en/latest/). A map of all the sites in the Western United States and Canada is available [here](https://nwcc-apps.sc.egov.usda.gov/imap/).
2. If we go the forecasting route, we will plan to use this python package called Herbie to dynamically download weather model data. See documentation [here](https://herbie.readthedocs.io/en/stable/). Another option is [open-meteo](https://open-meteo.com/en/docs/ecmwf-api).

### **Data Visualization**

Using Streamlit as a tool to visual data

#### **Team:**
Danny Hogan, Civil and Environmental Engineering (lead)
Bow Sruangsung, Civil and Environmental Engineering
Xiayang Tang, iSchool
Jane Dai, School of Public Health
