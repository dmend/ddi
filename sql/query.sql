SELECT v.VULN_ID, p.PAGE_ID, v.data FROM websites w
    JOIN pages p on w.WEBSITE_ID=p.WEBSITE_ID AND w.url LIKE '%foo.com'
    JOIN vulnerabilities v ON p.PAGE_ID=v.PAGE_ID AND p.path LIKE '%login.html';
