SELECT *
FROM COMMON t
         JOIN USER u ON t.UserID = u.UserID
         JOIN DOC d ON t.DataID = d.DataID
WHERE u.UserID <> 14
AND t.Timestamp > 1526040780000
ORDER BY t.Timestamp
LIMIT 501;