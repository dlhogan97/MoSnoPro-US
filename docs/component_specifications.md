# User Interfaces

## Central panel (map) - this is the primary visual component
- What it does: displays geography of Washington State. Displays sites where model data is available. Interactive.
- Inputs: separate shapefiles for geography and boundary lines for northwest region, WA state counties
- Outputs: WA state map overlaid (highlighted) over a faded out mapview of the broader region, which works because the state's county boundaries will be defined (but not selectable). 
- Components used
	- Map, station database, visualization database, user input point/click
- Side Effects
	- Filled blank space below the map upon click
	- Site metadata (summary) appears upon hover on map next to station

### Points on map
- What it does: Displays individual locations of approximately 80 SNOTEL sites across Washington State as dots/buttons. 
- Inputs: latitude and longitude data for each station location


## Side-bar, left
- What it does: Displays three panels, each with different options for what can be displayed in the bottom panel

### Data Filtering
- What it does: provide the user with a few different options for what data is displayed.

## Bottom panel, model visualizations
- What it does: has two panes to display up to 2 figures
- Inputs: data from SUMMA model, filtered to show 



## Bridge that feeds SUMMA output dataframe to server
- What it does: 
