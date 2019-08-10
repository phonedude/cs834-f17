ncdg10 <- read.csv("ndcg10.csv", header = TRUE)
plot(ncdg10$Query,ncdg10$Value,type = "o",col = "red", xlab = "Query Index", ylab = "NCDG10", 
     main = "NCDG10 for CACM Query Set",  ylim=c(0,1))