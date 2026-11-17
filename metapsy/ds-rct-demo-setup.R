####################################################################################################
# Packages
####################################################################################################
# install.packages(c("HSAUR3", "synthpop", "tidyverse", "DSMolgenisArmadillo", "MolgenisArmadillo"))
library(DSMolgenisArmadillo)
library(MolgenisArmadillo)
library(HSAUR3)
library(synthpop)
library(tidyverse)

####################################################################################################
# Load the Beat the Blues trial
# Randomised trial of computerised CBT (Beat the Blues) versus treatment as usual in 100 people with
# depression. Outcome: Beck Depression Inventory (BDI) before treatment and at 2, 3, 5 and 8 months.
# Proudfoot et al. (2003) Psychological Medicine 33:217-227. Distributed with the HSAUR3 package.
####################################################################################################
data("BtheB")
trial <- as_tibble(BtheB)

####################################################################################################
# Make three simulated sites from the trial
####################################################################################################
site_1 <- syn(trial, k = 300, seed = 101)$syn
site_2 <- syn(trial, k = 300, seed = 202)$syn
site_3 <- syn(trial, k = 300, seed = 303)$syn

site_1$id <- seq_len(nrow(site_1))
site_2$id <- seq_len(nrow(site_2))
site_3$id <- seq_len(nrow(site_3))

####################################################################################################
# Long format: one row per participant and follow-up, for models of change over time
####################################################################################################
to_long <- function(site) {
  pivot_longer(
    site,
    cols = c(bdi.2m, bdi.3m, bdi.5m, bdi.8m),
    names_to = "month",
    names_pattern = "bdi\\.(\\d+)m",
    names_transform = as.integer,
    values_to = "bdi"
  )
}
site_1_long <- to_long(site_1)
site_2_long <- to_long(site_2)
site_3_long <- to_long(site_3)

####################################################################################################
# Upload to Armadillo
####################################################################################################
url <- "https://armadillo-playground.molgenis.net/"
url <- "https://armadillo-demo.molgenis.net/"
url <- "http://localhost:8080"

armadillo.login(url)
armadillo.delete_project("rct")
armadillo.create_project("rct")
armadillo.upload_table("rct", "data", site_1, "site_1")
armadillo.upload_table("rct", "data", site_2, "site_2")
armadillo.upload_table("rct", "data", site_3, "site_3")
armadillo.upload_table("rct", "data", site_1_long, "site_1_long")
armadillo.upload_table("rct", "data", site_2_long, "site_2_long")
armadillo.upload_table("rct", "data", site_3_long, "site_3_long")
armadillo.upload_table("rct", "data", as.data.frame(mtcars), "mtcars")
