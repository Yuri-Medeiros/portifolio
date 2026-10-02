"""Generate the public contribution calendar during GitHub Pages deployment."""
import calendar
import datetime as dt
import json
import os
from pathlib import Path
import sys
import urllib.request


def query_range(now):
    year = now.year - 1
    start = now.replace(year=year, day=min(now.day, calendar.monthrange(year, now.month)[1]))
    return start.isoformat(), now.isoformat()


def fetch_calendar(token, now):
    start, end = query_range(now)
    query = '''query($login:String!, $from:DateTime!, $to:DateTime!) {
      user(login:$login) {
        contributionsCollection(from:$from, to:$to) {
          contributionCalendar {
            totalContributions
            weeks { contributionDays { date weekday contributionCount contributionLevel } }
          }
        }
      }
    }'''
    body = json.dumps({'query': query, 'variables': {'login': 'Yuri-Medeiros', 'from': start, 'to': end}}).encode()
    request = urllib.request.Request('https://api.github.com/graphql', data=body, headers={
        'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json',
        'User-Agent': 'Yuri-Portfolio-Contributions', 'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result.get('errors'):
        raise RuntimeError('; '.join(error.get('message', 'GraphQL error') for error in result['errors']))
    data = result.get('data', {}).get('user')
    if not data:
        raise RuntimeError('GitHub user not found')
    calendar_data = data['contributionsCollection']['contributionCalendar']
    if not calendar_data.get('weeks'):
        raise RuntimeError('GitHub returned an empty calendar')
    return {'available': True, 'username': 'Yuri-Medeiros', 'updatedAt': now.isoformat(),
            'from': start, 'to': end, **calendar_data}


def main():
    output = Path(sys.argv[1] if len(sys.argv) > 1 else 'assets/contributions.json')
    try:
        token = os.environ.get('GH_TOKEN')
        if not token:
            raise RuntimeError('GH_TOKEN is required in the deployment environment')
        data = fetch_calendar(token, dt.datetime.now(dt.timezone.utc).replace(microsecond=0))
    except Exception as error:
        print('::warning::Could not update GitHub contributions: ' + str(error), file=sys.stderr)
        if output.exists():
            return  # Preserve the last valid snapshot.
        data = {'available': False, 'username': 'Yuri-Medeiros'}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    print('Contribution data written to ' + str(output))


if __name__ == '__main__':
    main()
