# Weekly Sales Report Emailer

A Python script that sends a weekly sales report as an HTML email through Gmail. The report is a table of orders and revenue (KES) for Nairobi and Mombasa.

## Setup

1. Install the package: `pip install python-dotenv`
2. Turn on 2-Step Verification in your Google account, then create an app password at myaccount.google.com/apppasswords.
3. Create a `.env` file in the project folder (no quotes, no spaces):

```
GMAIL_ADDRESS=youraddress@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop
```

4. Add `.env` and `__pycache__/` to `.gitignore` so your password is never uploaded.

## Usage

Edit the last line of `send_report.py` with the full recipient address and your real numbers:

```python
send_html_report("recipient@example.com", {"nairobi_orders": 120, "nairobi_revenue": 485000, "mombasa_orders": 85, "mombasa_revenue": 312500})
```

Run it:

```
python send_report.py
```

## Notes

- Don't name your script `email.py`. It clashes with Python's built-in `email` package.
- The recipient must be a full email address, including the `@` and domain.