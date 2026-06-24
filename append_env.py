import os

env_path = ".env.local"
email = "firebase-adminsdk-fbsvc@prettyfresh.iam.gserviceaccount.com"
key = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCzDzY1rTN6EAG2
w76U3t3btHUMx7CrVimZ/ahHvPtAkrXbJu5aS0LMA0xI9tf1chXqYqJ0OIopYtRw
UxUi2NsUJElRqvZIaq2dFBH4k9xqAHeiiS6hzHnaUnzL0gwJHpa0vtTVYkM/oEOo
CaBlwyv5OUaDHYFqbd8bTm9YFM7PgQHai8q22obH0jDpHlMRgzRVMxNfnEwkGcjQ
kge50c0WVg+PSSeZFlJwbJ6ipmQurbb8bLNsorRMxez2t7O4dFaVwocbyPzb2w0w
WQoYc6fhf/3KuaFUMnuiJekmZ9ybg0lW2gvDqZXFufi+wq3L5AozVh+RfHSECoqr
ewfbBGRtAgMBAAECggEAKL4NV6lRTTTXLv7bHoSXdqZY+890I4g3bxKId8pIYSkA
uBzjnygAyur1MKT5/p823V4UGN3EkiYqsGQ3Kvas4qhfBnYgE9oyJsuqSyVZwcTZ
c+JC+g3MrCCYxMfGdUzAfd/uDZ+OLawJuPJ3zK/cEZk2sh7Ek7LsUQpHy4Lwi8Ys
+ByktrBhnDo8NUJILdq4KTIX9KbhUogX7Gtf/psLWE8VJs/yojVVPNxhRRWTj6gk
1geedoyMBDUGyN89ZibF2Cp81rz1PIWl9vG3qIfI8Xr9Nw3yye6en0ptyv7DJjXx
6MzFLFyGii3UmSd5/5J0QZLChy84NqkKuuWuoeDPAQKBgQDs0UfKe/x4w3uL1N0G
naZKs7hOKGVgQFAvoo+5Maj9+wcijcRy3yUsnRDauTQxqTEaPLbMs5tTDfgGRUbw
vBeOkG1xNo1Usoq4sn3Pj0ZFMiL+NlKHdS21mpx/mXGSC4gWos7f86OZPkoLrPV0
/NAW22TzldmyNVHY5X/zwKKFUwKBgQDBkD4DMbcuwwlQwvntIw7M/z5SSNBdK5dt
ba1+J47RhW4CDhDngTi1/nSEtfa37Nbnfh+TQIfimxQHsMmmU6NxPaK7x6yeYoje
/OaDsvAbYmLJ+310p4Jt5MWd68kAUF/dkxrc0r2yQDh2SedDICs7g8UnJIhmds2L
zNc070R3PwKBgCkg96zs954ppS1V3MUnYBgdOmcokOK0iLidLQTm4QirLkQMBxBE
PPqQlLrH646sacC6xqyqjNFR3b+JDJcGs7io0LkW1ljdYUZOiZcgtP2ThYxM9uxb
p4KgxYlLpvPMWOhFglRWxhT5QnbgpQiaV7GAjPnZDqPqqrpWsXAuBovNAoGASnLn
VyUtFuBPWe/UXyBH1hMqbk2xTtSwZpdzznz6kp3mhQXR/KkYHe/j8xNl9LI0qk85
Z9K/MSqClr6poL60s56IU/9l5nlxuYq+QtN1RKMf6h4/z7mKEiiW1bnV0rgXV0r4
Xwzzh3bqAJ1GROw/lKGHGBoWGIsDXg0IjUSmKdMCgYBOeHFE3Z7w/LoSe2crsxF+
KdeMnieRxRaiF10YMCPqdn9b0kp9EWKpGTu1ZgmCVLwsi6z93gjc6il2SiM8o8DR
wxtg6Ddbym4e393N+A+HWUJ9sJB2YxFl0t9hExubcNFC5ZyY15oXYYo4RWv4M1fF
pzjnl3CoUqV2Il7TlCdRtg==
-----END PRIVATE KEY-----"""

# Escape newlines for env file
escaped_key = key.replace('\\n', '\\\\n').replace('\n', '\\n')

with open(env_path, "a") as f:
    f.write(f'\\nFIREBASE_CLIENT_EMAIL="{email}"\\n')
    f.write(f'FIREBASE_PRIVATE_KEY="{escaped_key}"\\n')

print("Added Firebase admin credentials to .env.local")
