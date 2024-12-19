# Functional Specificaiton

## Background
Like pages of a book, each passing storm during the winter builds what we call the snowpack. Different "pages" in the snowpack book (we call them layers) react and change to the overlying weather conditions throughout the winter. Certain conditions cause layers within the snowpack to become unstable. Instabilities in the snowpack are hard to predict and difficult to manage, but are a main component necessary for avalanches to occur. These avalanches can pose risks to transportation, economic resources, property, and recreation in the area. Understanding when snow falls, how much snow falls, how dense that snow is, and the temperature within layers of the snowpack can provide useful information to predict which layers may become unstable. Models can provide us with a tool to see into the snowpack without needing to go into the field to measure these parameters. 

Avalanche forecasts rely on an accurate understanding of internal snowpack properties (temperature, density, etc.) to effectively communicate hazards to transportation and recreation in mountain environments. However, observations of internal snowpack properties are relatively few and far between since they require avalanche professionals to go into the field to take measurements. MoSnoPro-US offers a solution by providing estimates of important snowpack properties in an accessible format. The tool provides near-real time model results from a physically-based 1-D snow model driven by remote weather observations. This provides a way to remotely "see" into the snowpack to track internal snowpack changes that are difficult to capture across a broader area.


## Data Sources

Our data will leverage pandas (dataframes, geoJSONs) and xarray (netCDFs) to be compatiable with our software visualization tool, Streamlit. 

### SUMMA Model Output
The model we will be using is called SUMMA (Structure for Unifying Multiple Model Alternatives). It has a Python wrapper and can be installed as a Python package. See the documentation [here](https://github.com/UW-Hydro/pysumma). In our application, SUMMA is used as a physically-based 1-D snow model that provides output of internal snowpack properties. We will focus on visualizing attributes of snowpack depth, density, and temperature. 
- Weather data acquired from select remote snow telemetry stations throughout Washington located near major recreational areas. 

### SNOTEL Site Metadata
The dataset will be from NRCS (National Resource Conservation Service) SNOTEL (Snow Telemetry) weather stations throughout Washington. We will use a tool called `metloom` to efficiently access this data through their API. See documentation [here](https://metloom.readthedocs.io/en/latest/). A map of all the available NRCS SNOTEL sites in the Western United States and Canada is available [here](https://nwcc-apps.sc.egov.usda.gov/imap/).


## User Stories

### 1. Data Analyst

**Alex** is a data analyst at a transportation agency. He uses data on snowfall and its impact on road conditions to generate reports for decision-makers. Alex wants an application that simplifies filtering, visualizing, and extracting key patterns from large datasets, such as snowplow performance and accident trends. He has moderate programming skills and prefers an interface with intuitive controls and minimal setup. His primary need is interactive dashboards that help him explore correlations and export visuals for reports.

---

### 2. Graduate Student in Transportation Engineering

**Maria** is a graduate student researching the impact of snowstorms on road safety and traffic flow. She works with datasets from sensors and weather reports to develop insights for winter road maintenance strategies. Maria has basic programming experience and needs a tool that allows her to upload and analyze datasets quickly. She values interactive visualizations, such as time-series data of road conditions, and would like features that suggest possible interventions for safer winter roads.

---

### 3. Traffic Engineer

**James** is a traffic engineer responsible for ensuring road safety and maintaining traffic flow during snow events. He uses weather and traffic data to evaluate snowplow schedules, salt usage, and accident hotspots. James is not familiar with programming and relies on user-friendly software to analyze data. He needs an application that provides clear, actionable insights into road conditions, such as snowplow activity and accident trends, and allows for easy report generation to communicate with decision-makers.

---

### 4. Software Developer

**Priya** is a software developer maintaining a suite of tools for transportation analytics. She integrates weather and traffic data to create applications for snow management systems. Priya is proficient in Python and APIs, but she’s not an expert in transportation engineering. She needs a tool with a well-documented programming interface, allowing her to customize and integrate the MoSnoPro-US features into existing systems. She values flexibility, scalability, and ease of debugging when working with large datasets, such as traffic incidents during snowstorms.

---

### 5. Decision Maker/Manager

**Ethan** is a senior manager at a state department of transportation. He oversees resource allocation for snowplow operations and winter road maintenance. Ethan is not technical and relies on summary dashboards and visualizations to guide his decisions. He needs an application that provides key insights, such as snowplow coverage, road condition trends, and cost-efficiency metrics. The ability to quickly export visuals to presentation-ready formats like PDF or Excel is crucial for communicating with stakeholders and securing funding.

### 6. Avalanche Forecaster

**Dallas** is an avalanche forecaster at the Northwest Avalanche Center. He wants to remotely access snowpack information daily to better understand how the snowpack responds to overlying weather conditions. Dallas is very proficient in snow and meteorology but has little time to sift through large datasets. His primary need is a concise, high-quality interface that provides critical snowpack updates.

---

### 7. Snowboarder

**Cassie** is an avid snowboarder new to the region with prior experience in Colorado. She wants an application to better understand the local snowpack and how it changes over the winter, helping her decide when conditions are optimal for skiing. Cassie has experience interacting with snow but lacks technical knowledge in snow science. She prefers an easy-to-use tool with intuitive visuals.

---

### 8. Ski Resort Manager

**Jay** manages a ski resort and wants a simple, up-to-date interface for forecasting snow accumulation to optimize snowcat deployment for grooming trails. He prioritizes accuracy and real-time updates to ensure efficient resource management.

---

### 9. Hydrologist

**Logan** is a hydrologist for the Washington Department of Ecology. He monitors snowpack water content across multiple basins to forecast spring runoff and manage reservoirs. Logan needs precise data and visualizations that summarize basin-scale snowpack conditions, delivered through a professional and user-friendly platform.

---

### 10. Climate Researcher

**Emma** studies climate change impacts on snowpack in the Cascades. She needs access to historical snow model outputs to analyze trends in snow accumulation and melt patterns over past decades. While comfortable with technical data, Emma prefers an interface that overlays trends on maps intuitively.

---

### 11. Backcountry Skier

**Tyler** enjoys backcountry skiing and wants to plan trips based on snow stability and depth. He needs an interactive map that provides forecasted snow depth and stability metrics for specific locations. Tyler values clear, non-technical explanations of avalanche risks linked to the data.


---

### 12. Municipal Water Manager

**Natalie** oversees water supplies for a municipal utility in the Puget Sound region. She wants daily updates on snowpack conditions in key watersheds to forecast water availability during the summer. Natalie prefers concise dashboards with color-coded alerts for snowpack deficits.

---

### 13. TV Weather Reporter

**Chris** works for a local TV station providing weather updates. He needs snowpack data integrated with short-term weather forecasts to report on expected snow accumulation for recreational and public safety purposes. Chris values visually appealing, easy-to-read graphics for use in broadcasts.

---

### 14. Earth Sciences Educator

**Sophia** teaches earth sciences at a community college in Washington. She wants her students to explore real-world snowpack data to understand hydrological cycles and weather impacts. Sophia needs an interactive map and downloadable datasets suitable for class projects.

---

### 15. Forest Service Manager

**Eli** works for the U.S. Forest Service managing snow-covered trails. He needs localized snow depth and melt forecasts to prioritize trail maintenance and manage seasonal closures. Eli prefers clear, actionable data presented with minimal technical jargon.

---

### 16. Snow Scientist

**Maya** studies snowpack processes and requires access to snow model outputs with high spatial and temporal resolutions. She is comfortable with downloading raw data but appreciates built-in tools for quickly visualizing trends in snowpack and related weather conditions.

---

### 17. Snowshoeing Guide

**Ryan** leads snowshoeing tours in the Cascades. He wants daily snow conditions for popular trails to plan safe routes and advise clients on appropriate gear. Ryan values a straightforward app interface with mobile compatibility for quick field checks.

---

### 18. Graduate Student #1

**Ash** is a graduate student at UW who has never dabbled in snow sports, having grown up in Hawai'i. Since he has lots of nervous energy, he wants to be able to refresh a page daily to see if his first-ever upcoming group snowshoe trip might be during fair conditions. He wants to interact minimally with the page, relying on visual cues to have a "gut reaction" to snowpack conditions. Normally he works with a lot of data at work (and has a background in data visualization), but this is one thing in his life where he wants to not do no internal data processing. 

---

### 19. Graduate Student #2
**Juan** is a wildlife photographer who often goes on stake-outs for 6-8 hours at a time. He wants to check for stable snowpacks in Eastern Washington, and learn the area's humidity and temperature to prepare appropriate stake-out clothing attire. He wants a simple and concise summary of this information when identifying photography sites. Juan's job does not involve technical data skills (outside of image processing) and thus will appreciate simplicity (but not glossing over important details). 

---

### 20. Communications staff at WSDOT
**Tim** works for WSDOT and has been tasked to design content for the department's newest Instagram post. Since many backcountry skiiers have reached out to ask about safety closures following the bomb cyclone, he needs to find a source of information that he can check regularly without having to wait for results to be generated. He wants a simple overview of the situation where large amounts of snow have accumulated so that he can mark-up his own version of a WA state map to disseminate to non-technical audiences on social media. Tim's role as a front-facing, public communicator does not involve technical data skills. Since he also has no background in weather or safety science, he would also appreciate additional resources (like the Northwest Avalanche Center) that he can consult before making his final communication deliverable. 

---

### 21. Very busy, very stressed parent
**Pav** works two jobs and has been planning to take his 8-year-old daughter out for her first snowboarding adventure of the season. His partner was unexpectedly called away for a work emergency, and so he is unsure if he alone can handle the chaos of an all-day trek to the mountains on top of all the weather uncertainty. He does not have time to call the ski resort (only to be put on hold), so he needs a site he can check easily to get a quick decision aid. Because he has so much to juggle on his daily plate, he is looking for a "single click, immediate information" type of interaction. 

---

### 22. Ski Resort Workers' Union Organizer

**Ellen** organizes the union of ski resort workers at Stevens Pass, a supermajority of which have authorized a strike. They need to identify a high-impact strike time, which should coincide with the busiest weekend of the snow sport season. They need to proxy that traffic data using data from a year ago in conjunction with weather data so they don't actively endanger guests when the snowpack isn't safe. Ellen has a background in data science and is familiar with interpreting graphs that visualize longitudinal data. Ellen would also like to easily share the source data with other organizers who may be more familiar with the subject area. 



# User Profile Summaries

| **User**                              | **Knowledge**                                                                                             | **Needs**                                                                                         | **Information Users Want**                                                                             | **Use Cases**                                                                                                                                           |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Data Analyst (Alex)**                | Intermediate data analysis skills, moderate programming experience.                                       | Tools for filtering and visualizing snow and traffic data.                                         | Correlations between snowplow activity, snowfall, and traffic incidents.                               | 1. **Analyze Snowplow and Traffic Data**: Upload datasets, filter data, generate graphs, export to PDF.                                                |
| **Graduate Student (Maria)**           | Basic programming experience; knowledge of traffic and weather data analysis.                             | Intuitive tools to upload and analyze datasets quickly.                                            | Trends in road conditions during snowstorms and insights for interventions.                             | 1. **Analyze Snowplow and Traffic Data**: Import datasets, visualize trends, test intervention strategies.                                             |
| **Traffic Engineer (James)**           | Domain knowledge in transportation safety; minimal programming skills.                                    | User-friendly interface for evaluating snowplow and accident data.                                 | Accident hotspots, snowplow route efficiency, and resource summaries.                                   | 1. **Analyze Snowplow and Traffic Data**: Access dashboards, view heatmaps, generate summary reports.                                                  |
| **Software Developer (Priya)**         | Proficient in Python and APIs; less experience in transportation.                                         | Tools with well-documented APIs and customization features.                                        | APIs for querying datasets, code samples for extending functionality.                                   | 1. **Extend and Customize Features**: Use APIs to query data and embed visualizations into external systems.                                            |
| **Decision Maker (Ethan)**             | Minimal technical expertise; focuses on high-level summaries.                                             | Summary dashboards and easily exportable visuals.                                                  | Cost-efficiency metrics, snowplow coverage, and road condition trends.                                  | 1. **Monitor and Report Operations**: Access dashboards, export visuals for stakeholders.                                                              |
| **Avalanche Forecaster (Dallas)**      | Expert in snow and meteorology; prefers concise interfaces.                                               | High-quality snowpack updates in a concise format.                                                 | Daily snowpack stability updates and critical risk insights.                                            | 1. **Monitor Snowpack Conditions**: View dashboards summarizing critical snowpack metrics.                                                             |
| **Snowboarder (Cassie)**               | Limited technical knowledge but experienced in snow sports.                                               | User-friendly app for checking snow conditions.                                                    | Snowpack depth and trends, optimal skiing conditions.                                                   | 1. **Monitor Snowpack Conditions**: Explore snow depth trends, view basic recommendations.                                                             |
| **Ski Resort Manager (Jay)**           | Familiar with snow logistics but limited technical expertise.                                             | Accurate forecasts for snow accumulation and grooming optimization.                                | Snowfall predictions and real-time accumulation updates.                                                | 1. **Monitor Snowpack Conditions**: Access snowfall forecasts, export data for resource planning.                                                      |
| **Hydrologist (Logan)**                | Expert in water content monitoring; needs precise, actionable data.                                       | Tools for analyzing snowpack content and predicting runoff.                                         | Basin-scale snowpack metrics for spring runoff forecasts.                                               | 1. **Analyze Snowpack Trends**: Use maps with overlays of basin-level snow metrics, export data to hydrology models.                                    |
| **Climate Researcher (Emma)**          | Proficient in historical data analysis; focuses on trends.                                                | Tools for overlaying historical snow trends on maps.                                               | Decadal snow accumulation and melt patterns.                                                            | 1. **Analyze Snowpack Trends**: Visualize historical snow trends using dashboards, export charts for reporting.                                         |
| **Backcountry Skier (Tyler)**          | Non-technical but experienced in outdoor activities.                                                      | Easy-to-understand tools for planning safe ski trips.                                               | Avalanche risk data, snow stability metrics, and snow depth forecasts.                                  | 1. **Monitor Snowpack Conditions**: Access interactive maps, view avalanche risk metrics.                                                              |
| **Municipal Water Manager (Natalie)**  | Non-technical; focuses on actionable data.                                                               | Dashboards with snowpack alerts for water management.                                               | Color-coded alerts for snowpack deficits in key watersheds.                                              | 1. **Monitor Snowpack Conditions**: View alerts for snowpack deficits, export data for reports.                                                        |
| **TV Weather Reporter (Chris)**        | Non-technical; values visually appealing summaries.                                                       | Tools for creating broadcast-ready weather graphics.                                                | Visual summaries of snow conditions and short-term forecasts.                                           | 1. **Broadcast Weather Updates**: Generate and download visuals summarizing snow conditions for broadcasts.                                             |
| **Earth Sciences Educator (Sophia)**   | Familiar with basic data; prioritizes accessibility for students.                                         | Tools for accessing datasets and visualizations for teaching.                                       | Interactive maps and downloadable datasets for classroom projects.                                      | 1. **Teach Snowpack Concepts**: Provide real-world snowpack data for educational purposes.                                                             |
| **Forest Service Manager (Eli)**       | Limited technical knowledge; focuses on actionable insights.                                              | Tools for prioritizing trail maintenance schedules.                                                 | Localized snow depth and melt forecasts.                                                                | 1. **Monitor Snowpack Conditions**: View localized snow depth forecasts, export reports for planning.                                                   |
| **Snow Scientist (Maya)**              | Expert in snowpack processes and data visualization.                                                      | Tools for quickly visualizing high-resolution snow data.                                             | Trends in snowpack processes and associated weather conditions.                                          | 1. **Analyze Snowpack Trends**: Access visualization tools for high-resolution snow model outputs, download raw data.                                   |
| **Snowshoeing Guide (Ryan)**           | Minimal technical expertise; needs mobile-compatible tools.                                               | Mobile-friendly tools for checking snow conditions.                                                 | Snow stability and trail conditions for popular routes.                                                 | 1. **Monitor Snowpack Conditions**: Access mobile dashboards for quick trail condition checks.                                                         |
| **Graduate Student (Ash)**             | Prefers minimal interaction; focuses on quick updates.                                                    | Simple visualizations for assessing snow conditions at a glance.                                     | Basic snowpack trends and visual cues for conditions.                                                   | 1. **Monitor Snowpack Conditions**: Refresh a page to view visual cues indicating favorable or unfavorable snow conditions.                             |
| **Graduate Student (Juan)**            | Non-technical; focuses on concise summaries.                                                              | Simple summaries of snow stability and weather data.                                                | Snow stability, humidity, and temperature for Eastern Washington.                                       | 1. **Monitor Snowpack Conditions**: Access concise dashboards summarizing snow stability and weather, export summary for field planning.               |
| **Communications Staff (Tim)**         | Non-technical; experience with public communication.                                                      | A simple, regularly updated overview of snow accumulation.                                           | Areas with large snow accumulation, links to additional resources (e.g., Northwest Avalanche Center).    | 1. **Monitor Snowpack Conditions**: View snow accumulation updates, access external resources for public communication.                                 |
| **Busy Parent (Pav)**                  | Non-technical; needs immediate, easy-to-understand information.                                            | A single-click solution for checking snowboarding conditions.                                        | Quick decision aids for safe snowboarding trips.                                                        | 1. **Monitor Snowpack Conditions**: Access a simple dashboard for immediate safety and weather updates.                                                 |
| **Union Organizer (Ellen)**            | Data science background; experience interpreting longitudinal data.                                        | Tools for identifying high-impact strike times based on historical data and weather.                | Year-over-year traffic data, weather conditions, and historical patterns.                                | 1. **Analyze Snowplow and Traffic Data**: Access longitudinal data, combine traffic and weather information, export datasets for team collaboration.    |


