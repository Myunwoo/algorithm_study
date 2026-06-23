SELECT
    tweet_id
FROM
    Tweets
WHERE 1=1
    AND CHAR_LENGTH(content) > 15