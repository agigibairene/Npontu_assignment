import requests
import time
from django.http import JsonResponse

SERVICES = {
    "service_a": "https://jsonplaceholder.typicode.com/photos",
    "service_b": "https://jsonplaceholder.typicode.com/users",
    "service_c": "https://jsonplaceholder.typicode.com/todos",
}

TIMEOUT = 2  


def health_check(request):
    results = {}
    overall_status = "healthy"

    for name, url in SERVICES.items():
        start_time = time.time()
        try:
            response = requests.get(url, timeout=TIMEOUT)
            latency = round((time.time() - start_time) * 1000, 2)

            if response.status_code == 200:
                results[name] = {
                    "status": "up",
                    "latency_ms": latency
                }
            else:
                results[name] = {
                    "status": "down",
                    "latency_ms": latency
                }
                overall_status = "degraded"

        except requests.exceptions.RequestException:
            results[name] = {
                "status": "down",
                "latency_ms": None
            }
            overall_status = "degraded"

    return JsonResponse({
        "status": overall_status,
        "services": results
    })
