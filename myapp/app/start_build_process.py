import asyncio
from myapp.app.build_start import build_start
from time import perf_counter

from django.shortcuts import render


def start_build_process(request):
    start_time = perf_counter()
    
   
    context = asyncio.run(build_start(request))

    end_time = perf_counter()
    
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
    
    return render(request,'list.html')