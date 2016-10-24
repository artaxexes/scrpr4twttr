/*
 *
 * ./spark-shell --conf "spark.mongodb.input.uri=mongodb://127.0.0.1/twitter.tweets?readPreference=primaryPreferred" --conf "spark.mongodb.output.uri=mongodb://127.0.0.1/twitter.tweets" --packages org.mongodb.spark:mongo-spark-connector_2.11:2.0.0-rc0
 *
 * import com.mongodb.spark._
 * val tts = MongoSpark.load(sc)
 * val rtts = rdd.filter(doc => doc.getInteger("retweet_count") >= 1)
 *
 */
