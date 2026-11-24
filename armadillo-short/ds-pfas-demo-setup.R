####################################################################################################
# Packages
####################################################################################################
# install.packages(c("tidyverse", "MolgenisArmadillo"), repos = "https://cloud.r-project.org")
library(MolgenisArmadillo)
library(tidyverse)

####################################################################################################
# Simulate three sites
# Random data, not real patients. Each participant has a serum PFAS concentration (ng/mL) and a
# kidney cancer status. The odds of kidney cancer rise by 42% (log odds 0.35) for each doubling of PFAS.
# Each site has 0/1 cohort indicators, so the pooled model can include a fixed effect of
# cohort and a PFAS effect for each cohort.
####################################################################################################
simulate_site <- function(n, seed, cohort) {
  set.seed(seed)
  sex <- factor(sample(c("Male", "Female"), n, replace = TRUE, prob = c(0.55, 0.45)))
  smoking <- factor(
    sample(c("Never", "Former", "Current"), n, replace = TRUE, prob = c(0.45, 0.35, 0.2)),
    levels = c("Never", "Former", "Current")
  )
  age <- round(pmin(pmax(rnorm(n, 62, 10), 35), 90))
  bmi <- round(rnorm(n, 27, 4.5), 1)
  log2_pfas <- rnorm(n, log2(4), 0.9)

  log_odds <- -5 + 0.35 * log2_pfas + 0.03 * age + 0.5 * (sex == "Male") +
    0.3 * (smoking == "Former") + 0.6 * (smoking == "Current") + 0.04 * bmi
  kidney_cancer <- rbinom(n, 1, plogis(log_odds))

  tibble(
    kidney_cancer, pfas = round(2^log2_pfas, 2), log2_pfas = round(log2_pfas, 3), age, sex, smoking, bmi,
    cohort_groningen = as.integer(cohort == "groningen"),
    cohort_amsterdam = as.integer(cohort == "amsterdam"),
    cohort_barcelona = as.integer(cohort == "barcelona")
  )
}

site_1 <- simulate_site(n = 420, seed = 101, cohort = "groningen")
site_2 <- simulate_site(n = 260, seed = 202, cohort = "amsterdam")
site_3 <- simulate_site(n = 340, seed = 303, cohort = "barcelona")

####################################################################################################
# Upload to Armadillo
####################################################################################################
url <- "http://localhost:8080"

armadillo.login(url)
armadillo.delete_project("uncan")
armadillo.create_project("uncan")
armadillo.upload_table("uncan", "data", site_1, "site_1")
armadillo.upload_table("uncan", "data", site_2, "site_2")
armadillo.upload_table("uncan", "data", site_3, "site_3")
