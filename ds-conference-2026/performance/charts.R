# ------------------------------------------------------------------------------
# Build the two performance figures for the EOS 257 deck from the measured
# dsBase 6.3.6 vs 7.0 results.  Outputs themed PNGs into public/.
#
#   Rscript charts.R      # run from eos/sprint-257/
#
# Data: data/perf_comparison.csv  (columns: label, "dsBase 6.3.6", "dsBase 7.0",
# speedup).  To add ds.colnames once you have a valid value, append a row to that
# CSV and remove "ds.colnames" from EXCLUDE below.
# ------------------------------------------------------------------------------

suppressPackageStartupMessages({ library(ggplot2); library(cowplot) })

# --- Editable headline numbers (graph i) -------------------------------------
N_REFACTORED <- 29    # ds.* functions refactored in PR #661 (batch 2)
N_TOTAL      <- 123   # total ds.* functions in dsBaseClient
EXCLUDE      <- character(0)   # ds.colnames carries an estimated 2.4x (NA rates):
                               # its 6.3.6-vs-7.0 measurement is invalid because the
                               # clientside-checks refactor already shipped in 6.3.5/6.3.6.

# --- Theme palette (matches theme/styles/index.css) --------------------------
PRIMARY <- "#4285F4"; ACCENT <- "#0097A7"; GREY <- "#D9D9D9"; TEXT <- "#333333"
ORIG <- "#9AA0A6"   # mid-grey for the "original" (6.3.6) bars

dir.create("public", showWarnings = FALSE)

# --- Load + tidy -------------------------------------------------------------
d <- read.csv("data/perf_comparison.csv", check.names = FALSE, stringsAsFactors = FALSE)
names(d) <- c("label", "v636", "v70", "speedup")
d$fn <- sub(" .*$", "", d$label)              # strip " (combine:0)" -> "ds.abs"
d <- d[!d$fn %in% EXCLUDE, ]
d <- d[order(d$speedup), ]                      # ascending so coord_flip = desc

stats <- c(mean = mean(d$speedup), median = median(d$speedup), max = max(d$speedup))
message(sprintf("n=%d  mean=%.2f  median=%.2f  max=%.2f", nrow(d), stats[1], stats[2], stats[3]))

# --- (ii) Speed-up bar chart -------------------------------------------------
d$fn <- factor(d$fn, levels = d$fn)
bars <- ggplot(d, aes(x = fn, y = speedup)) +
  geom_hline(yintercept = 1, linetype = "dashed", colour = GREY, linewidth = 0.6) +
  geom_col(fill = PRIMARY, width = 0.72) +
  geom_text(aes(label = sprintf("%.1f×", speedup)),
            hjust = -0.15, size = 4.0, colour = TEXT) +
  annotate("text", x = 1, y = 1, label = "no change", angle = 90,
           vjust = -0.5, hjust = 0, size = 3.0, colour = "#999999") +
  coord_flip(clip = "off") +
  scale_y_continuous(expand = expansion(mult = c(0, 0.12))) +
  labs(x = NULL, y = "Speed-up (7.0 ÷ 6.3.6)") +
  theme_minimal(base_size = 14) +
  theme(panel.grid.major.y = element_blank(),
        panel.grid.minor = element_blank(),
        axis.text = element_text(colour = TEXT),
        axis.title.x = element_text(colour = TEXT, margin = margin(t = 8)),
        plot.margin = margin(8, 22, 4, 8))

# Stats strip baked UNDERNEATH the bars: mean / median / max as headline figures.
strip_df <- data.frame(
  x   = 1:3,
  num = sprintf("%.1f×", c(stats["mean"], stats["median"], stats["max"])),
  lab = c("mean", "median", "max"))
strip <- ggplot(strip_df, aes(x = x)) +
  geom_text(aes(y = 1.00, label = num), size = 13, fontface = "bold", colour = PRIMARY) +
  geom_text(aes(y = 0.30, label = lab), size = 5.2, colour = TEXT) +
  scale_x_continuous(limits = c(0.5, 3.5), expand = c(0, 0)) +
  scale_y_continuous(limits = c(0, 1.5), expand = c(0, 0)) +
  theme_void() +
  theme(plot.margin = margin(2, 8, 6, 8))

combined <- plot_grid(bars, strip, ncol = 1, rel_heights = c(0.84, 0.16))
ggsave("public/speedups.png", combined, width = 7.4, height = 8.4, dpi = 150, bg = "white")

# --- (iii) Original vs refactored absolute rates (grouped bars) ---------------
# One pair of bars per function: original (6.3.6) speed and refactored (7.0) speed,
# in calls/second.  ds.colnames is dropped here (its rates are estimated, not
# measured).  Keeps the speed-up ordering so the biggest wins sit at the top.
r <- d[!is.na(d$v636) & !is.na(d$v70), c("fn", "v636", "v70")]
long <- data.frame(
  fn      = factor(rep(r$fn, 2), levels = r$fn),
  version = factor(rep(c("6.3.6 (original)", "7.0 (refactored)"), each = nrow(r)),
                   levels = c("6.3.6 (original)", "7.0 (refactored)")),
  rate    = c(r$v636, r$v70))
grp <- ggplot(long, aes(x = fn, y = rate, fill = version)) +
  # reverse = TRUE so within each pair the ORIGINAL bar sits on top, refactored below
  geom_col(position = position_dodge2(reverse = TRUE, padding = 0.12), width = 0.72) +
  coord_flip() +
  scale_fill_manual(values = c("6.3.6 (original)" = ORIG, "7.0 (refactored)" = PRIMARY)) +
  scale_y_continuous(expand = expansion(mult = c(0, 0.06))) +
  labs(x = NULL, y = "Calls / second", fill = NULL) +
  theme_minimal(base_size = 18) +
  theme(panel.grid.major.y = element_blank(),
        panel.grid.minor = element_blank(),
        legend.position = "top",
        legend.text = element_text(size = 18, colour = TEXT),
        legend.key.size = unit(1.1, "lines"),
        axis.text.y = element_text(colour = TEXT, size = 15),
        axis.text.x = element_text(colour = TEXT, size = 15),
        axis.title.x = element_text(colour = TEXT, size = 24, face = "bold",
                                    margin = margin(t = 10)),
        plot.margin = margin(8, 18, 8, 8))
ggsave("public/rates_compare.png", grp, width = 11.0, height = 7.4, dpi = 150, bg = "white")

# Same data, ordered biggest-win-first, for the animated <RatesBars /> component.
j <- d[!is.na(d$v636) & !is.na(d$v70), c("fn", "v636", "v70", "speedup")]
j <- j[order(-j$speedup), ]
rows <- sprintf('  {"name": "%s", "original": %.4f, "refactored": %.4f}',
                j$fn, j$v636, j$v70)
writeLines(c("[", paste(rows, collapse = ",\n"), "]"), "data/rates.json")
message("wrote data/rates.json (", nrow(j), " functions)")

# Improvement summary over the SAME functions shown in the bar chart (excludes
# ds.colnames), for the <PerfStats /> panel beside it.
sm <- j$speedup
writeLines(sprintf('{"mean": %.4f, "median": %.4f, "max": %.4f}',
                   mean(sm), median(sm), max(sm)), "data/perf_summary.json")
message(sprintf("wrote data/perf_summary.json (mean=%.2f median=%.2f max=%.2f)",
                mean(sm), median(sm), max(sm)))

# --- (i) Functions-refactored donut ------------------------------------------
donut <- data.frame(
  grp = c("Refactored", "Remaining"),
  n   = c(N_REFACTORED, N_TOTAL - N_REFACTORED))
donut$grp <- factor(donut$grp, levels = c("Remaining", "Refactored"))
pct <- round(100 * N_REFACTORED / N_TOTAL)
ref <- ggplot(donut, aes(x = 2, y = n, fill = grp)) +
  geom_col(width = 1, colour = "white") +
  coord_polar(theta = "y") +
  xlim(0.5, 2.5) +
  scale_fill_manual(values = c(Refactored = PRIMARY, Remaining = GREY), guide = "none") +
  annotate("text", x = 0.5, y = 0, label = sprintf("%d / %d", N_REFACTORED, N_TOTAL),
           size = 12, fontface = "bold", colour = PRIMARY) +
  annotate("text", x = 0.5, y = 0, label = sprintf("\n\n\n%d%% refactored", pct),
           size = 5, colour = TEXT) +
  theme_void()
ggsave("public/refactored.png", ref, width = 5.2, height = 5.2, dpi = 150, bg = "white")

message("wrote public/speedups.png and public/refactored.png")
