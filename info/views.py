from django.shortcuts import render
from django.http import HttpResponse
from ipware import get_client_ip
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import gspread
import requests
import json

# Create your views here.

@api_view(['GET'])
@csrf_exempt
def get_form(request):

    cred = {
  "type": "service_account",
  "project_id": "portfolio-client-379113",
  "private_key_id": "fc26c6c4f23ff5a1e16a8288961418cd8a8a440d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC4jxIq7Sz5m6w+\nwj/JHcIRdSIic9hNHF8KGCfbd0XO9X1VeWk8LtVl0afYc4z72Ob03h/1J4/VTbW+\ndWS5Q12Z+h6hNuM3exWVFMbiVf6WemHO/UGoRVnvWU8HmI4HklqHiAsMCpOsMi4S\ngyodm0mPpmIzUAblVo3GwdzFUvhvFyV2jiL9iqc5MLqHzcAvHyojyf/wc2ij6lRa\nJU48R5vxMiHs/PtWWXBnDNQluMGO3Nqe1nwc4O7bKxBiPH8wZk6VAPDpb75sg1SS\nbcKNoVTZExpec14Nn/H/I/vqYYUywCU6Cm/LvechScXj8SP59Iomf2cd/hjvsuTi\nqHm0fMlfAgMBAAECggEABdIlXYs7duftB9Gyl1JD868BE5sZwFzbtoLKhwZ9AikF\n+fMpWYeUnXB+XbpPQQY3SpPS6DWGONEJoWcsdRdl1VxpKOaFRhOwu5H7L9pMfEyB\n1zhvoLIHQyBK+M9b82svRcUJrCiNPcobX+QZKPPj3w79W+bzQLp5IEKvBt42DbLc\neMWSxN/xtl275hx/BaPfryd3O337uc0D6mIqXmvuaRZ8apVoqwapkHQeO6S68FcA\ndi+zinS7y1lMV5MHE0IcJXCAXPquAwcQ4Mce0bVx3M+Ym2daYejoApWIEmVFhbDw\n9G5btJ5u9Ow/mIKncF2oHpKimyTprDEU4gD62Ccq+QKBgQDgXd/+ELvWV5zRHqy/\nNPH/YRy6r1C0RnTop0L7cCZfIMA+Y5AjXwwxxSq9uwJBYYB+Fqd54+y0sar4IKvN\nWe5buQqNZYlZKMN5tYVPpINYUZl1E/ZlsIz6E52tPZHL7d1U9iC5tyXxEx2wdcjQ\n/ZUi+iszzNt2f//y3R9CIQZRVQKBgQDSlGbc6X/ZotqZDO9Ss7fXCKJS4h15z28D\n/HEHy3kxSzGr60oCpAhvKubVLUmQROZbJXRGceQ4K5go/eWTdXhk26JxNALCMGtG\nwak1/0D3LAQu47JgXahXuE6d8t5ZKlMQ/kUYqy3fmB3mhUlmDnFs14V4k7PvNgPP\nlJnU+WP/4wKBgQCh7b6Se/tFJ/hKyQu99/VL7gexCISDh3Iq00S5eWiIMXftzyeh\nD6EaboV5Z3WqQDdfSPRYOVKF2tBcwh+cVnJ8CmF+STDGg3AI8CQlpcMRw9qwL9cd\n7zzf47Zh6NTHzIV4IybdQjyE79n2mBt2Ef5Hvyvc99XQgXL1EffUX0dS/QKBgEtu\nhXpU2ktnns58Z65EWnJY0WzHOq/LsoTHBOY56OvTd7OR0S0o/Sx1PcLXOibHx4yW\n2hPx8EJ+uz7T1E0CI2Jdms7aRrKxDXyHGsoQ6YCg786sGdWTNx5VEzRZL3TZSHAp\n5S51AzW5E9zjmetI+TB384PBxQ7HVo4hOQmlXEDpAoGAQ1e/MGYsvkbt+N9/MCum\nMc2VJ+ZH3SWfSMS8OmIpt3Han2TamJc0Qu71jJFd/aSJvtNHOgXJauu6ijKT/J9h\nIOp5EH5WudxIMYWfGt7QLK39t8FeNTxfu9LOmqmbFnZyclTmIlhohZPbMAAjRuJP\nMW9yoAJF7rAcnJGDtB0baI4=\n-----END PRIVATE KEY-----\n",
  "client_email": "vivek-262@portfolio-client-379113.iam.gserviceaccount.com",
  "client_id": "107939320143570186946",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vivek-262%40portfolio-client-379113.iam.gserviceaccount.com"
}
    req_headers = request.META
    gc = gspread.service_account_from_dict(cred)
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1xlP--BQTO_bxVy3p-l_-sLL-cL7XhxQdNfPl-r8sEOM/edit#gid=0')
    worksheet = sh.sheet1
    client_ip, is_routable = get_client_ip(request)
    response = requests.get(f'https://ipapi.co/{client_ip}/json/').json()
    data = [client_ip,response.get("city"),response.get("region"),response.get("country_name"),response.get("postal"),response.get("latitude"),response.get("longitude"),response.get("org")]
    worksheet.append_row(data)
    return Response("HELLO ")