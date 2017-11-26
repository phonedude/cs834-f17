map <- read.csv("map.csv", header = TRUE)
plot(map$Query,map$Value,type = "o",col = "red", xlab = "Query Index", ylab = "MAP", 
     main = "MAP for CACM Query Set",  ylim=c(0,1))

#legend("topright", c("Query1","Query2"), col=c("red","blue"),pch=21:22, lty=1:2)