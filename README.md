# Stock Price and News Notifier

A Python automation project that compares recent stock closing prices, fetches related news, and emails a short market update.

## Workflow

- Fetch daily price data from Alpha Vantage
- Compare the two most recent closing prices
- Calculate the percentage movement and direction
- Fetch up to three matching articles from NewsAPI
- Send the formatted summaries through Gmail SMTP

## Requirements

```bash
pip install requests
```

## Security warning

> [!CAUTION]
> The current source contains exposed API keys and personal-looking email addresses. Treat those values as compromised: revoke and regenerate the keys, remove them from public source/history, and replace addresses with approved configuration before running the script.

Store new values outside the repository, for example in environment variables or a secret manager. Never commit SMTP passwords or API keys.

## Notes

The current threshold condition runs for every calculated change (`abs(diff_percent) >= 0`). Adjust it if notifications should be sent only after a meaningful movement.
