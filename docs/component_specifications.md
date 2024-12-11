# Component Specification

## Software Components

### 1. Data Manager
**What it does:**
The Data Manager handles the acquisition, storage, and preprocessing of snow and weather data (e.g. snowfall, snowpack properties, SNOTEL data) and model outputs . It acts as the interface between raw data and other system components, offering functionality like querying subsets of the data, ensuring data integrity, and processing data for visualizations.  

**Inputs:**
- Raw datasets, such as:
	- SNOTEL CSVs containing snowpack metrics
	- SUMMA model outputs in NetCDF format
- Query parameters (e.g., date ranges, locations, and metrics to filter)

**Outputs:**
- Cleaned and structured datasets (e.g. pandas DataFrames or xarray Datasets.)
- Metadata about data quality (e.g., last update, missing values).
___

#### 2. Visualization Manager
**What it does:** 
The Visualization Manager creates interactive and static visualizations for analyzing snowpack properties and trends. It supports predefined plots (e.g., time-series, snow depth vs. temperature graphs) and custom visualizations based on user preferences.

**Inputs:**
- Processed data from the Data Manager.
- User-defined visualization parameters (e.g., graph type, axis labels, filters)

**Outputs:**
- Interactive visualizations (e.g dashboard) rendered in the Streamlit app   
- Static plots exportable as PNG, SVG, or PDF for presentations
- Central panel (map) - this is the primary visual component
	- What it does: displays geography of Washington State. Displays sites where model data is available. Interactive.
	- Inputs: separate shapefiles for geography and boundary lines for northwest region, WA state counties
	- Outputs: WA state map overlaid (highlighted) over a faded out mapview of the broader region, which works because the state's county boundaries will be defined (but not selectable). 
	- Components used
		- Map, station database, visualization database, user input point/click, curser zoom in/out
	- Side Effects
		- Filled blank space to the right the map upon click
		- Site metadata (summary) appears upon hover on map next to station
	- Points on map
		- What it does: Displays individual locations of approximately 10 SNOTEL sites across Washington State as black dots. 
	- Side-bar, left
		- What it does: Displays two options for the main screen in Streamlit (Overview page, Interactive map)
		- Inputs: String text
		- Outputs: Main screen display
- Data Filtering
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
___

### 3. Decision Support Module
**What it does:**
The Decision Support Module generates actionable insights based on processed data and predefined thresholds. It simplifies decision-making by producing summaries, alerts, or rankings tailored to user needs (e.g., public communication, avalanche forecasting, or safety management).  

**Inputs:**
- Processed data from the Data Manager.
- Predefined thresholds or rules (e.g., snow accumulation levels for closures).
- User queries (e.g., “areas with highest snow accumulation”).

**Outputs:**
- Alerts or warnings (e.g., “High snowfall detected in Zone X”).
- Summaries or decision matrices for high-impact recommendations.
___

## Interactions to Accomplish Use Cases
### Use Case: Monitor Snowpack Conditions for Avalanche Safety
1. **Data Manager Interaction**
	- Fetches weather and snowpack data (e.g. from SNOTEL stations and SUMMA model outputs).
	- Preprocesses data to filter for selected stations and time periods.
2. **Visualization Manager Interaction**
	- Generates visualizations, such as snow depth vs temperature graphs, to help users analyze snowpack stability.
	- Provides interactive maps for users to select specific sites and visualize snowpack properties.
3. **Decision Support Module Interaction**
	- Indentifies high-risk zones based on predefined thresholds (e.g. snow depth > 2m and temperature fluctuations).
	- Sends alerts or summaries to avalanche forecasters for rapid decision-making.
___

## Preliminary Plan
1. **Setup and Framework:**
	- Configure the project directory for modular design and test-driven development.  
   - Integrate Streamlit for user interface components.
2. **Data processing and Visualization:**
	- Double-check model can generate plots for SNOTEL sites, assess time-to-completion to understand user wait-time burden
	- Build plotting functions based on SNOTEL string names
	- Update "secrets" for Dropbox file access to model data (Streamlit can handle the raw output to generate maps on command)
	- Write and test functions for gathering model output
	- Write and test functions for plotting model output
	- Write and test functions for user experience fine-tuning in Streamlit
	- Determine best approach for using Streamlit (Folium)
3. **Testing and Iteration:**
	- Update doc strings for all functions
	- Validate all features with comprehensive unit and integration tests.  
	- Continue to iterate (code review, documentation), or at least identify areas that need continuous refinement
4. **Documentation and Deployment:**
	- Write detailed documentation for end-users and developers.  
   	- Deploy the application