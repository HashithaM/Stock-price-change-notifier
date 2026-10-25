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

## Configuration

The script requires five environment variables and fails before network access if any is missing:

- `ALPHA_VANTAGE_API_KEY`
- `NEWS_API_KEY`
- `SMTP_USER`
- `SMTP_PASSWORD`
- `NOTIFICATION_RECIPIENT`

Copy the dummy names from `.env.example` into your own private environment. The script does not automatically load `.env`, and `.env` is ignored by Git.

> [!IMPORTANT]
> Revoke and regenerate any key that appeared in an earlier public revision. Replacing the current source does not invalidate exposed credentials or erase Git history.

## Notes

The current threshold condition runs for every calculated change (`abs(diff_percent) >= 0`). Adjust it if notifications should be sent only after a meaningful movement.
