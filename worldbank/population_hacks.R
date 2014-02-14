# load data
data<-read.csv('/Users/andrewjudson/GitHub/local/opendata/worldbank/population.csv')
str(data)
options(digits=10)
summary(data$yr_2012)
# plot with / without log scales
plot(data$yr_2012)
plot(log(data$yr_2012))