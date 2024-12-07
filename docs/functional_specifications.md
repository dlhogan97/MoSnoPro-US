# Functional Specificaiton
## Background
Avalanche forecasts rely on an accurate understanding of internal snowpack properties (temperature, density, etc.) to effectively communicate hazards to transportation and recreation in mountain environments. However, observations of internal snowpack properties are relatively few and far between since they require avalanche professionals to go into the field to take measurements. MoSnoPro-US offers a solution by providing estimates important snowpack properties in an accessible format. The tool provides near-real time model results from a physically-based 1-D snow model driven by remote weather observations. This provides a way to remotely "see" into the snowpack to track internal snowpack changes that are difficult to capture across a broad area. 

## User Profiles

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

## Data Sources
- Weather data acquired from select remote snow telemetry (SnoTel) stations throughout Washington located near major recreational areas. 
- Snow model output from pySUMMA, a physically-based 1-D snow model which provides output of internal snowpack properties.

# MoSnoPro-US Functional Specification

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


