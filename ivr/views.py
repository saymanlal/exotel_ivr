from django.shortcuts import render
from django.http import HttpResponse

def start_call(request):
    response = """
    <Response>
        <Gather action="/ivr/gather/" method="POST" numDigits="1">
            <Say>
                Namaskar. Nayi complaint ke liye 1 dabayein.
                Purani complaint ke liye 2 dabayein.
            </Say>
        </Gather>
    </Response>
    """
    return HttpResponse(response, content_type="text/xml")


def gather(request):
    digit = request.POST.get("Digits")

    if digit == "1":
        response = """
        <Response>
            <Say>Aapne nayi complaint chuni hai.</Say>
        </Response>
        """
    elif digit == "2":
        response = """
        <Response>
            <Say>Aapne purani complaint chuni hai.</Say>
        </Response>
        """
    else:
        response = """
        <Response>
            <Say>Galat chayan. Dobara koshish karein.</Say>
            <Redirect>/ivr/start/</Redirect>
        </Response>
        """

    return HttpResponse(response, content_type="text/xml")
