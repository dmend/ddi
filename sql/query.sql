SELECT v.VULN_ID, p.PAGE_ID, v.data FROM (
    SELECT * FROM websites WHERE url LIKE '%foo.com'
) AS w
    JOIN (
        SELECT * FROM pages WHERE path LIKE '%login.html'
) AS p ON w.WEBSITE_ID=p.WEBSITE_ID
    JOIN vulnerabilities v ON p.PAGE_ID=v.PAGE_ID;
