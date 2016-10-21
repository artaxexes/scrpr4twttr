val tts = MongoSpark.load(sc)
val rtts = rdd.filter(doc => doc.getInteger("retweet_count") >= 1)
