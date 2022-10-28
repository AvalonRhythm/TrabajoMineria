import pandas as pd

df_review = pd.read_csv('data/yelp_reviews.csv')
print(df_review)

reviewsNeg = []
reviewsPos = []

for review in df_review.iloc:
    if review[3] == 1 or review[3] == 2:
        reviewsNeg.append(review)
    elif review[3] == 3 or review[3] == 4 or review[3] == 5:
        reviewsPos.append(review)

reviewsNeg = pd.DataFrame(reviewsNeg)
reviewsPos = pd.DataFrame(reviewsPos)

print(reviewsNeg)
print(reviewsPos)

reviewsNeg.to_csv("data/reviewsNeg.csv")
reviewsPos.to_csv("data/reviewsPos.csv")
