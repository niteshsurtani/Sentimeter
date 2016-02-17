from review_crawler_flipkart import extractReviews
from process_reviews import processReviews
from benchmark import doBenchmark

print "Starting Engine ..."

extractReviews()
print "Reviews extracted from Flipkart."

processReviews()
print "Reviews processed and stored."

doBenchmark()
