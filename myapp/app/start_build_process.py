import asyncio
from myapp.app.build.build_start import build_start
from time import perf_counter

from django.shortcuts import redirect, render


def start_build_process(request):
    start_time = perf_counter()
    
   
    asyncio.run(build_start(request))

    end_time = perf_counter()
    
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
    
    return redirect('my-view') #render(request,'list.html')