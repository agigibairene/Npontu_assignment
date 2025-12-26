from django.shortcuts import render
from django.views import View
import requests


def check_service(url):
    try:
        res = requests.get(url, timeout=5)
        return {
            "url": url,
            "status_code": res.status_code,
            "healthy": res.status_code == 200,
        }
    except:
        return {
            "url": url,
            "status_code": None,
            "healthy": False,
        }


class HealthCheck(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        url = request.POST.get("url")
        result = None

        if url:
            result = check_service(url)

        return render(request, "index.html", {
            "result": result
        })
