query <- read.csv("AverageInterpolation.csv", header = TRUE)
query1 <- read.csv("AverageInterpolationQuery1.csv", header = TRUE)
query2 <- read.csv("AverageInterpolationQuery2.csv", header = TRUE)

plot(query$Recall, query$Precision,xlab = "Recall", ylab = "Precision",ylim=c(0,1)
     ,main = "Average Recall-Precision graph using standard recall levels",type = "o", col = "red", pch = 21 ,lty = 1)

lines(query1$Recall,query1$Precision,type = "o",col = "black", pch = 22, lty = 2)
lines(query2$Recall,query2$Precision,type = "o",col = "green", pch = 23 ,lty = 3)

legend("bottomright", c("Query1","Average","Query2"), col=c("red","black", "green"),pch=21:23, lty=1:3)