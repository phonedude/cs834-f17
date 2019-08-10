p10 <- read.csv("p10.csv", header = TRUE)
plot(p10$Query,p10$Value,type = "o",col = "red", xlab = "Query Index", ylab = "P10", 
     main = "P10 for CACM Query Set",  ylim=c(0,1))