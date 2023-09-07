from django.shortcuts import render
from datetime import datetime
import pytz
from django.http import JsonResponse


# Create your views here.
def api_endpoint(request):
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track', '')
    current_day = datetime.now().strftime('%A')
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext",
    github_repo_url = "https://github.com/username/repo",
    status_code =  200
    
    response_data = {
        "slack_name": slack_name,
        "track": track,
        "current_day": current_day,
        "utc_time": utc_time,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code,
    }

    return JsonResponse(response_data)


# print(datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))