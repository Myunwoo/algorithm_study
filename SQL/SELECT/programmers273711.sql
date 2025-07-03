SELECT
    ITEM_ID, ITEM_NAME, RARITY
FROM
    ITEM_INFO
WHERE
    ITEM_ID IN (
        SELECT
            B.ITEM_ID
        FROM
            ITEM_INFO A, ITEM_TREE B
        WHERE
            A.RARITY = 'RARE'
            AND A.ITEM_ID = B.PARENT_ITEM_ID    
    )
ORDER BY
    ITEM_ID DESC