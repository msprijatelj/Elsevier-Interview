# Safe Harbor De-Identification


```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "birthDate": "2000-01-01",
    "zipCode": "10013",
    "admissionDate": "2019-03-12",
    "dischargeDate": "2019-03-14",
    "notes": "Patient with ssn 123-45-6789 previously presented under different ssn"
}' \
  http://127.0.0.1:5000/
```
