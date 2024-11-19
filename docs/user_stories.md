# User Stories
1. Dallas is a avalanche forecaster. He works for the Northwest Avalanche Center and he wants to remotely access snowpack information daily. He wants this information to better understand how the snowpack responds to overlying weather conditions. He has little time available to spend sifting through lots of information and data, but he is very profiecient in understanding snow and meteorology.
2. Cassie is an avid snowboarder. She is new to the region with prior experience in Colorado. She wants to access information to better understand the local snowpack and how it changes over the winter. She wants to know when it may be better or worse to ski. She has experience with interacting with snow, but is not super technical on the snow science.
3. Jay is a ski resort manager. He is trying to better understand when to deploy snowcats for grooming trails. He desires a simple and up-to-date interface for forecasting how much snow may fall at his resort.
4. Logan is a hydrologist for the Washington Department of Ecology. He wants to monitor snowpack water content across multiple basins to forecast spring runoff for reservoir management. Logan needs precise data and visualizations that integrate basin-scale snowpack summaries, accessible via a professional yet user-friendly platform.
5. Emma studies the impact of climate change on snowpack in the Cascades. She needs access to historical snow model outputs to analyze trends in snow accumulation and melt patterns over the past decades. She is comfortable with technical data but prefers an intuitive interface for overlaying trends on maps.
6. Tyler enjoys backcountry skiing and wants to plan trips based on snow stability and depth. He needs an interactive map with forecasted snow depth and stability metrics for specific locations. Tyler values clear, non-technical explanations of avalanche risks linked to the data.
7. Natalie oversees water supplies for a municipal utility in the Puget Sound region. She wants daily updates on snowpack conditions in key watersheds to forecast water availability during the summer. Natalie prefers concise dashboards with color-coded alerts for snowpack deficits.
8. Chris works for a local TV station providing weather updates. He needs snowpack data that integrates with short-term weather forecasts to report on expected snow accumulation for recreational and public safety purposes. Chris values attractive, easy-to-read visuals for use in broadcasts.
9. Sophia teaches earth sciences at a community college in Washington. She wants her students to explore real-world snowpack data to understand hydrological cycles and the effects of weather. She needs an interactive map and downloadable datasets for class projects.
10. Eli works for the U.S. Forest Service and manages snow-covered trails. He needs localized snow depth and melt forecasts to prioritize trail maintenance and manage seasonal closures. Eli prefers clear, actionable data with minimal technical jargon.
11. Maya studies snowpack processes and requires access to snow model outputs at high spatial and temporal resolutions. She is comfortable with downloading raw data but would appreciate built-in tools to quickly visualize trends in snowpack and related weather conditions.
12. Ryan leads snowshoeing tours in the Cascades. He wants daily snow conditions for popular trails to plan safe routes and advise clients on gear. He prefers a straightforward app interface with mobile compatibility for quick checks in the field.

# Implied User
This implied user is the model itself.
- To make sure the data is available and rerun.
- Data caches?
- Functionality when the data goes down. Last update, next update expected
- Implied functonality with up-to-date data as available/run at a given time. 
- Fault tolerance. 
 
# Authenticate User
- MVP without authentication
- Give default products for simple use cases
- Provide advanced features? 
- Remove informaton about how the data is hosted 

# User Interfaces
### Map
- What it does: displays geography of Washington State. Displays sites where model data is available. Interactive.
- Inputs:
	- location data of sites
	- point-and-click command
- Outputs
	- hover feature: output of station metadata
	- click feature: outputs the model visualization.
- Components used
	- Map, station database, visualization database, user input point/click
- Side Effects
	- Filled blank space opposite of the map upon click
	- Site metadata appears upon hover on map next to station
### Data Filtering
- What it does: provide the user with a few different options for what data is displayed. 
### Model Data Bridge

