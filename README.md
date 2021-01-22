# Safe Harbor De-Identification

Python3.7 is recommended to run this code.  To install & deploy, run `make all` in your terminal environment; this will set up a virtual Python environment, install the relevant Python packages, and locally deploy the API endpoint.  The endpoint can then be tested via POST request to the API endpoint described by the app (default `http://127.0.0.1:5000`).  This can be done via a cURL command in another terminal window, or through the API request framework of your choice.  For example, to test using the sample payload given in the original problem's README, copy/paste the below cURL command into your terminal environment.

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "birthDate": "2000-01-01",
    "zipCode": "10013",
    "admissionDate": "2019-03-12",
    "dischargeDate": "2019-03-14",
    "notes": "Patient with ssn 123-45-6789 previously presented under different ssn, email abc@xyz.com. Phone number 555-123-4567."
  }' \
  http://127.0.0.1:5000/
```
## Rules Implemented
The rules implemented include the following:
* Birth date to age
* Zip Code stripped to first 3 digits or converted to "00000"
* Admission and Discharge dates converted to years only
* Redaction of email, US phone number, and SSN from notes

I have omitted the redaction of dates within the `notes` field for this submission due to lack of time.  Were I to attempt to implement the detection and redaction of dates, I would likely rely upon a third-party package to detect all of the potential date formats before writing my own code to redact any detected dates.


## Feedback
Solution was solid, but these regions need improvement:
* Improve error handling
* Issue with opening/closing the zip code file with every request (read it into existence once)
