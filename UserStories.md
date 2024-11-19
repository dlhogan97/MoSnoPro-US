
# User Stories for MoSnoPro-US Project

## 1. Data Analyst

**Alex** is a data analyst at a transportation agency. He uses data on snowfall and its impact on road conditions to generate reports for decision-makers. Alex wants an application that simplifies filtering, visualizing, and extracting key patterns from large datasets, such as snowplow performance and accident trends. He has moderate programming skills and prefers an interface with intuitive controls and minimal setup. His primary need is interactive dashboards that help him explore correlations and export visuals for reports.

---

## 2. Graduate Student in Transportation Engineering

**Maria** is a graduate student researching the impact of snowstorms on road safety and traffic flow. She works with datasets from sensors and weather reports to develop insights for winter road maintenance strategies. Maria has basic programming experience and needs a tool that allows her to upload and analyze datasets quickly. She values interactive visualizations, such as time-series data of road conditions, and would like features that suggest possible interventions for safer winter roads.

---

## 3. Traffic Engineer

**James** is a traffic engineer responsible for ensuring road safety and maintaining traffic flow during snow events. He uses weather and traffic data to evaluate snowplow schedules, salt usage, and accident hotspots. James is not familiar with programming and relies on user-friendly software to analyze data. He needs an application that provides clear, actionable insights into road conditions, such as snowplow activity and accident trends, and allows for easy report generation to communicate with decision-makers.

---

## 4. Software Developer

**Priya** is a software developer maintaining a suite of tools for transportation analytics. She integrates weather and traffic data to create applications for snow management systems. Priya is proficient in Python and APIs, but she’s not an expert in transportation engineering. She needs a tool with a well-documented programming interface, allowing her to customize and integrate the MoSnoPro-US features into existing systems. She values flexibility, scalability, and ease of debugging when working with large datasets, such as traffic incidents during snowstorms.

---

## 5. Decision Maker/Manager

**Ethan** is a senior manager at a state department of transportation. He oversees resource allocation for snowplow operations and winter road maintenance. Ethan is not technical and relies on summary dashboards and visualizations to guide his decisions. He needs an application that provides key insights, such as snowplow coverage, road condition trends, and cost-efficiency metrics. The ability to quickly export visuals to presentation-ready formats like PDF or Excel is crucial for communicating with stakeholders and securing funding.

---
# Functional Specification for MoSnoPro-US

| User                                           | Knowledge                                                                                                           | Needs                                                                                                                 | Information Users Want                                                                                                                                                         | Use Cases                                                                                                                                                                                                                                  |
|:-----------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Analyst                                   | Intermediate data analysis skills, moderate programming experience (Python, Pandas, basic visualization libraries). | Tools to explore snow-related transportation data and generate visualizations with minimal technical setup.           | Insights into correlations between snowfall intensity, snowplow activity, and traffic incidents. Interactive filtering and plotting of traffic, weather, and maintenance data. | Upload datasets via a web interface. Apply filters (e.g., date ranges, location) and visualize trends in traffic and snowplow data. Export graphs for reports.                                                                             |
| Graduate Student in Transportation Engineering | Basic programming and a solid understanding of traffic and weather data analysis.                                   | Intuitive features to upload and analyze datasets, produce visualizations, and test hypotheses for academic research. | Visualized trends in road conditions during snowstorms. Impact of maintenance strategies on road safety and traffic flow.                                                      | Explore accident data during snow events using interactive plots. Test the impact of various interventions using simulation tools (if available). Save findings for inclusion in academic papers or presentations.                         |
| Traffic Engineer                               | Deep domain expertise in transportation and road safety but limited programming or technical knowledge.             | A user-friendly system to evaluate road conditions, snowplow performance, and accident trends without coding.         | Accident hotspots and their correlation with snowfall and road conditions. Snowplow route efficiency and resource usage summaries.                                             | View dashboards summarizing real-time or historical road conditions. Identify problem areas or inefficiencies in snowplow operations. Generate PDF reports for internal reviews.                                                           |
| Software Developer                             | Advanced programming skills in Python, APIs, and database management; less expertise in transportation concepts.    | A well-documented programming interface to integrate MoSnoPro-US with other systems or extend its functionality.      | APIs for querying transportation and weather data. Code samples for extending or embedding functionalities into other tools.                                                   | Query the system using provided APIs to access datasets programmatically. Customize visualizations or add features based on specific project requirements. Debug integration issues using the system’s documentation.                      |
| Decision Maker/Manager                         | Minimal technical expertise, focuses on high-level insights and resource management decisions.                      | Clean, easy-to-understand dashboards summarizing road safety, snowplow operations, and budgetary efficiency.          | Visual summaries of snowplow coverage, road safety metrics, and cost breakdowns. Downloadable reports for presentations or meetings.                                           | Open pre-designed dashboards to view high-level summaries (e.g., cost vs. coverage of snowplow operations). Export charts and insights to share with stakeholders. Make informed decisions on budget allocation and resource distribution. |
