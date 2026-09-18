# Armadillo UNCAN demo

| Time | Line |
| --- | --- |
| 0:01.0 | In this presentation, we're going to show how our UncanConnect data can be analysed using Federated Analysis. Federated Analysis is the remote analysis of data which combines multiple data sources in one model. |
| 0:14.4 | With Federated Analysis, code travels, not the data — each site runs the computation locally, on its own data. |
| 0:22.8 | Only the summary statistics are returned to the researchers; anything that could disclose or recreate individual-level data is blocked. |
| 0:31.1 | We're going to demonstrate two parts of the UncanConnect software stack: Armadillo, a server application to manage data access, and DataSHIELD, a federated framework to analyse data. |
| 0:43.6 | How does Federated Analysis work? Here you see an example with three cohorts. |
| 0:49.9 | Each data owner installs Armadillo locally, |
| 0:53.3 | and uploads a portion of their data to make it available for analysis. |
| 0:57.6 | A researcher then requests access to the data via the negotiation process shown before, |
| 1:03.0 | and once granted, they receive credentials to log into a central portal. |
| 1:07.7 | From here they can conduct analysis across the three cohorts, receiving summary statistics, such as means, standard deviations and model parameters. We're going to show how this works first from the data manager perspective. |
| 1:23.7 | Here we see the login page for Armadillo, |
| 1:26.8 | and you can click via institutional login and log in via the Life Sciences Authentication and Authorization Infrastructure, or LS AAI, using our institution, Groningen. |
| 1:38.3 | This takes you to the Armadillo landing page. |
| 1:42.8 | On this landing page you can already see that one project has been created, called UncanConnect, and this just contains synthetic data. |
| 1:51.1 | We can explore this project here, |
| 1:54.0 | opening the folder and the file, |
| 1:56.6 | and see a preview of the data that's been uploaded |
| 2:00.3 | Here we just have one table as a simplified example. We can also go to the metadata preview |
| 2:06.9 | and see more details on each of these columns: what the data type is, and also what the level of missing data is. |
| 2:17.5 | Now, once the researcher has completed the negotiation process, the data manager needs to give the researcher access to the data. They will be provided a link, which once clicked, takes them to a project approval page in Armadillo. |
| 2:32.6 | Here they can see an overview of the project that's been requested, the researcher that has requested access, and a list of the individual variables the researcher has requested. |
| 2:43.0 | In this simplified example the researcher has requested 5 variables: quality of life, age at diagnosis, and some information about chemotherapy outcomes. |
| 2:53.7 | To approve the request, the data manager clicks the approve button, |
| 2:57.8 | and then they are shown a confirmation message. |
| 3:01.3 | Now if we navigate to the projects page we can see what's been created — a new project called "Project 1". |
| 3:09.1 | This contains a subset of the data for this project, and we also see that a.researcher@umcg.nl has been granted access to this project via DataSHIELD. |
| 3:19.5 | If we click on this like before, we can see a table with just five columns: the subset based on the agreed variables from the negotiation process. |
| 3:29.0 | This data is now available for this researcher to analyse via DataSHIELD. |
| 3:35.3 | Now, what does it look like from the researcher perspective? Once the researcher has been through the negotiation process and has been granted access to the data, they can conduct their analysis using RStudio. |
| 3:49.0 | First of all they need to enter a few details, like the URLs of the remote servers. |
| 3:54.5 | Next they run a command to request access tokens. |
| 3:58.2 | A browser window will be opened, |
| 4:00.6 | as before, we use life sciences authentication to log in via the institution and get access tokens for each of the cohort. |
| 4:08.0 | Once these access tokens have been received they can be used to build a login object, |
| 4:13.1 | and then with this the researcher can log into a DataSHIELD session. |
| 4:17.8 | It takes a few seconds, and then we receive confirmation that we are logged in and that the data is available to be used. |
| 4:25.7 | Now we are logged in we can interact with the data. However, remember that with federated analysis we can never see the data itself. |
| 4:35.2 | We can, however, view summaries of the data. For example, we can return column names, |
| 4:41.2 | and see it matches the variables we were given access to through negotiator. |
| 4:46.6 | We can also explore the distribution of the data, for example the quality of life variable. |
| 4:52.0 | Here we produce histograms for each of the three cohorts. |
| 4:57.3 | We can also look at tabular data. |
| 5:00.1 | In this example we can see counts of different chemotherapy outcomes per study. |
| 5:06.8 | Finally, we can fit a regression model to understand whether starting quality of life is associated with lower dropout for chemotherapy, or fewer treatment modifications. |
| 5:17.0 | This gives a table of estimates for each cohort, and the combined estimate across all cohorts. |
| 5:23.3 | We can also take these estimates and make a forest plot to visualise the associations. |
| 5:28.6 | This is run with synthetic data, but illustrates in this example that higher quality of life is associated with lower chemotherapy discontinuation. In this demo we have seen how we can go from variable discovery through to access and analysis — with no participant data ever leaving the participating studies. |
