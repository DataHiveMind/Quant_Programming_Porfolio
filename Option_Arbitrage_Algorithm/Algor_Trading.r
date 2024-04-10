
# Install the necessary packages
install.packages("quantstrat", repos = "https://R-Forge.R-project.org")
install.packages("zoo")
install.packages("TTR", repos = "https://R-Forge.R-project.org")
install.packages("Defualts")
install.packages("devtools")
install.packages("quantmod")
require(quantstrat)
require(devtools)
install_github(repo = "IKtrading", username - "Ilyakipins")
install_github(repo = "DSTrading", username = "Ilyakipins")
require(IKtrading)
require(DSTrading)

# Load the data
options("getSymbols.warning4.0" = FALSE)
rm(list = ls(.blotter), envir=.blotter)
currency("USD")
Sys.setenv(TZ = "UTC")
symbols <- "SPY"
suppessmessages(getSymbols(symbols, from ="1998-01-01", to = "2012-31-01"))
stock(symbols, currency = "USD", multiplier = 1)
initDate <- "1998-01-01"

