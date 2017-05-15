INSERT INTO websites (Name, URL)
VALUES
    ('foo', 'http://foo.com'),
    ('bar', 'http://bar.com');

INSERT INTO pages (WEBSITE_ID, path)
VALUES
    (1, '/login.html'),
    (1, '/logout.html'),
    (1, '/admin.html'),
    (2, '/login.html'),
    (2, '/logout.html'),
    (2, '/admin.html');

INSERT INTO vulnerabilities (PAGE_ID, data)
VALUES
    (1, 'SQL injection response blah'),
    (1, 'XXE response'),
    (1, 'Stored XSS response'),
    (2, 'Session hijack'),
    (4, 'XXE response'),
    (6, 'Default credentials response');

