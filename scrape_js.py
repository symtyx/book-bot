import json
import requests
# request url
url_endpoint = 'https://gmu.bncollege.com/'
# get response
dep_endpoint = url_endpoint + "course-material/findCourse?courseFinderSuggestion=SCHOOL_DEPARTMENT&campus=366&term=366_366_22_W&oer=false"
source = requests.get(dep_endpoint).json()
# print(source)

for dep in source:
    course_endpoint = url_endpoint + f"course-material/findCourse?courseFinderSuggestion=SCHOOL_COURSE&campus=366&term=366_366_22_W&department={dep['code']}&oer=false"
    course_source = requests.get(course_endpoint).json()
    dep['courses'] = course_source

for courses in source:
    print(f"Course DEPT Name: {courses['name']}")
    for num in courses['courses']:
        section_endpoint = url_endpoint + f"course-material/findCourse?courseFinderSuggestion=SCHOOL_COURSE_SECTION&campus=366&term=366_366_22_W&department={courses['code']}&course={num['code']}&oer=false"
        section_source = requests.get(section_endpoint).json()
        num['sections'] = section_source

with open('catalog_data.json', 'w') as outfile:
    json.dump(source, outfile, indent=4, sort_keys=True)
# FOR ALL DEPARTMENTS
# :method: GET
# :scheme: https
# :authority: gmu.bncollege.com
# :path: course-material/findCourse?courseFinderSuggestion=SCHOOL_DEPARTMENT&campus=366&term=366_366_22_W&oer=false
# Accept: */*
# Content-Type: application/json
# Cookie: s_ppv=course%2520finder%2520page%2C49%2C45%2C967%2C1%2C3; akavpau_HLX_ALLOW=1648236299~id=64796c0ec55db3850d82b991b8075236; __gads=ID=98998564bf3d2ebe-22bde656efd100d0:T=1647897348:RT=1648235696:S=ALNI_MYr2fGVKcryDM2GDeetnItrIbyQVg; s_eVar12=master%20content%20catalog; s_ips=892; s_plt=1.30; s_pltp=course%20finder%20page; s_tp=1974; s_cc=true; s_sq=%5B%5BB%5D%5D; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+25+2022+15%3A14%3A56+GMT-0400+(EDT)&version=6.21.0&hosts=&consentId=ab3e3921-e286-486d-b223-80795f7903e8&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CBG1%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _gcl_aw=GCL.1648235694.Cj0KCQjw0PWRBhDKARIsAPKHFGgb49yOX4F_6tK0TDI2P7WlT8RQjl7PAoSz0q0U_UYlqZq-6pTwivoaAkJTEALw_wcB; _gcl_dc=GCL.1648235694.Cj0KCQjw0PWRBhDKARIsAPKHFGgb49yOX4F_6tK0TDI2P7WlT8RQjl7PAoSz0q0U_UYlqZq-6pTwivoaAkJTEALw_wcB; optimizelyEndUserId=oeu1647897347313r0.9778264313208891; anonymous-consents=%5B%5D; georgemason-cart=b0be7a3e-705a-464c-9be5-d9b08133e872; gvo_s_eVar32=google; gvo_s_eVar33=cpc; gvo_s_eVar34=true; gvo_s_prop65=google; gvo_s_prop66=cpc; gvo_s_prop67=true; AMCV_98FD24485ED1CFE80A495C05%40AdobeOrg=-2121179033%7CMCIDTS%7C19077%7CMCMID%7C00103699949021612960172026794005989681%7CMCAID%7CNONE%7CMCOPTOUT-1648242894s%7CNONE%7CMCAAMLH-1648840494%7C7%7CMCAAMB-1648840494%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19080%7CvVersion%7C5.3.0; JSESSIONID=Y36-655b11ca-e59d-4454-b2e0-6c2995ac7118.accstorefront-5cf4b76cd4-p4k68; ROUTE=.accstorefront-5cf4b76cd4-p4k68; AMCV_98FD24485ED1CFE80A495C05%40AdobeOrg=0%7CMCMID%7C00103699949021612960172026794005989681; _gcl_au=1.1.1814327035.1647897348; fpestid=m2lGsxA-1OLllFDxIBiXGoulmfM_TlE7MuGdcv97ALfxwYuSxjyZOwnWy1BjDHPf-03sOw; s_cc=true; s_eVar1=mozilla%2F5.0%20(macintosh%3B%20intel%20mac%20os%20x%2010_15_7)%20applewebkit%2F605.1.15%20(khtml%2C%20like%20gecko)%20version%2F15.2%20safari%2F605.1.15; s_eVar13=george%20mason; s_eVar14=366; s_eVar15=fairfax%2Fsci%20tech%20campus; s_eVar16=Fairfax%2FSci%20Tech%20Campus; s_eVar17=linked_multicampus; s_eVar18=english; s_eVar3=anonymous; s_eVar64=true; s_eVar99=00103699949021612960172026794005989681; s_ecid=MCMID%7C00103699949021612960172026794005989681; AMCVS_98FD24485ED1CFE80A495C05%40AdobeOrg=1; cookie-notification=NOT_ACCEPTED
# Accept-Language: en-US,en;q=0.9
# Host: gmu.bncollege.com
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15
# Referer: https://gmu.bncollege.com/course-material/course-finder
# Accept-Encoding: gzip, deflate, br
# Connection: keep-alive
# X-Requested-With: XMLHttpRequest


# FOR ALL COURSES RELATIVE TO DEPT
# :method: GET
# :scheme: https
# :authority: gmu.bncollege.com
# :path: /course-material/findCourse?courseFinderSuggestion=SCHOOL_COURSE&campus=366&term=366_366_22_W&department=366_366_100&oer=false
# Accept: */*
# Content-Type: application/json
# Cookie: s_ppv=course%2520finder%2520page%2C49%2C45%2C967%2C1%2C3; akavpau_HLX_ALLOW=1648236314~id=eec63b4e15f28a6234fb56fc44ff17ac; __gads=ID=98998564bf3d2ebe-22bde656efd100d0:T=1647897348:RT=1648235696:S=ALNI_MYr2fGVKcryDM2GDeetnItrIbyQVg; s_eVar12=master%20content%20catalog; s_ips=892; s_plt=1.30; s_pltp=course%20finder%20page; s_tp=1974; s_cc=true; s_sq=%5B%5BB%5D%5D; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+25+2022+15%3A14%3A56+GMT-0400+(EDT)&version=6.21.0&hosts=&consentId=ab3e3921-e286-486d-b223-80795f7903e8&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CBG1%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _gcl_aw=GCL.1648235694.Cj0KCQjw0PWRBhDKARIsAPKHFGgb49yOX4F_6tK0TDI2P7WlT8RQjl7PAoSz0q0U_UYlqZq-6pTwivoaAkJTEALw_wcB; _gcl_dc=GCL.1648235694.Cj0KCQjw0PWRBhDKARIsAPKHFGgb49yOX4F_6tK0TDI2P7WlT8RQjl7PAoSz0q0U_UYlqZq-6pTwivoaAkJTEALw_wcB; optimizelyEndUserId=oeu1647897347313r0.9778264313208891; anonymous-consents=%5B%5D; georgemason-cart=b0be7a3e-705a-464c-9be5-d9b08133e872; gvo_s_eVar32=google; gvo_s_eVar33=cpc; gvo_s_eVar34=true; gvo_s_prop65=google; gvo_s_prop66=cpc; gvo_s_prop67=true; AMCV_98FD24485ED1CFE80A495C05%40AdobeOrg=-2121179033%7CMCIDTS%7C19077%7CMCMID%7C00103699949021612960172026794005989681%7CMCAID%7CNONE%7CMCOPTOUT-1648242894s%7CNONE%7CMCAAMLH-1648840494%7C7%7CMCAAMB-1648840494%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19080%7CvVersion%7C5.3.0; JSESSIONID=Y36-655b11ca-e59d-4454-b2e0-6c2995ac7118.accstorefront-5cf4b76cd4-p4k68; ROUTE=.accstorefront-5cf4b76cd4-p4k68; AMCV_98FD24485ED1CFE80A495C05%40AdobeOrg=0%7CMCMID%7C00103699949021612960172026794005989681; _gcl_au=1.1.1814327035.1647897348; fpestid=m2lGsxA-1OLllFDxIBiXGoulmfM_TlE7MuGdcv97ALfxwYuSxjyZOwnWy1BjDHPf-03sOw; s_cc=true; s_eVar1=mozilla%2F5.0%20(macintosh%3B%20intel%20mac%20os%20x%2010_15_7)%20applewebkit%2F605.1.15%20(khtml%2C%20like%20gecko)%20version%2F15.2%20safari%2F605.1.15; s_eVar13=george%20mason; s_eVar14=366; s_eVar15=fairfax%2Fsci%20tech%20campus; s_eVar16=Fairfax%2FSci%20Tech%20Campus; s_eVar17=linked_multicampus; s_eVar18=english; s_eVar3=anonymous; s_eVar64=true; s_eVar99=00103699949021612960172026794005989681; s_ecid=MCMID%7C00103699949021612960172026794005989681; AMCVS_98FD24485ED1CFE80A495C05%40AdobeOrg=1; cookie-notification=NOT_ACCEPTED
# Accept-Language: en-US,en;q=0.9
# Host: gmu.bncollege.com
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15
# Referer: https://gmu.bncollege.com/course-material/course-finder
# Accept-Encoding: gzip, deflate, br
# Connection: keep-alive
# X-Requested-With: XMLHttpRequest

# FOR ALL COURSE SECTIONS
# :method: GET
# :scheme: https
# :authority: gmu.bncollege.com
# :path: /course-material/findCourse?courseFinderSuggestion=SCHOOL_COURSE_SECTION&campus=366&term=366_366_22_W&department=366_366_100&course=203&oer=false
# Accept: */*
# Content-Type: application/json
# Cookie: s_ppv=course%2520finder%2520page%2C49%2C45%2C967%2C1%2C3; akavpau_HLX_ALLOW=1648236460~id=a9c32a461ab01df39d6fc3622e1849a3; __gads=ID=98998564bf3d2ebe-22bde656efd100d0:T=1647897348:RT=1648235696:S=ALNI_MYr2fGVKcryDM2GDeetnItrIbyQVg; s_eVar12=master%20content%20catalog; s_ips=892; s_plt=1.30; s_pltp=course%20finder%20page; s_tp=1974; s_cc=true; s_sq=%5B%5BB%5D%5D; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+25+2022+15%3A14%3A56+GMT-0400+(EDT)&version=6.21.0&hosts=&consentId=ab3e3921-e286-486d-b223-80795f7903e8&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CBG1%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _gcl_aw=GCL.1648235694.Cj0KCQjw0PWRBhDKARIsAPKHFGgb49yOX4F_6tK0TDI2P7WlT8RQjl7PAoSz0q0U_UYlqZq-6pTwivoaAkJTEALw_wcB; _gcl_dc=GCL.1648235694.Cj0KCQjw0PWRBhDKARIsAPKHFGgb49yOX4F_6tK0TDI2P7WlT8RQjl7PAoSz0q0U_UYlqZq-6pTwivoaAkJTEALw_wcB; optimizelyEndUserId=oeu1647897347313r0.9778264313208891; anonymous-consents=%5B%5D; georgemason-cart=b0be7a3e-705a-464c-9be5-d9b08133e872; gvo_s_eVar32=google; gvo_s_eVar33=cpc; gvo_s_eVar34=true; gvo_s_prop65=google; gvo_s_prop66=cpc; gvo_s_prop67=true; AMCV_98FD24485ED1CFE80A495C05%40AdobeOrg=-2121179033%7CMCIDTS%7C19077%7CMCMID%7C00103699949021612960172026794005989681%7CMCAID%7CNONE%7CMCOPTOUT-1648242894s%7CNONE%7CMCAAMLH-1648840494%7C7%7CMCAAMB-1648840494%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19080%7CvVersion%7C5.3.0; JSESSIONID=Y36-655b11ca-e59d-4454-b2e0-6c2995ac7118.accstorefront-5cf4b76cd4-p4k68; ROUTE=.accstorefront-5cf4b76cd4-p4k68; AMCV_98FD24485ED1CFE80A495C05%40AdobeOrg=0%7CMCMID%7C00103699949021612960172026794005989681; _gcl_au=1.1.1814327035.1647897348; fpestid=m2lGsxA-1OLllFDxIBiXGoulmfM_TlE7MuGdcv97ALfxwYuSxjyZOwnWy1BjDHPf-03sOw; s_cc=true; s_eVar1=mozilla%2F5.0%20(macintosh%3B%20intel%20mac%20os%20x%2010_15_7)%20applewebkit%2F605.1.15%20(khtml%2C%20like%20gecko)%20version%2F15.2%20safari%2F605.1.15; s_eVar13=george%20mason; s_eVar14=366; s_eVar15=fairfax%2Fsci%20tech%20campus; s_eVar16=Fairfax%2FSci%20Tech%20Campus; s_eVar17=linked_multicampus; s_eVar18=english; s_eVar3=anonymous; s_eVar64=true; s_eVar99=00103699949021612960172026794005989681; s_ecid=MCMID%7C00103699949021612960172026794005989681; AMCVS_98FD24485ED1CFE80A495C05%40AdobeOrg=1; cookie-notification=NOT_ACCEPTED
# Accept-Language: en-US,en;q=0.9
# Host: gmu.bncollege.com
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15
# Referer: https://gmu.bncollege.com/course-material/course-finder
# Accept-Encoding: gzip, deflate, br
# Connection: keep-alive
# X-Requested-With: XMLHttpRequest

# write method and get all departments and save it in a file...
    # with each department, loop through with the department parameter using the department_id (i.e. department=366_366_100)
        # with each course number, loop through those and get the section numbers relative to the course parameter













