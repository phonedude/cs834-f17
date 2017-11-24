query_merge <- read.csv("QueryMerge.csv", header = TRUE)
query2 <- read.csv("Interpolated_query2.csv", header = TRUE)
query1 <- read.csv("Interpolated_query1.csv", header = TRUE)

query1$Recall
plot(query_merge$Recall, query_merge$Precision,xlab = "Recall", ylab = "Precision",ylim=c(0,1)
     ,main = "Recall vs Precision Graph", pch=22, col = query_merge$Type)

lines(query1$Recall,query1$Precision,type = "o",col = "black", pch = 22, lty = 1)
lines(query2$Recall,query2$Precision,type = "o",col = "red", pch = 22 ,lty = 2)

legend("bottomright", c("Query1","Query2"), col=c("black", "red"),pch=22, lty=1:2)