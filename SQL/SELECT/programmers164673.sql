SELECT
    ugb.TITLE,
    ugb.BOARD_ID,
    ugr.REPLY_ID,
    ugr.WRITER_ID,
    ugr.CONTENTS,
    DATE_FORMAT(ugr.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM
    USED_GOODS_BOARD as ugb
INNER JOIN
    USED_GOODS_REPLY as ugr
ON
    ugb.BOARD_ID = ugr.BOARD_ID
WHERE
    DATE_FORMAT(ugb.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY
    ugr.CREATED_DATE, ugb.TITLE;

# DATE_FORMAT(ugb.CREATED_DATE, '%Y-%m') = '2022-10'
# SUBSTR(ugb.CREATED_DATE,1,7)='2022-10'
    
