# Component Specification

## Software Components

### Central panel (map) - this is the primary visual component
- What it does: displays geography of Washington State. Displays sites where model data is available. Interactive.
- Inputs: separate shapefiles for geography and boundary lines for northwest region, WA state counties
- Outputs: WA state map overlaid (highlighted) over a faded out mapview of the broader region, which works because the state's county boundaries will be defined (but not selectable). 
- Components used
	- Map, station database, visualization database, user input point/click
- Side Effects
	- Filled blank space below the map upon click
	- Site metadata (summary) appears upon hover on map next to station

#### Points on map
- What it does: Displays individual locations of approximately 80 SNOTEL sites across Washington State as dots/buttons. 
- Inputs: latitude and longitude data for each station location
- ...


### Side-bar, left
- What it does: Displays three panels, each with different options for what can be displayed in the bottom panel
- ...

#### Data Filtering
- What it does: provide the user with a few different options for what data is displayed. Allows customization based on location and snowpack attributes (filter out based the dangerous level, or based on the specific location )
- Inputs:
	- Users select specific sites through dropdown or multi-select list 
	- Users choose which specific snowpack properties to focus on (danger level)
- Outputs
	- Filtered Data for Visualizations: the filtered dataset will be passed to the visualization components to update the display dynamically
	- Interactive Display Updates: when the user adjusts filters, visualizations update immediately to reflect the selected parameters.
- Components used
	- Map, station database, visualization database, user input point/click
- Side Effects
	- Highlight the sites selected. Grey down the sites not selected.


### Bottom panel, model visualizations
- What it does: has two panes to display up to 2 figures
- Inputs: data from SUMMA model, filtered to show...

#### Decision Support Module
- What it does: The Decision Support Module provides actionable insights based on processed data and user requirements. It includes features like generating alerts, ranking scenarios, and offering summaries tailored to specific use cases (e.g., public communication or safety decisions).
- Inputs:
	- Processed data from the Data Manager.
	- Predefined thresholds or rules (e.g., snow accumulation levels for closures).
	- User queries (e.g., “areas with highest snow accumulation”).
- Outputs:
	- Textual summaries or alerts (e.g., “High snowfall detected in Zone X”).
	- Decision matrices or ranked lists for high-impact recommendations.

#### Visualization Manager
- What it does: The Visualization Manager is responsible for creating interactive and static visualizations based on processed data. It supports both predefined visualizations (e.g., heatmaps, trend graphs) and custom plots based on user needs.
- Inputs:
	- DataFrames from the Data Manager.
	- User preferences for visualizations (e.g., graph type, axis labels, themes).
- Outputs:
	- Interactive dashboards or static plots in formats such as PNG or SVG.
	- Embeddable components for integration into reports or presentations.



### Model Data Bridge / Data Manager
- What it does: The Data Manager handles the acquisition, storage, and preprocessing of snow and wather data and model outputs. It provides an interface for querying subsets of the data based on user-defined filters and ensures data integrity across the system.
- Inputs:
	- Raw datasets (e.g., snowfall, snowplow activity, traffic incidents) in formats such as CSV, JSON, or through APIs.
	- Query parameters (e.g., date ranges, locations, and metrics to filter).
- Outputs:
	- Cleaned and filtered datasets, structured as DataFrames.
	- Metadata about data quality (e.g., last update, missing values).

## Interactions to Accomplish Use Cases

## Preliminary Plan