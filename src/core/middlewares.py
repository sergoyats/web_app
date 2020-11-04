from time import perf_counter
from datetime import datetime
import cProfile
from django.conf import settings
import pstats
from io import StringIO


class PerformanceMonitoringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # self.pr = cProfile.Profile()
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        pr = cProfile.Profile()
        start = perf_counter()
        pr.enable()  # start profiling
        response = self.get_response(request)
        pr.disable()
        finish = perf_counter()

        if finish - start > settings.MAX_RESPONSE_TIME:
            s = StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
            ps.print_stats(settings.LOG_RECORDS_COUNT)

            with open(f'{datetime.today().strftime("%Y-%m-%d")}_performance.log', 'a') as f:
                f.write(f'TIME: {datetime.now().time()} \n')
                f.write(f'URI: {request.path} \n')
                f.write(f'METHOD: {request.method}\n')
                if request.GET:
                    f.write(f'GET: {request.GET}\n')
                if request.POST:
                    f.write(f'POST: {request.POST}\n')

                f.write(f'DEBUG INFO: {s.getvalue()} \n')
                f.write('-' * 20 + '\n')

        # Code to be executed for each request/response after
        # the view is called.

        return response
